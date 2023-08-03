#!/bin/bash
pgbench -r -T60
python3 main.py ./config/cpu.yaml

