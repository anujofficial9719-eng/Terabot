#!/bin/bash

echo "🚀 Starting TeraBot..."

# create downloads folder
mkdir -p downloads

# start aria2
echo "⚡ Starting aria2..."
aria2c \
--enable-rpc \
--rpc-listen-all=true \
--rpc-allow-origin-all \
--max-connection-per-server=16 \
--split=16 \
--min-split-size=1M \
--file-allocation=none \
--daemon=true

sleep 2

# start API
echo "🌐 Starting API..."
nohup python3 api.py > api.log 2>&1 &

sleep 2

# start Bot
echo "🤖 Starting Bot..."
nohup python3 bot.py > bot.log 2>&1 &

echo "✅ All services started!"
