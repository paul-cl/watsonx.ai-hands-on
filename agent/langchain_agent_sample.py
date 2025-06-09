from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.prompts import PromptTemplate
from langchain.tools import tool
from langchain_ibm import WatsonxLLM

# LangChain LLM 설정 (OpenAI 또는 IBM watsonx.ai 연동 가능)
llm = WatsonxLLM(temperature=0.7, model_name="meta-llama/llama-3-3-70b-instruct")

# 맛집 검색 기능 정의
@tool
def search_restaurants(location: str, cuisine: str) -> str:
    """
    주어진 지역과 음식 종류를 기반으로 맛집을 검색합니다.
    예: location='강남', cuisine='이탈리안'
    """
    # 실제 API 연동 부분은 생략하고, 예시로 반환합니다.
    result = call_api_to_search_restaurants(location, cuisine)
    
    return f"{location}에 있는 인기 있는 {cuisine} 맛집 3곳: ...{result}"

# 예약 기능 정의
@tool
def make_reservation(restaurant_name: str, time: str) -> str:
    """
    특정 맛집에 대해 시간 정보를 기반으로 예약합니다.
    """
    # 실제 API 연동 부분은 생략하고, 예시로 반환합니다.
    result = call_api_to_make_reservation(restaurant_name, time)
    if not result:
        return "예약에 실패했습니다. 다시 시도해 주세요."
    # 예약 성공 시 메시지 반환
    # 예시로 예약 성공 메시지 반환
  
    return f"{restaurant_name}에 {time} 시 예약 완료되었습니다."

# Tools 목록
tools = [search_restaurants, make_reservation]

# Agent 생성
agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# 사용자 쿼리 테스트
query = "강남에서 저녁에 먹을 수 있는 이탈리안 식당 알려줘 예약해줘."
response = agent_executor.run(query)
print(" 응답:", response)
