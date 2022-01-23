# PythonProjects 기본 개념 공부하기

```python
printf("파이썬 기초 공부하기");
```

- 파이썬의 기본 개념
  - 파이썬 문법
  - 파이썬 변수
  - 파이썬 연산자
    - (+)  : 덧셈
    - (-)  : 뺄셈
    - (*)  : 곱셉
    - (/)  : 나눗셈(float까지)
    - (//) : 몫(int)
    - (%)  : 나머지(int)
  - 파이썬 랜덤함수
    -변수.random 
  - 파이썬 슬라이싱
    - print("주민번호" + 변수[7])   # (공백 포함) index[7]의 위치 출력.
    - print("주민번호" + 변수[0:4]) # (공백 포함) index[0]부터 index[4]직전까지 출력. 즉 index[0~3] 출력.
  - 파이썬 문자열 처리함수
    - 공부하기 싫어요..! :cold_sweat:
  - 문자열 포맷
  - 탈출 문자
    - 퀴즈로 이전 학습 내용 복습 
  - 리스트
    - 리스트 정의 
    - append  : 리스트 마지막에 추가
    - insert  : 원하는 인덱스 위치에 추가 ==> insert(해당 index위치 , 입력하고자 하는 단어) == insert(2, "피지크")   
    - pop     : 리스트 마지막(리스트중에 최근 리스트) 삭제
    - count   : 해당하는 단어 리스트 확인
  - 리스트 정렬
    - sort    : 오름차순으로 정렬
    - reverse : 순서 뒤집기 ==> [2, 3, 5, 6, 7] ==> [7, 6, 5, 3, 2]
    - clear   : 리스트 내용 모두 제거
    - extend  : 리스트 병합
      - **list 사용 주의**
      ```python
      # 사용 예시)
          num_list = [5, 2, 4, 3, 1]
          num_list.clear()
          print(num_list)          # 1) 출력물은 [] 으로 정상적으로 나옴.
          -----------------------------
          print(num_list.clear())  # 2) 출력물은 None 으로 비정상적으로 나옴.
          # 차이가 있으니 알아둘 것.
          # 다른 리스트 명령도 1)과 같은 방식으로 정의해야함.
      ```     
  - 사전
    - 변수.get()
    - 변수[]
      - **차이점**
      ```python
      # 사용 예제)
          dictionary = [9 : "토레스", 8 : "제라드", 10 : "메시", 7 : "호날두"]
          
          # If) 에러 발생시
          
          print(dictionary[999])        # 에러 발생 
          print("Hello World")          # 출력 안됌         
          -----------------------------
          print(dictionary.get(999))    # 에러 대신 None 출력. 
          print("Hello World")          # 출력 됌.

          # 차이가 있으니 알아둘 것.
      ```  
    - 값 확인하는 방법
      - key in 변수 ==> 있다면 True 출력.
      - key in 변수 ==> 없다면 Flase 출력.   
    - Key 삽입 및 업데이트
      ```python
          cabinet = {"A-3" : "클래식 피지크", "A-4" : "보디빌딩"}   # {Key : Value}

          # 새로운 Key 삽입
          print(cabinet)
          cabinet["C-7"] = "로이더!"    # C-7이 없는 Key 값이라면 "로이더!"가 저장되며,
                                       # 만약 C-7이 사용중이면 "로이더!"로 새로 업데이트가 된다.
          print(cabinet)
          print(cabinet.get("C-7"))   
      ```  
     - del : Key 삭제
      ```python
          cabinet = {"A-3" : "클래식 피지크", "A-4" : "보디빌딩"}   # {Key : Value}
         
          # Key 삭제
          print(cabinet)
          del cabinet["A-4"]  # "A-4" Key 삭제.
          print(cabinet)
      ```  
    - key들 확인 방법
      ```python
          print(cabinet.keys()) # dict_keys(['A-3', 'C-7'])로 출력.  
      ```      
    - Value들 확인 방법
      ```python
          print(cabinet.values()) # dict_values(['클래식 피지크', '로이더!'])로 출력.  
      ``` 
    - key, Value 쌍으로 확인 방법
      ```python
          print(cabinet.items()) # dict_items([('A-3', '클래식 피지크'), ('C-7', '로이더!')]) 
      ```       
    - Dictionary 포맷.
      ```python
          cabinet.clear()     # Dictionary 포맷
          print(cabinet)      # Dictionary 포맷되어서 {} 출력.
      ```
    - coming soon...:octocat: 
- 공부자료
> '유튜브 나도코딩'

:tv: [유튜브](https://youtu.be/kWiCuklohdY)

**사용한 언어**

- [x] Python
- [x] VS Code
