#!/bin/bash
# start_freqtrade.sh
# 后台运行 freqtrade，同时将日志输出到 freqtrade.log

# 定义日志文件与 PID 文件
LOGFILE="freqtrade.log"
PIDFILE="freqtrade.pid"

# 启动 freqtrade 的 trade 模式，注意 nohup 会使进程在后台持续运行
nohup freqtrade trade -c ./user_data/config_live.json --strategy E0V1E > "$LOGFILE" 2>&1 &

# 将新启动进程的 PID 保存到文件中
echo $! > "$PIDFILE"

echo "Freqtrade 已启动，PID=$(cat "$PIDFILE")"
echo "日志输出见: $LOGFILE"