from dpsda.feature_extractor import extract_features
from dpsda.logging import log_embeddings
import os
from dpsda.data_loader import load_data
import argparse
from apis.utils import set_seed



all_feature_extractor = ["sentence-t5-xl", "sentence-t5-large", "sentence-t5-base",
                         "all-MiniLM-L6-v2",  "all-mpnet-base-v2",
                         "paraphrase-MiniLM-L6-v2",
                         "distilbert-base-nli-stsb-mean-tokens", "roberta-large-nli-stsb-mean-tokens"]

data_files = {'pubmed': 'data/pubmed/train.csv',
              'yelp': 'data/yelp/train.csv',
              'openreview': 'data/openreview/iclr23_reviews_train.csv',
              'cas': 'data/bigbio-datasets/',
              'cls/psytar': '../../data/cls/psytar/original/train-original.jsonl',
              'cls/hallmarks_of_cancer': '../../data/cls/hallmarks_of_cancer/original/train-original.jsonl',
              'cls/mimic': '../../data/cls/mimic/original/mimic-train-chapter.jsonl',
              'cls/n2c2_2008': '../../data/cls/n2c2_2008/original/train-original.jsonl',
              }
parser = argparse.ArgumentParser()
parser.add_argument("--model_name_or_path", type=str,
                    default="stsb-roberta-base-v2", required=False)
parser.add_argument("--dataset", type=str, default="yelp",
                    choices=data_files.keys(),
                    required=False)

args = parser.parse_args()
set_seed(seed=0, n_gpu=1)


feature_extractor = args.model_name_or_path


all_private_samples, all_private_labels, private_labels_counter, private_labels_indexer = load_data(
    dataset=args.dataset,
    data_file=data_files[args.dataset],
    num_samples=-1)

all_private_features = extract_features(
    data=all_private_samples,
    batch_size=10000,
    model_name=feature_extractor,
)

log_embeddings(all_private_features, all_private_labels[:len(all_private_features)],
               os.path.join('result', 'embeddings', feature_extractor.replace('/', '_')), fname=f"{args.dataset.replace('/', '_')}_train_all")


print("finished!")
