from datasets import load_dataset, Dataset
from pathlib import Path

from scgpt_utlis.gene_tokenizer import GeneVocab # nested use

special_tokens = ["<pad>", "<cls>", "<eoc>"]

parquet_dir = '/home00/liss/Study/cellxgene/scb/prostate'


def test_func():
    pass


def add_cls(parquet_dir):
    # If there many parquet files, load_dataset will merge automatically
    parquet_files = [str(f) for f in Path(parquet_dir).glob("*.parquet")]
    cache_dir = Path(parquet_dir).parent / "cache"

    vocab_file = Path(parquet_dir) / "gene_vocab.json"
    vocab = GeneVocab.from_file(vocab_file)
    # for s in special_tokens:
    #     if s not in vocab:
    #         # vocab.append_token(s)
    #         vocab.insert_token(s, 0)

    cls_prefix_datatable = Path(parquet_dir) / "cls_prefix_data.parquet"

    if not cls_prefix_datatable.exists():
        print("preparing cls prefix dataset")
        raw_dataset = load_dataset(
            "parquet",
            data_files=parquet_files,
            split="train",
            cache_dir=str(cache_dir))  # Default: "~/datasets"
        raw_dataset = _map_append_cls(raw_dataset, vocab)
        raw_dataset.to_parquet(str(cls_prefix_datatable))

def _map_append_cls(dataset: Dataset, vocab: GeneVocab, cls_value: int = -2) -> Dataset:
    dataset = dataset.map(
        lambda example: {
            "genes": [vocab["<cls>"]] + example["genes"],
            "expressions": [cls_value] + example["expressions"],
        },
        # batched=True,  # not using since then the map func needs to loop
        # num_proc=len(os.sched_getaffinity(0)),
    )

    return dataset
