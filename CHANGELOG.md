# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- 搜索功能支持
- 新增迭代二 KB 排障命令文档（acli system 子命令承载）
  - 完全只读新增命令（15 个）：blkid、dig、dmesg、id、iperf3、lscpu、md5sum、nslookup、sar、ss、turbostat、traceroute、uptime、which、who
  - 部分只读新增命令（8 个）：arp、chkconfig、diff、fdisk、find、iptables、qemu-img、route
  - curl 接口放通命令（1 个）：curl（acli system curl，承载 100 条 GET API）
  - 既有命令路径白名单扩展（4 个）：cat、du、grep、ls（分别挂载 cat 命令族与 ls 命令族的共用路径白名单）

## [0.1.0] - 2025-08-01
### Added
- 新增acli命令说明文档
- 新增一键启动/停止/重启脚本
- 新增自动部署脚本
