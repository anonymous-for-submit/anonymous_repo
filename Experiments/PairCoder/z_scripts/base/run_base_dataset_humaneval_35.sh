model=gpt-35-turbo
dataset=humaneval
split_name=plus
python /data/zlyuaj/muti-agent/PairCoder/src/main_fuzz_passAt10_baseDataset.py \
    --dataset humaneval \
    --split_name ${split_name} \
    --model ${model}\
    --dir_path results \
    --input_path /data/zlyuaj/muti-agent/PairCoder/data/HumanEval_Plus.jsonl\
    --output_path  ./outputs/ \
    --output_file_name ${dataset}_${model} \
    --num_generate 10\
    # --start_idx 132
