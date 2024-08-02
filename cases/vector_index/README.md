# 向量索引 (Vector Index)

## Windows 環境
- 使用 FAISS 建立向量索引
  - [安裝說明](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)
- 安裝 Sentence Transformers
  - [安裝說明](https://sbert.net/docs/installation.html)
- 範例模型
  - [Pretrained Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#semantic-search-models)
- 如果出現 `ImportError: DLL load failed while importing _multiarray_umath: 找不到指定的模組。`
  - 安裝 numpy 小於 2.0 的版本: `pip install numpy==1.26.4`
  - 如果還有問題，可以試試安裝: `pip install pybind11==2.12`