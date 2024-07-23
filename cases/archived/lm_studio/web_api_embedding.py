# Make sure to `pip install openai` first
from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_embedding(text, model="nomic-ai/nomic-embed-text-v1.5-GGUF"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

vector_example = get_embedding("Once upon a time, there was a cat.")
print(vector_example) # 句向量
print("=" * 50)
print("向量維度:", len(vector_example)) # 維度
print("=" * 50)

# 計算兩個句子的相似度
import numpy as np
text_a = "Once upon a time, there was a cat."
text_b = "Long times ago, there was a cat."
vector_text_a = get_embedding(text_a)
vector_text_b = get_embedding(text_b)

# 透過 cosine similarity 計算相似度
cosine_similarity = np.dot(vector_text_a, vector_text_b) / (np.linalg.norm(vector_text_a) * np.linalg.norm(vector_text_b))
print(cosine_similarity)
print(f"{cosine_similarity * 100:.4f} % 相似度")
