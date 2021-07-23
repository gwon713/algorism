## 큐 (Queue)

##### 먼저 집어 넣은 데이터가 먼저 나오는 선입 선출 FIFO(First In First Out) 형식의 자료구조

![queueimage](https://miro.medium.com/max/1196/1*PMYRFmVecFT61P4aAh0g1g.png)

### 큐(Queue)의 사용 사례

##### 데이터가 입력된 시간 순서대로 처리해야 할 필요가 있는 상황에 이용한다.

- 너비 우선 탐색(BFS, Breadth-First Search) 구현
- 처리해야 할 노드의 리스트를 저장하는 용도로 큐(Queue)를 사용한다.
- 노드를 하나 처리할 때마다 해당 노드와 인접한 노드들을 큐에 다시 저장한다.
- 노드를 접근한 순서대로 처리할 수 있다.
- 캐시(Cache) 구현
- 우선순위가 같은 작업 예약 (인쇄 대기열)
- 선입선출이 필요한 대기열 (티켓 카운터)
- 콜센터 고객 대기시간
- 프린터의 출력 처리
- 윈도 시스템의 메시지 처리기
- 프로세스 관리
  

출처 https://gmlwjd9405.github.io/2018/08/02/data-structure-queue.html