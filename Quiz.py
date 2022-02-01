# ------------------------------------------------------------------------------------------------------------------------------------

# 퀴즈 1)

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com ==> replace로 처리
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver ==> index로 처리
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성

#규칙 1) 

# url = "http://naver.com"
# my_str = url.replace("http://", "")     # "http://"를 ""(공백)으로 변경 후 출력.
# print(my_str)

# #규칙 2)
# my_str = my_str[:my_str.index(".")]     # "."이전까지의 index를 출력. 즉, [0:5]까지 출력된다.
# print(my_str)

# #규칙 3)

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # :3에서 index [0 ~ 2]의 배열을 출력.
# print("{}의 비밀번호는 {}입니다.".format(url, password))

# ------------------------------------------------------------------------------------------------------------------------------------

# 퀴즈 2)

# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추천프로그램을 작성 하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20명 이라고 가정.
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가.
# 조건3 : random 모듈의 shuffle 과 sameple 을 활용.

# (출력 예제)
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --축하합니다.--

# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# from random import *
# client = range(1, 21, 1)
# print(type(client))
# client = list(client)
# print(client, type(client))
# shuffle(client)


# winner = sample(client, 4) # tip if문을 사용하지 않고도 4명을 뽑고 4명을 format을 사용해 리스트로 나누어 출력하는것이 더 쉽다. 

# print("--당첨자 발표--")
# print("치킨 당첨자 : {}".format(winner[0])) # practice.py 참고
# print("커피 당첨자 : {}".format(winner[1:4])) # index 1-3까지 출력
# print("--축하합니다.--")

# ------------------------------------------------------------------------------------------------------------------------------------

# 퀴즈 3)

# 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다. 
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력물 예제)

# [O] 1번째 손님 (소요시간 : 15분) # [O] : 탑승자
# [ ] 2번째 손님 (소요시간 : 50분) # [ ] : 미 탑승자
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분 

# 알아야하는 조건 Tip

# 1. 난수라는 조건이 있으므로 form random 사용 ==> 이게 중요!
# 2. 증가하는 범위(range)함수를 사용해 탑승객을 표현
# 3. 랜덤 범위(randrange)함수를 사용해 랜덤 시간 표현
# 4. 탑승객을 표기하기 위해 탑승객 함수 정의
# 5. format 사용

# from random import *

# cnt = 0 # 총 탑승객

# for i in range(1, 51, 1) : # 1 - 50명 승객
#     time = randrange(5, 51) # 5 - 50분 사이의 소요시간
#     if (5 <= time <= 15) : # 매칭 성공
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 실수 : 나는 {0}를 가르키는 것이 'cnt'인줄 알고 선언했는데 'cnt'가 아닌, 'i'이다. ==> 당연이 for 'i' in range이니까 'i'이다.
#         cnt += 1 # 조건에 총 탑승객도 표기해야해서 매칭이 성공한 사례를 가지고 cnt에 1을 더한다.
#     else : # 매칭 실패
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 이때는 매칭이 실패한 경우라서 cnt에 1을 더하지 않는다.
# print("# 총 탑승 승객 : {0}분".format(cnt))

# ------------------------------------------------------------------------------------------------------------------------------------

# Quiz 4) 표준 체중을 구하는 프로그램을 작성하시오.

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
# # 내가 한것 

# weight = 0
# height = float(input("키를 입력하시오 : "))
# gender = str(input("성별을 입력하시오 : "))
# def std_weight(height, gender):
#     global weight
#     if(gender == "남성"):
#         weight = height * height * 22
#         return weight
#     elif(gender == "여성"):
#         weight = height * height * 21
#         return weight 
# print("키 {0}의 평균 체중은 {1}.2f 입니다.".format(height, weight))

# 답안지 
# Tip 소수 두번째자리 출력 : round를 사용하면 된다. => round(def한 함수, 2) 
# def std_weight(height, gender):
#     if(gender == "남성"):
#         return height * height * 22 
#     elif(gender == "여성"):
#         return height * height * 21
# height = 175
# gender = "남성" 
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 평균 체중은 {2}kg입니다.".format(height, gender, weight))

# 문제 복습 풀이 
# Tip 소수 두번째자리 출력 : round를 사용하면 된다. => round(def한 함수, 2) 

# def std_weight(height, gender):
#     if(gender == "남성"):
#         return height * height * 22
#     elif(gender == "여성"):
#         return height * height * 21
# height = int(input("키(cm)를 입력하시오 : "))
# gender = str(input("성별을 입력하시오 : "))
# weight = round(std_weight(height/100, gender), 2)
# print("키 {0}cm {1}의 평균 체중은 {2}kg 입니다.".format(height, gender, weight))

# def을 사용할 때
# Tip 소수 두번째자리 출력(자동 반올림됨.) : round를 사용하면 된다. => round(def한 함수, 2) 

# ------------------------------------------------------------------------------------------------------------------------------------

# 퀴즈 5) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# -x 주차 주간보고-
# 부서 : 
# 이름 : 
# 업무요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt' , '2주차.txt', ...와 같이 만듭니다.
# hint : 1 ~ 50주차는 for i in range(1, 51, 1) : 쓰면 됌.

# 내가 푼 문제 풀이
for i in range(1, 51, 1) : 
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as task_file :
        task_file.write("- {0}주차 주간보고 -".format(i))
        task_file.write("\n부서 : ")
        task_file.write("\n이름 : ")
        task_file.write("\n업무요약 : ")
        
with open("{0}주차.txt".format(i), "r", encoding="utf8") as task_file :
    print(task_file.read())

# 답안지 

for i in range(1, 51):
    with open(str(i) + "주차 보고서", "w", encoding="utf8") as task_file:
        task_file.write("- {0}주차 주간보고 -".format(i))
        task_file.write("\n부서 : ")
        task_file.write("\n이름 : ")
        task_file.write("\n업무요약 : ") 

    
