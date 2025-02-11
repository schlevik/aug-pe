mlm_prob=0.5
var_type="hallmarks_of_cancer_rephrase_tone"
feat_ext="kamalkraj/BioSimCSE-BioLinkBERT-BASE"
length=64
temperature=1.4
num_seed_samples=1472
lookahead_degree=0
k=6 # number of variations
L=$((k+1))
init_L=${L}
num_samples=$((L*num_seed_samples))
echo generating $num_samples samples
epochs=10
word_var_scale=0
select_syn_mode=rank
#model_type=gpt2  
# model_type=microsoft/biogpt
model_type=meta-llama/Llama-3.2-1B-Instruct
# noise=0
# noise=22.16 # e=0.5
# noise=11.76 # e=1
# noise=6.28 # e=2
# noise=3.41 # e=4 
args=""
cls_batch_size=32
api="HFGPT"
feature_extractor_batch_size=1024
if [ "$model_type" = "gpt2-large" ]; then
    batch_size=64
elif [ "$model_type" = "gpt2-medium" ]; then
    batch_size=128
elif [ "$model_type" = "gpt2" ]; then
    batch_size=512
else
    batch_size=224
fi

# ### load datacheckpoint 
# data_checkpoint_args=""
# for  (( iter=0; iter<=epochs; iter++ ))
# do
# train_file=${result_folder}/${iter}/samples.csv
# if [ -e "$train_file" ]; then
#     echo "$train_file does exist."
#     # load from  data checkpoint
#     data_checkpoint_args="--data_checkpoint_step ${iter} --data_checkpoint_path ${result_folder}/${iter}/samples.csv"
# else
#     echo "$train_file does not exist."
# fi
# done
# echo load data from ${data_checkpoint_args} ${args}


# noise=22.16 # e=0.5
# noise=11.76 # e=1
# noise=6.28 # e=2
# noise=3.41 # e=4 
# "0" "6.28"
for noise in "0" "6.28" "22.16" "11.76" "3.41"; do 
    ### run PE
    echo "Noise level ${noise}."
    result_folder="result/hallmarks_of_cancer/${model_type}_${feat_ext//\//_}/${num_samples}_n${noise}_L${L}_initL${init_L}_var${lookahead_degree}_${var_type}_${select_syn_mode}_len${length}var${word_var_scale}_t${temperature}"
    echo $result_folder
    python main.py ${args} ${data_checkpoint_args} \
    --dataset cls/hallmarks_of_cancer \
    --train_data_file ../../data/cls/hallmarks_of_cancer/original/train-original.jsonl \
    --api ${api} \
    --noise ${noise} \
    --model_type ${model_type} \
    --do_sample  \
    --length ${length} \
    --random_sampling_batch_size ${batch_size} \
    --variation_batch_size ${batch_size} \
    --temperature ${temperature} \
    --select_syn_mode ${select_syn_mode} \
    --num_samples_schedule ${num_samples} \
    --combine_divide_L ${L} \
    --init_combine_divide_L ${init_L} \
    --variation_degree_schedule ${mlm_prob} \
    --lookahead_degree ${lookahead_degree} \
    --epochs ${epochs} \
    --feature_extractor ${feat_ext} \
    --feature_extractor_batch_size ${feature_extractor_batch_size} \
    --mlm_probability ${mlm_prob} \
    --variation_type ${var_type} \
    --result_folder ${result_folder} \
    --log_online \
    --apply_template \
    --train_data_embeddings_file result/embeddings/kamalkraj_BioSimCSE-BioLinkBERT-BASE/cls_hallmarks_of_cancer_train_all.embeddings.npz
done 