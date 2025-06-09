
f"""아래 보고서를 읽고 다음 지침에 따라 분석을 수행하세요.

1. 먼저 문서의 핵심 내용을 반영하는 **중요 키워드 5~10개**를 추출하세요. 키워드는 명사형으로, 문서 내 주요 주제, 기술, 사건, 정책 등을 포함해야 합니다.
2. 추출한 키워드를 바탕으로 **300자 이내 요약문**을 작성하세요. 요약은 키워드를 모두 포함하며, 단락 전체가 하나의 명확한 문장으로 연결되어야 합니다.
3. 요약문은 한국어로 자연스럽고 간결하게 작성하며, 단정적 어투로 마무리합니다.
4. 숫자, 연도, 기관명 등은 가능한 정확히 유지하세요.

형식은 다음과 같습니다:

[키워드]: 키워드1, 키워드2, 키워드3, ...

[요약]: 요약문

예시 입력:
"2024년 IBM은 watsonx.ai 플랫폼을 통해 AutoRAG 기능을 출시했다. 이 기능은 RAG 기반 질문응답 성능을 크게 향상시키며 기업의 데이터 기반 의사결정을 지원한다."

예시 출력:
[키워드]: IBM, watsonx.ai, AutoRAG, RAG, 질문응답, 데이터 기반 의사결정  
[요약]: IBM은 watsonx.ai의 AutoRAG 기능을 통해 RAG 기반 질문응답의 정확도를 높이고 데이터 기반 의사결정을 효율적으로 지원하고 있다.

이제 아래 문서를 분석하세요:
{document}
"""

response = send_to_watsonxai(prompts=[prompt], model_name=LLAMA_3_70B_CHAT,  decoding_method="greedy", max_new_tokens=100,
                              min_new_tokens=1, temperature=0, repetition_penalty=1.0)


def make_summary(contents: str, time: str) -> str:

    # 실제 API 연동 부분은 생략하고, 예시로 반환합니다.
    result = call_api_to_make_summary(contents, time)
    if not result:
        return "요약에 실패했습니다. 다시 시도해 주세요."
    # 예약 성공 시 메시지 반환
    # 예시로 예약 성공 메시지 반환
  
    return f"{contents}"