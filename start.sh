#!/bin/bash

echo "Starting aria2..."
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all &

echo "Starting API..."
python3 api.py &

echo "Starting Bot..."
python3 bot.py
