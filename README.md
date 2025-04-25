# watsonx.ai-hands-on
watsonx.ai hands-on lab 자료입니다.

### IBM에서 제공하는 모델 정보
https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models.html?context=wx&audience=wdp

### IBM에서 더이상 제공하지 않는 모델 정보
https://www.ibm.com/docs/en/watsonx-as-a-service?topic=models-foundation-model-lifecycle

### 모델 ID 참조 사이트
https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html


# lab2. Prompt Engineering
### 1. Zero Shot

#### Structured Mode (p13)
Instruction
```
주어진 특성을 가진 회사에 대한 5문장 마케팅 메시지를 생성합니다.
```
프롬픔트를 실행합니다.
```
특성:
회사소개 - 골든뱅크
제안에는 수수료 없음, 5% 이자율, 최소 잔액 없음
어조 – 정보 제공
응답 요청 - 링크를 클릭하십시오.
종료일 - 7월 15일
```
   
#### Chat Mode (p14)
```
주어진 특성을 가진 회사에 대한 5문장 마케팅 메시지를 생성합니다.
특성:
회사소개 - 골든뱅크
제안에는 수수료 없음, 5% 이자율, 최소 잔액 없음
어조 – 정보 제공
응답 요청 - 링크를 클릭하십시오.
종료일 - 7월 15일
```

#### Freedom Mode (p15)
prompt
```
The following paragraph is a consumer complaint.
Read the following paragraph and list all the issues. 

I called your helpdesk
multiple times and every time I waited 10-15 minutes before I gave up. The first time I got through, the line got cut suddenly and I had to call back. This is just not helpful. When I finally got through like after 3 days (yes, 3 days) your agent kept going over a long checklist of trivial things and asking me to verify, after I repeatedly told the agent that I am an experienced user and I know what I am doing. It was a complete waste of time. After like an eternity of this pointless conversation, I was told that an SME will contact me. That – was 2 days ago. What is the problem with your support system?

```

문장 아래에 다음을 추가합니다.
```
The list of issues is as follows:
```


문장 아래에 다음을 추가합니다.
```
1.
```

### 2. One Shot
#### Structured Mode Example(p20)
##### 첫번째 예제를 입력합니다.   
input
```
The following paragraph is a consumer complaint. Read the following paragraph and list all the issues.
I bought a GPS from your store and the instructions included are in Spanish, not English. I have to use Google Translate to figure it out. The mounting bracket was broken, and so I need information on how to get a replacement. Moreover, the information seems to be outdated because I cannot see the new roads put in around my house within the last 12 months.

```
output
```
The list of issues is as follows:
1) The instructions are in Spanish, not English.
2) The mounting bracket is broken.
3) The information is outdated.

```

프롬프트를 실행합니다.
```
The following paragraph is a consumer complaint. Read the following paragraph and list all the issues. 
I called your help desk multiple times and every time I waited 10-15 minutes before I gave up. When I finally got through like after 3 days (yes, 3 days) your agent kept going over a long checklist of trivial things and asking me to verify, after I repeatedly told the agent that I am an experienced user and I know what I am doing, It was a complete waste of time. After like an eternity of this pointless conversation, I was told that an SME will contact me. That - was 2 days ago. What is the problem with your support system?

```

### 3. Few-Shot Prompt
##### 두번째 예제를 입력합니다.   
input
```
The following paragraph is a consumer complaint. Read the following paragraph and list all the issues. 
I called your help desk multiple times and every time I waited 10-15 minutes before I gave up. This is just ridiculous. When I finally got through like after 3 days (yes, 3 days) your agent kept going over a long checklist of trivial things and asking me to verify, after I repeatedly told the agent that I am an experienced user and I know what I am doing, It was a complete waste of time. After like an eternity of this pointless conversation, I was told that an SME will contact me. That - was 2 days ago. What is the problem with your support system?

```
output
```
The list of issues is as follows:
1) The wait time on the help desk is too long.
2) The agent went over a long checklist of trivial things.
3) The agent did not believe the consumer when they said they were an experienced user.
4) The agent said an SME would contact the consumer, but it has been 2 days and they have not heard back.
5) There is a problem with the support system.

```
프롬프트를 실행합니다.   
```
The following paragraph is a consumer complaint. Read the following paragraph and list all the issues. 
I am writing to express my dissatisfaction regarding my recent purchase from your company. Firstly, the delivery of the product, a vibrant red gaming chair, was significantly delayed, arriving 10 days later than the promised delivery date. This delay caused inconvenience and disrupted my plans. Secondly, upon receiving the product, I was disappointed to find that its quality did not meet my expectations. The chair arrived with several critical components broken, including the armrests and the hydraulic piston, rendering it unusable. As a loyal customer, I expect timely delivery and high-quality products from your company. I kindly request that you address these issues promptly and provide a suitable resolution to restore my confidence in your services.

```
output

##### System Prompt
프롬프트 끝에 추가하여 기본 한글이 출력되게 한다.
```
한국어로 답해 주세요. (한국어)
```

##### Memory in LLM
freeform에서 실행
```
CUSTOMER 테이블의 CUSTOER_ID 와 TRANSACTION 테이블의 CUSTOMER_ID를 조인하는 SQL 쿼리를 만들어줘.
```
위 결과를 삭제후 다시 아래 프롬프트 실행
```
이 쿼리를 사용하여 Netezza DB에 접속해서 실행하는 파이썬 코드 작성해줘.
```

chatmode에서 실행
```
CUSTOMER 테이블의 CUSTOER_ID 와 TRANSACTION 테이블의 CUSTOMER_ID를 조인하는 SQL 쿼리를 만들어줘.
```

```
이 쿼리를 사용하여 Netezza DB에 접속해서 실행하는 파이썬 코드 작성해줘.
```

##### InstructLab
chat mode에서 granite-13b-chat-v2 모델 선택
area 영역에서 내용 확인
```
what is the area of circle with radius 6cm ?
```


# lab3. Notebook Code 
### 마케팅 컨텐츠 반복으로 프롬프트 생성하는 코드(P50)
```python
# df_1 'Instruction' 및 'Content' 열을 포함하는 DataFrame입니다.. 
for index, row in df_1.iterrows():
    prompt_instruct = row['Instruction']
    prompt_input = row['Content']
    prompt_text = f"""{prompt_instruct}

Input: Characteristics: {prompt_input}

Output:"""
    print("Submitting generation request...")
    generated_response = model.generate_text(prompt=prompt_text, guardrails=False)
    print(generated_response)
    
    # 간격에 줄 바꿈 문자 추가. 
    print()

    df_1.at[index, 'Generated_Response'] = generated_response

```
```python
pd.set_option('display.max_colwidth', None)
df_1
```

### 결과를 CSV로 저장하는 코드(P50)
```python
#프로젝트 토큰은 데이터 소스, 연결과 같은 프로젝트 리소스에 액세스하는 데 사용되며 플랫폼 API에서 사용되는 권한 부여 토큰입니다 .
from project_lib import Project

project = Project(None, '<my_project_id>', '<my_project_token>')
pc = project.project_context
```

```python
print('Project Name: {0}'.format(project.get_name()))
print('Project Description: {0}'.format(project.get_description()))
print('Project Bucket Name: {0}'.format(project.get_project_bucket_name()))
print('Project Assets (Connections): {0}'.format(project.get_assets(asset_type='connection')))
```

파일명을 수정하세요.
예:```이름_Generated.csv```
```python
project.save_data(data=df_1.to_csv(index=False), file_name='<my_name>_Generated.csv', overwrite=True)

```


# lab5.Milvus DB를 활용한 RAG
라이브러리 로드
```python
from pymilvus import (
    connections,
    Collection
)
from sentence_transformers import SentenceTransformer
from langchain.docstore.document import Document
from langchain.chains.question_answering import load_qa_chain

from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
```

Milvus 검색 함수 정의하기  
```python
def milvus_search(query, COLLECTION_NAME,embedding_model_name):
    model_name = embedding_model_name
    collection_name = COLLECTION_NAME
    connections.connect("default", host=MILVUS_DB_HOST, port=MILVUS_DB_PORT) 
    collection = Collection(collection_name)
    collection.load()
    search_params = {
        "metric_type": "L2",
        "params": {"ef": 10},
    }
    model = SentenceTransformer(model_name)
    vectors_to_search = model.encode([query]).tolist()

    result = collection.search(vectors_to_search, "vector", search_params,
                                limit=3,
                                output_fields=["text", "vector"],
                                )

    hits = result[0]
    def text2doc(t):
        return Document(page_content = t)

    docs = [text2doc(h.entity.get('text')) for h in hits]
    return docs
```

key 정보 설정
```python
api_key = "<CLOUD_API_KEY>"
# region에 따라 주소가 다를 수 있습니다. 주소를 확인해 주세요.
ibm_cloud_url = "https://us-south.ml.cloud.ibm.com" 
project_id = "<MY_PROJECT_ID>"

if api_key is None or ibm_cloud_url is None or project_id is None:
    raise Exception("One or more environment variables are missing!")
else:
    creds = {
        "url": ibm_cloud_url,
        "apikey": api_key 
    }
```

모델 초기화
```python
# watsonx model 초기화
params = {
#     GenParams.DECODING_METHOD: "sample",
#     GenParams.TEMPERATURE: 0.2,
#     GenParams.TOP_P: 1,
#     GenParams.TOP_K: 100,
    GenParams.DECODING_METHOD: "greedy",
    GenParams.TEMPERATURE:  0.7,
    GenParams.MIN_NEW_TOKENS: 50,
    GenParams.MAX_NEW_TOKENS: 1000
}

model_llm = Model(
    model_id="meta-llama/llama-3-70b-instruct",
    params=params,
    credentials=creds,
    project_id=project_id
).to_langchain()
```

Milvus DB에 질의하기
```python
user_input = "코로나 감염 증상은?"
docs_search = milvus_search(user_input,COLLECTION_NAME,embedding_model_name)
print(docs_search)
```

모델 결과물 생성하기 
```python
chain_types = "stuff"
# chain_types = "map_reduce"
# chain_types = "refine"

chain = load_qa_chain(model_llm, chain_type=chain_types)
response = chain.run(input_documents=docs_search, question=user_input+". 한국어로 답하시오.")
print(response)
```

# prompt template 만들기
## Prompt template 만들기

### 1. model 선택하기
```
llama-4-maverick-17b-128e-instruct-fp8
```

### 2. Instruction 입력
```
주어진 한글문장을 영어로 번역하시오 .
```

### 3. Example 입력

Example 1 text 입력
```
마지막으로, 의회에서 인권 문제를 다루는 방식을 검토할 것을 요구하는 16항을 환영합니다.
```

Example 1 Translation 입력
```
Finally, I welcome paragraph 16 which calls for a review of the way we deal with human rights issues in Parliament.
```

Example 2 text 입력
```
저는 룩셈부르크에서 열린 어느 세션에서 이 주제를 논의했던 걸 잘 기억합니다.
```

Example 2 Translation 입력
```
I remember very well that we discussed it in a session in Luxembourg.
```

### 4. 변수 입력
context 변수 생성후 test your prompt 에 생성한 변수명을 입력 합니다.
```
{context}
```



# AI Service 호출하기

## 1. 토큰생성해서 환경변수에 담기  
API 키 정보를 변경한 후 shell에서 실행합니다.   
* ```<YOUR CLOUD API KEY>``` : IBM Cloud API Key 를 생성하여 사용합니다.
    * IBM Cloud API Key는 IBM Cloud watsonx Console에서 생성할 수 있습니다.
    * IBM Cloud API Key는 Administration > Access (IAM) > API keys에서 생성할 수 있습니다.
    * API Key는 IBM Cloud에서 제공하는 서비스에 대한 인증을 위해 사용됩니다.
    * 예 : 
        ```bash
            apikey=dsgsdagasgas@dXZXZ134t5e5s
        ``` 
```bash
export ACCESS_TOKEN=$(curl -s --insecure -X POST --header "Content-Type: application/x-www-form-urlencoded" --header "Accept: application/json" --data-urlencode "grant_type=urn:ibm:params:oauth:grant-type:apikey"  --data-urlencode "apikey=<YOUR CLOUD API KEY>" "https://iam.cloud.ibm.com/identity/token"  | jq -r '.access_token')

```

## 2. Prompt template 배포한 AI Service 호출하기  
다음의 두개의 정보를 변경합니다.   
* ```<번역할 문장>``` : 번역할 문장입니다. watsonx.ai의 prompt template에서 설정한 변수를 사용합니다.
    * 예 : 
    ```json
        { "context": "IBM은 세계 최고의 AI 엔지니어와 기술을 보유한 AI 전문 기업입니다." }
    ```
* ```<배포된 AI Service URL 주소>``` : 배포한 에인전트 URL 주소. watsonx.ai의 deployment에서 확인할 수 있습니다. Stream URL이 아닌 AI Service URL을 사용합니다.
    * 예 : 
    ```json
    "https://us-south.ml.cloud.ibm.com/ml/v1/deployments/bdb1781c-8744-4b1f-af53-58c0dc53b0dc/text/generation_stream?version=2021-05-01"
    ```

```bash
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer $ACCESS_TOKEN" \
  -d '{ "parameters": { "prompt_variables": { "context": "<번역할 문장>" }, "stop_sequences": ["질문:", "\\n\\n"] } }' \
  "<배포된 AI Service URL 주소>" \
  | jq -r '.results[0].generated_text | split("\n") | .[0]' \
  | (echo "" && cat)
```

## 3. AutoRAG로 배포한 AI Service 호출하기  
다음의 두개의 정보를 변경합니다.   
* ```<질문>``` : 질의할 내용을 입력합니다.
    * 예 : 
    ```json
        {"content":"생성형 AI란?","role":"user"}
    ```
* ```<배포된 AI Service URL 주소>``` : 배포한 에인전트 URL 주소. watsonx.ai의 deployment에서 확인할 수 있습니다. Stream URL이 아닌 AI Service URL을 사용합니다.
    * 예 : 
    ```json
    "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/14c7e962-9bc0-41cd-b845-fa47ba5f0100/ai_service?version=2021-05-01"
    ```

```bash
curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" --header "Authorization: \
 Bearer $ACCESS_TOKEN" -d '{"messages":[{"content":"<질문>","role":"user"}]}' "<배포된 AI Service URL 주소>" \
| jq -r '.choices[0].message.content' \
| xargs -0 echo -e
```


# agent 만들기
맛집을 검색하고 예약하는 agent 플로어.
```scss
Input (user query)
    ↓
PromptTemplate (질의 전처리)
    ↓
LLM (답변 생성)
    ↓
Tools (맛집 검색 / 예약 기능)
    ↓
Output
```



