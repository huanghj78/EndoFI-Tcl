while true; do
    pid=$(ps aux | grep "postgres: postgres postgre[s]" | awk '{print $2}')
    if [[ ! -z "$pid" ]]; then
        break
    fi
done
echo $pid
sed -i -E "s/pid: [0-9]+/pid: $pid/" ./config/slow_sql.yaml
python3 main.py ./config/slow_sql.yaml

