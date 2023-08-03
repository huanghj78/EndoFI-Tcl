cd samples
sample=$1
rm $sample
while true; do
    pid=$(ps aux | grep "postgres: postgres postgre[s]" | awk '{print $2}')
    if [[ ! -z "$pid" ]]; then
        break
    fi
done
top -b -d 1 -p $pid > $sample

