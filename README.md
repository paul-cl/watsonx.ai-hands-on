# watsonx.ai-hands-on
watsonx.ai hands-on lab 자료입니다.

### IBM에서 제공하는 모델 정보
https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models.html?context=wx&audience=wdp

### IBM에서 더이상 제공하지 않는 모델 정보
https://www.ibm.com/docs/en/watsonx-as-a-service?topic=models-foundation-model-lifecycle

### 모델 ID 참조 사이트
https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html


# lab2. Prompt
### 1. Zero Shot
#### Freedom Mode (p15)
prompt
```
The following paragraph is a consumer complaint.
Read the following paragraph and list all the issues. 

I called your helpdesk
multiple times and every time I waited 10-15 minutes before I gave up. The first time I got through, the line got cut suddenly and I had to call back. This is just not helpful. When I finally got through like after 3 days (yes, 3 days) your agent kept going over a long checklist of trivial things and asking me to verify, after I repeatedly told the agent that I am an experienced user and I know what I am doing. It was a complete waste of time. After like an eternity of this pointless conversation, I was told that an SME will contact me. That – was 2 days ago. What is the problem with your support system?

The list of issues is as follows:

```

### 2. One Shot
#### Structured Mode Example(p20)
예제를 입력합니다.   
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
예제를 입력합니다.   
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

# lab2. Notebook Code 
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
project.save_data(data=df_1.to_csv(index=False), file_name='<my_name>_Generated.csv', overwrite=True
```
