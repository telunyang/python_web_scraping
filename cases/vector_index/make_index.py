'''
匯入套件
'''
import os
from sentence_transformers import SentenceTransformer
import faiss

# 索引預設變數
index = None

'''
[faiss.IndexFlatL2]
使用歐氏距離

[faiss.IndexFlatIP]
IP = Inner Product，
測試使用 Inner Product 來比較 features 資料
同時進行 feature normalization
等同於 cosine similarity
'''

# 模型名稱
model_name = 'sentence-transformers/distiluse-base-multilingual-cased-v1'

# 索引存放路徑
index_path = './vector.index'

# 讀取 model
bi_encoder = SentenceTransformer(model_name)

# 「句子」與對應的「句子 ID」(需要 int)
listSentences = [
    '我每天都被自己帥醒，壓力好大', 
    '別瞎掰好嗎', 
    '願你有個美好的一天', 
]
listIds = [1, 2, 3]

# 將所有句子轉換成向量，同時計算轉向量時間
embeddings = bi_encoder.encode(
    listSentences, 
    batch_size=4,
    show_progress_bar=True,
    normalize_embeddings=False # 建議先查詢預訓練模型是否支援
)

# 讀取索引，不存在就初始化
if not os.path.exists(index_path):
    dims = embeddings.shape[1]
    index = faiss.IndexFlatIP(dims) # 初始化索引的維度
    index = faiss.IndexIDMap(index) # 讓 index 有記錄對應 doc id 的能力
else:
    # 索引存在，直接讀取
    index = faiss.read_index(index_path)

# 加入 doc id 到 對應的 vector
index.add_with_ids(embeddings, listIds) # 加入 向量 與 文件ID
# index.add(embeddings) # 僅加入向量

# 儲存索引
faiss.write_index(index, index_path)

# 釋放記憶體
del index, embeddings