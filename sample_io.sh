cd samples
sample=$1
rm $sample
while true; do
    pid=$(ps aux | grep "postgres: postgres postgre[s]" | awk '{print $2}')
    if [[ ! -z "$pid" ]]; then
        break
    fi
done
python3 /root/iotop/iotop.py -b -p $pid >> $sample
# i=0
# while true; do
#     let i+=1
#     python3 /root/iotop/iotop.py -b -p $pid >> $sample
#     echo $i >> $sample
#     # echo "-----------------------------------------------------------------------------" >> $sample
#     sleep 1
# done

