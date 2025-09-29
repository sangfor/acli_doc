---
sidebar_position: 10
---

# fio
操作概述: 调用系统fio命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system fio
```

结果示例:
```bash
No jobs(s) defined

fio-2.1.10
fio [options] [job options] <job file(s)>
  --debug=options       Enable debug logging. May be one/more of:
                        process,file,io,mem,blktrace,verify,random,parse,
                        diskutil,job,mutex,profile,time,net,rate
  --parse-only          Parse options only, don't start any IO
  --output              Write output to file
  --runtime             Runtime in seconds
  --latency-log         Generate per-job latency logs
  --bandwidth-log       Generate per-job bandwidth logs
  --minimal             Minimal (terse) output
  --output-format=x     Output format (terse,json,normal)
  --terse-version=x     Set terse version output format to 'x'
  --version             Print version info and exit
  --help                Print this page
  --cpuclock-test       Perform test/validation of CPU clock
  --crctest             Test speed of checksum functions
  --cmdhelp=cmd         Print command help, "all" for all of them
  --enghelp=engine      Print ioengine help, or list available ioengines
  --enghelp=engine,cmd  Print help for an ioengine cmd
  --showcmd             Turn a job file into command line options
  --eta=when            When ETA estimate should be printed
                        May be "always", "never" or "auto"
  --eta-newline=time    Force a new line for every 'time' period passed
  --status-interval=t   Force full status dump every 't' period passed
  --readonly            Turn on safety read-only checks, preventing writes
  --section=name        Only run specified section in job file
  --alloc-size=kb       Set smalloc pool to this size in kb (def 1024)
  --warnings-fatal      Fio parser warnings are fatal
  --max-jobs=nr         Maximum number of threads/processes to support
  --server=args         Start a backend fio server
  --daemonize=pidfile   Background fio server, write pid to file
  --client=hostname     Talk to remote backend fio server at hostname
  --idle-prof=option    Report cpu idleness on a system or percpu basis
                        (option=system,percpu) or run unit work
                        calibration only (option=calibrate)

Fio was written by Jens Axboe <jens.axboe@oracle.com>
                   Jens Axboe <jaxboe@fusionio.com>
                   Jens Axboe <axboe@fb.com>
```