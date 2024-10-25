'''
匯入套件
'''
from sentence_transformers import SentenceTransformer
import faiss

# 基本設定
model_name = 'sentence-transformers/distiluse-base-multilingual-cased-v1'
bi_encoder = SentenceTransformer(model_name)

# 讀取索引
index_path = './vector.index'
index = faiss.read_index(index_path)

# 查詢句子
list_query = ['不要亂說話', '希望你一整天都開心']

# 將查詢句子轉換成向量
embeddings = bi_encoder.encode(
    list_query, 
    batch_size=4, 
    show_progress_bar=False,
    normalize_embeddings=False
)

# 查詢
D, I = index.search(embeddings, k=3)

# 顯示結果
list_scores = D.tolist()
list_ids = I.tolist()
print(f"相似度: {list_scores}")
print(f"檢索的 Document IDs 為: {list_ids}")

# 釋放記憶體
del index, embeddings