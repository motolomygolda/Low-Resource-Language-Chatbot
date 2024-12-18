from rouge_score import rouge_scorer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def evaluate_response(reference, generated):
    """Evaluate the chatbot response using BLEU and ROUGE."""
    # ROUGE evaluation
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(reference, generated)

    # BLEURT evaluation
    bleurt_model_name = "google/bleurt-base-128"
    tokenizer = AutoTokenizer.from_pretrained(bleurt_model_name)
    model = AutoModelForSequenceClassification.from_pretrained(bleurt_model_name)

    inputs = tokenizer(reference, generated, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    bleurt_score = torch.sigmoid(outputs.logits).item()

    return {
        "ROUGE-1": rouge_scores["rouge1"].fmeasure,
        "ROUGE-L": rouge_scores["rougeL"].fmeasure,
        "BLEURT": bleurt_score
    }
