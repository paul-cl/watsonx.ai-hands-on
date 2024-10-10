# watsonx.ai evn 만들기

language
```
python3.11
```

hardware configuration
```
4vCPU and 16G ram
```
å
software configuration
```
Runtime 24.1 on python 3.11
```


```yaml
channels:
  - defaults  

dependencies:
  - pip # keep this conda dependency when installing packages via pip: below
  - pip:
    - grpcio==1.60.0
    - pymilvus
    - ipython-sql==0.4.1
    - sqlalchemy==1.4.46
    - pyhive[presto]
    - python-dotenv
    - sentence_transformers
    - langchain>=0.1.14
    - langchain-ibm>=0.1.3
    - ibm-generative-ai
    - requests>=2.30.0
    - PyPDF2
    - langchain-community
    - langchain-huggingface
```