# 向量索引 (Vector Index)

## Windows 環境 - CPU Only 版本
- 安裝建立 C 和 C++ 應用程式所需的元件 (請下載 Community 版本)
  - [連結](https://visualstudio.microsoft.com/zh-hant/vs/features/cplusplus/)
- 使用 FAISS 建立向量索引
  - [安裝說明](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)
  - 安裝指令:
    - `conda install -c pytorch faiss-cpu=1.8.0` 或 `conda install -c conda-forge faiss-cpu`
- 安裝 Sentence Transformers
  - [安裝說明](https://sbert.net/docs/installation.html)
  - 安裝指令:
    - `pip install -U sentence-transformers` 或 `conda install -c conda-forge sentence-transformers`
- 範例模型
  - [Pretrained Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html#semantic-search-models)
- 執行程式
  - `python make_index.py`
  - 如果出現 `ImportError: DLL load failed while importing _multiarray_umath: 找不到指定的模組。`
    - 步驟一: 先安裝 numpy 2.0 `pip install numpy==2.0`
    - 步驟二: 再安裝 numpy 小於 2.0 的版本 `pip install numpy==1.26.4`
    - 步驟三: 重新執行程式 `python make_index.py`
    - 如果還有問題，可以試試安裝 `pip install pybind11==2.12`