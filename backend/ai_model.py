from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

def get_code_embedding(code):

    inputs = tokenizer(code, return_tensors="pt", truncation=True, padding=True)

    outputs = model(**inputs)

    embedding = outputs.last_hidden_state.mean(dim=1)

    return embedding.detach().numpy()