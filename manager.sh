#!/usr/bin/env bash
# 服务的外置管理脚本，Windows 下请使用 Git-Bash / MSYS2 / Cygwin
# 用法: bash manager.sh init|start|stop|restart|status [port]

# 0. 如有中文乱码，可取消下面注释
# export LANG=zh_CN.UTF-8        # Linux
# chcp 65001 > /dev/null         # Windows

set -euo pipefail

logfile="app.log"
pidfile="app.pid"
DIR="$(dirname "$0")"
cd "$DIR" || exit 1

# 启动服务
function start() {
    local port=${1:-6888}

    # 端口占用检查：占用即报错
    case "$(uname -s)" in
    Linux* | Darwin*)
        lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 && {
            echo ">>> 错误，端口 $port 已被占用"
            return 1
        }
        ;;
    MINGW* | CYGWIN* | MSYS*)
        netstat -ano | grep -qE ":$port .*LISTENING" && {
            echo ">>> 错误，端口 $port 已被占用"
            return 1
        }
        ;;
    esac

    # 1. 构建阶段（同步）
    echo ">>> 开始构建"
    echo "..."
    npm run build >>"$logfile" 2>&1

    # 2. 启动服务（后台）
    echo ">>> 启动服务"
    nohup npm run serve -- --port "$port" >>"$logfile" 2>&1 </dev/null &

    # 3. 健康检查
    for ((i = 1; i <= 60; i++)); do
        if curl -s "http://localhost:$port" >/dev/null; then
            case "$(uname -s)" in
            Linux* | Darwin*)
                pid=$(lsof -t -i :$port)
                ;;
            MINGW* | CYGWIN* | MSYS*)
                pid=$(netstat -ano | grep ":$port " | awk '{print $5}' | sed 's/[^0-9]*//g' | head -n 1)
                ;;
            esac
            echo "$pid" >"$pidfile"
            echo ""
            echo ">>> 服务启动成功，端口: $port，日志: $logfile，PID: $(cat "$pidfile")"
            echo ">>> 访问地址: http://localhost:$port"
            return 0
        fi
        printf "."
        sleep 1
    done

    echo ""
    echo ">>> 启动超时(60s)，请检查日志: $logfile"
    return 1
}

# 停止服务
function stop() {
    if [[ ! -f $pidfile ]]; then
        echo ">>> 警告，找不到 $pidfile，请确认服务是否启动过，即将跳过停止服务"
        return 0
    fi

    pid=$(cat "$pidfile")
    [[ $pid =~ ^[0-9]+$ ]] || {
        echo ">>> 警告，$pidfile 中无有效 PID，请确认服务是否启动过，即将跳过停止服务"
        return 0
    }

    case "$(uname -s)" in
    Linux*) OS=Linux ;;
    MINGW* | CYGWIN* | MSYS*) OS=Windows ;;
    *)
        echo ">>> 错误，不支持的操作系统"
        return 1
        ;;
    esac

    echo ">>> 当前系统: $OS , 即将关闭进程号为 $pid 的进程服务"

    if [ "$OS" = "Linux" ]; then
        if ! kill -0 "$pid" 2>/dev/null; then
            echo ">>> 进程 $pid 不存在"
            rm -f "$pidfile"
            return 0
        fi
        kill -TERM "$pid"
        sleep 2
        if kill -0 "$pid" 2>/dev/null; then
            echo ">>> 强制杀死 $pid"
            kill -KILL "$pid"
        fi
    else
        if ! taskkill //PID "$pid" //F 2>/dev/null; then
            echo ">>> 进程 $pid 不存在或已退出"
        else
            echo ">>> 进程 $pid 已终止"
        fi
    fi

    rm -f "$pidfile"
    echo ">>> 服务已停止"
    return 0
}

# 重启服务
function restart() {
    stop
    start "$@"
    return $?
}

# 查看服务状态
function status() {
    local port=${1:-6888}
    if [[ -f $pidfile ]]; then
        pid=$(cat "$pidfile")
        if kill -0 "$pid" 2>/dev/null; then
            if curl -s "http://localhost:$port" >/dev/null; then
                echo ">>> 服务已开启，进程号: $pid"
            else
                echo ">>> 进程 $pid 存在，但端口 $port 无响应，请检查服务是否僵死"
            fi
        else
            echo ">>> 进程 $pid 已不存在，存在 app.pid 文件残留，请检查"
        fi

    else
        echo ">>> 服务未开启"
    fi
}

# 主入口
case "${1:-}" in
init) npm install ;;
start) start "${2:-}" ;;
stop) stop ;;
restart) restart "${2:-}" ;;
status) status "${2:-}" ;;
*)
    echo "用法: $0 init|start|stop|restart|status [port]"
    exit 1
    ;;
esac
