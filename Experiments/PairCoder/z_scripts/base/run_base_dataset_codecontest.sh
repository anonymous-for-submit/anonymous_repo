model=gpt-35-turbo
dataset=codecontest
split_name=test
python /data/zlyuaj/muti-agent/PairCoder/src/main_fuzz_passAt10_baseDataset.py \
    --dataset ${dataset} \
    --split_name ${split_name} \
    --dir_path results \
    --model ${model}\
    --input_path /data/zlyuaj/muti-agent/PairCoder/data/CodeContest_Test.jsonl\
    --output_path  ./outputs/ \
    --output_file_name ${dataset}_${model} \
    --num_generate 10
