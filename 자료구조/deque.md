## 덱(Deque)

##### 먼저 집어 넣은 데이터가 먼저 나오는 선입 선출 FIFO(First In First Out) 형식의 자료구조인 큐의 동작이 양방향에서 가능한 자료구조

![deque_image](https://t1.daumcdn.net/cfile/tistory/99DEB94D5C47326713)

##### - 앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.

##### - 덱(Deque)는 양 끝 엘리먼트(element)의 append와 pop이 압도적으로 빠르다

##### - 컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우

##### 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 덱(deque)는 O(1)로 접근 가능하다.

