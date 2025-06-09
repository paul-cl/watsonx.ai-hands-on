from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END
from langchain_core.runnables import Runnable

# 에이전트 상태 구조 정의
class AgentState(TypedDict):
    query: str
    recommended: Optional[List[str]]
    selected: Optional[str]
    reservation_status: Optional[str]

# 사용자 입력을 분석해서 맛집 추천하는 Node
def recommend_restaurants(state: AgentState) -> AgentState:
    query = state['query']
    # 여기서 실제로는 검색 시스템 또는 LLM을 연결
    recommendations = call_api_to_search_restaurants(location, cuisine)

    return {**state, "recommended": recommendations}

# 사용자에게 추천된 맛집을 보여주는 Node : 작업
def choose_restaurant(state: AgentState) -> AgentState:
    # 실제로는 유저의 선택을 받는 인터페이스와 연결되어야 함
    selected = state['recommended'][0]  # 예시로 첫 번째 선택
    return {**state, "selected": selected}

# 예약을 진행하는 Node : 작업
def make_reservation(state: AgentState) -> AgentState:
    # 실제 예약 API와 연동할 수 있음
    result = call_api_to_make_reservation(restaurant_name, time)
    if not result:
        return "예약에 실패했습니다. 다시 시도해 주세요."
    
    status = f"{state['selected']} 예약 완료!"
    return {**state, "reservation_status": status}

# langgraph를 사용 : 노드 등록
graph = StateGraph(AgentState)
graph.add_node("recommend", recommend_restaurants)
graph.add_node("choose", choose_restaurant)
graph.add_node("reserve", make_reservation)

# 각 노드의 상태를 정의 : 노드 연결
graph.set_entry_point("recommend")
graph.add_edge("recommend", "choose")
graph.add_edge("choose", "reserve")
graph.add_edge("reserve", END)

app = graph.compile()

# 에이전트 실행
result = app.invoke({"query": "강남 근처에서 소고기 맛집 찾아줘"})
print(result)

