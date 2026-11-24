# models

Load for Hugging Face assets, embeddings, retrieval and evaluation.

## hub

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification

ds = load_dataset("acme/invoices", split="train", streaming=True)
tok = AutoTokenizer.from_pretrained("distilbert-base-uncased", revision="main")
```

- Pin the revision. `main` moves under you and breaks a reproduced result.
- Check the license and the card before use: `datasets-server` reports size and splits.
- `streaming=True` for a corpus larger than memory; you lose shuffling.
- Tokenizer max length truncates silently. Log the truncated fraction; over 5% means the wrong length.

## embeddings

| decision | rule |
| --- | --- |
| model | one model per index, revision pinned |
| distance | cosine for normalized vectors, dot for trained embeddings |
| dimension | fixed; a change means a full reindex |
| normalization | normalize once, at write time |
| chunking | by structure, 300-800 tokens, 10-20% overlap |
| metadata | store source id and as-of date with every vector |

Mixing vectors from two models returns plausible garbage: distances are meaningless across spaces.

## retrieval eval

```python
def recall_at_k(queries, k=10):
    hits = sum(1 for q in queries if q.gold_id in search(q.text, k))
    return hits / len(queries)
```

- Build 50-200 query and gold-document pairs from real usage.
- Report recall@k and MRR with n. A single anecdote is not a retrieval metric.
- Test the reranker separately from the retriever, or you cannot tell which helped.
- Partition by tenant before measuring, or a cross-tenant hit inflates the score.

## evaluation

| task | metric | trap |
| --- | --- | --- |
| classification | precision, recall, F1 per class | accuracy hides a rare class |
| extraction | field-level exact match | normalizing away real errors |
| ranking | recall@k, MRR, nDCG | evaluating on the training corpus |
| generation | rubric, 2 judges | judge agrees with everything |
| vision | mAP, IoU per class | one class dominating |

Report n, the split and the date. A metric without them cannot be compared.

## leakage checklist

- Duplicate rows across splits: hash the entity key and intersect.
- Time-ordered data split randomly: split by time.
- Target encoded in a feature name: check column provenance.
- Normalization fitted on the full set before splitting: fit on train only.

## computer vision

- torchvision pipeline: `Resize(256)`, `CenterCrop(224)`, `Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])` for ImageNet weights. Wrong normalization runs fine and halves accuracy.
- cv2 reads BGR, PIL reads RGB. A model trained on RGB fed BGR still runs and scores worse with no error.
- Augment the train split only: flip, crop, color jitter. A flip on OCR or on medical laterality is a label error.
- Split by image group or patient id. Near-duplicate frames leak across a random split and inflate the score.
- Metrics: mAP@0.5 with IoU 0.5 for detection, per-class recall for an imbalanced set.
- `model.eval()` and `torch.no_grad()` at inference. Batch norm in train mode makes the same input score differently each run.
