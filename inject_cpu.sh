while true; do
    pid=$(ps aux | grep "postgres: postgres postgre[s]" | awk '{print $2}')
    if [[ ! -z "$pid" ]]; then
        break
    fi
done
echo $pid
sed -i -E "s/pid: [0-9]+/pid: $pid/" ./config/cpu.yaml
# sleep 10s
python3 main.py ./config/cpu.yaml

