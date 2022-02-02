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
      # Key 
          cabinet.clear()     # Dictionary 포맷
          print(cabinet)      # Dictionary 포맷되어서 {} 출력.
      ```
  - 튜플 VS 리스트
  
    - |차이점|튜플|리스트|
      |:------:|:---:|:---:|
      |내용|변경 불가|변경 가능|
      |속도|리스트보단 빠름.||
      |영역| 수정하지 않는 영역에 사용함.||
  - 집합(set) : 중복 안되며, 순서는 없다.
      ```python
      # 사용 예제)
          my_set = {1, 2,3, 4, 5, 6, 7, 7, 7} # 중복된, 7은 한번만 출력.
          print(my_set) # 출력 값 ==> {1, 2, 3, 4, 5, 6, 7} 출력.
          ------------------------------------------------------------
          
          java = set(["박기수", "박상철", "조순"])
          python = set(["심원준", "오정민", "박기수", "박상철"])

      # 교집합 (java & python에 속한 사람 출력.)
          
          # 방법 1)
          print(java & python) # {'박상철', '박기수'} 출력.
          # 방법 2)
          print(java.intersection(python)) # {'박상철', '박기수'} 출력.
          ------------------------------------------------------------
          
      # 합집합 (java & python 둘중에 하나 속한 사람 출력.)

          print(java | python) # {'심원준', '조순', '박기수', '박상철', '오정민'} 출력.
          print(java.union(python)) # {'심원준', '조순', '박기수', '박상철', '오정민'} 출력.

      # 집합은 순서가 없기에 위치는 랜덤하게 출력됨.
          ------------------------------------------------------------
          
      # 차집합(java는 할줄알지만 python을 할줄모르는 사람.)

          print(java - python) # {'조순'} 출력.
          print(java.difference(python)) # {'조순'} 출력.
          ------------------------------------------------------------
          
      # 집합 python에 명단 추가(튜플이 아닌, 집함(set)이라 가능.)

          python.add("오경은") # 집합 python에 "오경은" 명단 생성
          print(python) # {'오정민', '오경은', '심원준', '박기수', '박상철'} 출력.
          ------------------------------------------------------------
          
      # 집합 java 명단에 삭제하는 방법.

          java.remove("박기수") # 집합 java안에 속한 "박기수" 명단 제거.
          print(java) # {'박상철', '조순'} 출력.
          ------------------------------------------------------------
       
      ```
  - 자료구조의 변경
    - set(집합)
    - list
    - tuple
    ```python
    # 자료 구조형 1) set 
    menu = {"커피", "우유", "주스"} # 집합은 set형태로 만듬.
    print(menu, type(menu)) # {'커피', '주스', '우유'}로 출력.
                            # <class 'set'>으로 들어감.  

    # 자료 구조형 2) list
    menu = list(menu)
    print(menu, type(menu)) # ['커피', '주스', '우유']로 출력.
                            # <class 'list'>으로 들어감. ==> menu를  set으로 설정해도 menu에 list로 감싸 형 변환.

    # 자료 구조형 3) tuple
    menu = tuple(menu)
    print(menu, type(menu)) # ('커피', '주스', '우유')로 출력.
                            # <class 'list'>으로 들어감. ==> menu를  set으로 설정해도 menu에 tuple로 감싸 형 변환.

    menu = set(menu)
    print(menu, type(menu))
    # 즉, 어떤 타입으로 감싸는지에 따라 출력되는 타입이 다름.
    # set ==> {}
    # list ==> []
    # tuple ==> ()
    ```
  - If문
  - For문
  - While문
  - 함수
    - def
     - 전달값  
     - 반환값 
     - 키워드 값
     - 가변인자 값
     - 기본값
  - 지역변수 및 전역 변수
    - 지역 변수 : 함수 내에서만 사용할 수 있는것.
    ```python
    # 지역변수에서 전역변수 정의 함수 사용 방법 : global
    gun = 10 # 여기에만 gun을 할당하면 def안에 gun이 정의되지 않아 에러
    def checkpoint(soldiers): # 경계 근무
        global gun # 전역공간에 있는 gun을 사용한다.
        gun = gun - soldiers
        print("[함수 내] 남은 총 : {0}".format(gun))

    print("[전체 총] : {0}".format(gun))
    checkpoint(2) # 2명이 총을 들고 병기 근무 투입.
    print("[남은 총] : {0}".format(gun))
    ```
    - 전역 변수 : 모든 공간 즉, 프로그램 내에서 모든 공간에서 부를수 있는 것.    
- Quiz 4)
    ```python
    # 표준 체중을 구하는 프로그램을 작성하시오.

    # * 표준체중 : 각 개인의 키에 적당한 체중

    # (성별에 따른 공식)

    # 남자 : 키(m) X 키(m) X 22
    # 여성 : 키(m) X 키(m) X 21

    # 조건1 : 표준 체중은 별도의 함수 내에서 계산
     #         * 함수명 : std_weight
    #         * 전달값 : 키(height), 성별(gender)
    # 조건2 : 표준 체중은 소수점 둘째자리까지 표시

    # (출력 예제)
    # 키 175cm 남자의 표준 체중은 67.38kg입니다.
    ```
- 내가 한것
    ```python
     weight = 0
     height = float(input("키를 입력하시오 : "))
     gender = str(input("성별을 입력하시오 : "))
     def std_weight(height, gender):
         global weight
         if(gender == "남성"):
             weight = height * height * 22
             return weight
         elif(gender == "여성"):
             weight = height * height * 21
             return weight 
     print("키 {0}의 평균 체중은 {1}.2f 입니다.".format(height, weight))
    ```
- 답안지
    ```python
    # Tip 소수 두번째자리 출력 : round를 사용하면 된다. => round(def한 함수, 2) 
     def std_weight(height, gender):
         if(gender == "남성"):
             return height * height * 22 
         elif(gender == "여성"):
             return height * height * 21
     height = 175
     gender = "남성" 
     weight = round(std_weight(height / 100, gender), 2)
     print("키 {0}cm {1}의 평균 체중은 {2}kg입니다.".format(height, gender, weight))
    ```
- 문제 복습 풀이(최종본)
    ```python
    # Tip 소수 두번째자리 출력 : round를 사용하면 된다. => round(def한 함수, 2) 

    def std_weight(height, gender):
        if(gender == "남성"):
            return height * height * 22
        elif(gender == "여성"):
            return height * height * 21
    height = int(input("키(cm)를 입력하시오 : "))
    gender = str(input("성별을 입력하시오 : "))
    weight = round(std_weight(height/100, gender), 2)
    print("키 {0}cm {1}의 평균 체중은 {2}kg 입니다.".format(height, gender, weight))

    # def을 사용할 때
    # Tip 소수 두번째자리 출력(자동 반올림됨.) : round를 사용하면 된다. => round(def한 함수, 2) 
    ```
  - def에서 소수점 출력하는 법
    - round함수 사용
    ```python
    # Tip 소수 두번째자리 출력 : round를 사용하면 된다. => round(def한 함수, 2) 
    # 문제 복습 풀이(최종본) 코드 부분
    def std_weight(height, gender):
    ...
    weight = round(std_weight(height/100, gender), 2) # 소수 두번째자리 표기(반올림 적용됨.)
    ```
  - 표준 입출력
    - ljust(8) : ljust는 왼쪽으로 정렬. l = left,  8은 총 8칸으로 공간을 확보한 상태에서 왼쪽으로 정렬해달라.
    - rjust(4) : rjust는 왼쪽으로 정렬. r = right, 4은 총 4칸으로 공간을 확보한 상태에서 오른쪽으로 정렬해달라.
    - zfill(3) : zfill은 지정한 크기에 나머지 공간을 0으로 채운다. 즉, 3칸을 만들고 나머지 공백은 0으로 채워라.
    ```python
    # 시험 성적(딕셔너리{사잔})
    ...
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    ```
    ```python
    # 은행 대기순번표
    # ex) 001, 002 식으로
    ...
    for num in range(1, 21, 1):
        print("대기번호 : " + str(num).zfill(3)) 
    ```
  - 파일 입출력
    ```python
    score_file = open("score.txt","w", encoding="utf8") # 'w'는 write(쓰다)라는 목적 utf8을 해줘야 한글이 깨지지 않는다.
    print("수학 : 0", file = score_file)
    print("영어 : 50", file = score_file)
    score_file.close()

    # 파일을 항상 열었으면 닫아야한다.
    ```
  - Pockle : Pockle은 프로그램상에서 우리가 사용하고 있는 데이터를 파일화 해주는 작업
    - 파일화된 것을 다른 사람이 쓸 수 있게 만들수 있다.
    - 작업할때 "wb"식으로 작성한다. 자세한건 아래 코드 참고  
    ```python
    improt pickle
    ...
    profile_file = open("profile.pickle", "wb") # 'w'는 write(쓰기) , 'b'는 binary이다.
    ```
  - with : pickle과 같은 효과를 볼 수 있다 자세한 내용은 아래 코드를 참고.
    ```python
        improt pickle
    ...
    with open("profile.pickle","rb") as profile_file : 
        print(pickle.load(profile_file))
    ```
- 답안지
    ```python
    # Tip 소수 두번째자리 출력 : round를 사용하면 된다. => round(def한 함수, 2) 
     def std_weight(height, gender):
         if(gender == "남성"):
             return height * height * 22 
         elif(gender == "여성"):
             return height * height * 21
     height = 175
     gender = "남성" 
     weight = round(std_weight(height / 100, gender), 2)
     print("키 {0}cm {1}의 평균 체중은 {2}kg입니다.".format(height, gender, weight))
    ```
- 문제 복습 풀이(최종본)
    ```python
    # Tip 소수 두번째자리 출력 : round를 사용하면 된다. => round(def한 함수, 2) 

    def std_weight(height, gender):
        if(gender == "남성"):
            return height * height * 22
        elif(gender == "여성"):
            return height * height * 21
    height = int(input("키(cm)를 입력하시오 : "))
    gender = str(input("성별을 입력하시오 : "))
    weight = round(std_weight(height/100, gender), 2)
    print("키 {0}cm {1}의 평균 체중은 {2}kg 입니다.".format(height, gender, weight))

    # def을 사용할 때
    # Tip 소수 두번째자리 출력(자동 반올림됨.) : round를 사용하면 된다. => round(def한 함수, 2) 
    ```
  
  
- 내가 푼 문제 풀이
    ```python
    for i in range(1, 51, 1) : 
       with open("{0}주차.txt".format(i), "w", encoding="utf8") as task_file :
           task_file.write("- {0}주차 주간보고 -".format(i))
           task_file.write("\n부서 : ")
           task_file.write("\n이름 : ")
           task_file.write("\n업무요약 : ")
        
    with open("{0}주차.txt".format(i), "r", encoding="utf8") as task_file :
        print(task_file.read())
    ```
- 답안지
    ```python
        for i in range(1, 51):
    with open(str(i) + "주차 보고서", "w", encoding="utf8") as task_file:
        task_file.write("- {0}주차 주간보고 -".format(i))
        task_file.write("\n부서 : ")
        task_file.write("\n이름 : ")
        task_file.write("\n업무요약 : ") 
    ```
  - 클래스
    - init : Python에서 사용하는 생성자이다. 
    ```python
        class Unit:
           def __init__(self, name, hp, damage): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
                self.name = name
                self.hp = hp
                self.damage = damage
        marine1 = Unit("마린", 40, 5) # self를 제외하고 name, hp, damage를 정의했으면 동일한 갯수만큼 선언해야한다.
        marine2 = Unit("마린", 40, 5)
        tank1 = Unit("탱크", 150, 35)
        tank2 = Unit("탱크", 150, 35)
    ``` 
    - 객체: 클래스로부터 만들어진 녀석들이다.
    - instance : 클래스로부터 정의된 값들 # 즉 마린과, 탱크가 인스턴스이다.
    - 맴버 변수 : 클래스 내에서 정의된 변수. 위에 코드상에서 self.하는 name, hp, damage가 맴버 변수인 것이다.
    - 메소드 : 클래스 안에서 실행(정의 == def)을 의미한다.
    ```python
        # 공격 유닛(클래스)
        class AttackUnit:
            def __init__(self, name, hp, damage): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
                self.name = name # 여기서 = 다음에 나오는 name은 위에(def __init__(self, name, hp, damage)) 전달받은 인자를 바로 사용하겠다는 뜻이다.
                self.hp = hp
                self.damage = damage
                print("{0} 유닛이 생성 되었습니다.".format(self.name))
                print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))
                
            # (location 메소드)
            def attack(self, location): # 클래스를 사용할때는 self을 항상 사용해줘야한다.
                print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
                # 위에 self.name, self.damage는 상단 def __init__에서 정의된 것들을 사용하는 것이고 location 값은 def attack(self, location)인,
                # location에게 받는다는 뜻이다.
    
            # (damaged 메소드)
            def damaged(self, damage):
                print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
                self.hp -= damage
                print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
                if self.hp <=0 :
                    print("{0}의 체력이 없기에 파괴되었습니다.".format(self.name))
                    ...
          # 정의한 메소드 사용
                    ...
       # 파이어뱃 : 공격 유닛, 화염방사기
       firebat1 = AttackUnit("파벳", 50, 16)
       firebat1.attack("5시") # def attack(self, location)로 지정되고 괄호 안에 (self, location)이지만 self는 항상 안해도 된다. 
                              # 즉, location만 작성해주면 된다.

       # 파이어뱃이 공격 받았을 때, 총 체력은 50인데 0이 되었을 때 문구도 실행되는지 확인 
       firebat1.damaged(25)
       firebat1.damaged(25)
                    
    ``` 
  - coming soon...:octocat: 
- 공부자료
> :tv: [유튜브](https://youtu.be/kWiCuklohdY)

**사용한 언어**

- [x] Python
- [x] VS Code

**git 오류 메세지**
- Git: “Not currently on any branch.” 일때
```git
    git checkout -b newbranch # 새로운 임의의 branch 만든다.(현재 master(main)에 branch가 되지 않았기 때문에 새로 branch를 만들어 merge를 해야한다.)
    git checkout master
    git merge newbranch
    git branch -d newbranch

```
> '참고자료' : https://poorman.tistory.com/409
> 'rebase참고 자료' : https://mizzo-dev.tistory.com/entry/git-commit-edit
