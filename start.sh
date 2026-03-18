#!/bin/bash

aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all &

python3 api.py &
python3 bot.py
