#!/bin/bash
# stop_freqtrade.sh
# 根据 PID 文件停止 freqtrade 进程

PIDFILE="freqtrade.pid"

if [ ! -f "$PIDFILE" ]; then
    echo "PID 文件不存在，可能进程未启动。"
    exit 1
fi

PID=$(cat "$PIDFILE")
# 尝试停止该进程
if kill "$PID" > /dev/null 2>&1; then
    echo "成功停止 PID 为 $PID 的进程。"
    rm -f "$PIDFILE"
else
    echo "无法停止 PID 为 $PID 的进程。请检查是否具有权限或进程是否仍在运行。"
fi