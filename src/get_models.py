# %%
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification


def get_ner_tokenizer():
    return AutoTokenizer.from_pretrained("dslim/bert-base-NER")


def get_ner_model():
    return AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")


def save_model(model, tokenizer, path):
    model.save_pretrained(path)
    tokenizer.save_pretrained(path)


if __name__ == "__main__":

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = get_ner_model()
    tokenizer = get_ner_tokenizer()
    save_model(model, tokenizer, "./models/dslim/bert-base-NER")
    print("ner_model saved")


# %%
