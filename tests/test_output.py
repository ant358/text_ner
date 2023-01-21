import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification
from src.output import NerResults
from src.input import text_input

model = AutoModelForTokenClassification.from_pretrained(
    './models/dslim/bert-base-NER')
tokenizer = AutoTokenizer.from_pretrained('./models/dslim/bert-base-NER')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def test_ner_results():
    text = text_input()
    ner_results = NerResults(text['text'], model, tokenizer, device)
    assert len(ner_results.ner_results) > 0


def test_ner_df():
    text = text_input()
    ner_results = NerResults(text['text'], model, tokenizer, device)
    assert type(ner_results.ner_df) == pd.DataFrame


def test_entities():
    text = text_input()
    ner_results = NerResults(text['text'], model, tokenizer, device)
    result = ner_results.unique_entities
    assert len(result) > 0


def test_entities2():
    text = text_input()
    ner_results = NerResults(text['text'], model, tokenizer, device)
    result = ner_results.unique_entities
    assert "score" in result.columns


def test_entities3():
    text = text_input()
    ner_results = NerResults(text['text'], model, tokenizer, device)
    result = ner_results.unique_entities
    assert "Liege" in result.word.to_list()
