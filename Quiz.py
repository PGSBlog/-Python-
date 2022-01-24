# ------------------------------------------------------------------------------------------------------------------------------------

# 퀴즈

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com ==> replace로 처리
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver ==> index로 처리
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성

#규칙 1) 
'''
url = "http://naver.com"
my_str = url.replace("http://", "")     # "http://"를 ""(공백)으로 변경 후 출력.
print(my_str)

#규칙 2)
my_str = my_str[:my_str.index(".")]     # "."이전까지의 index를 출력. 즉, [0:5]까지 출력된다.
print(my_str)

#규칙 3)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # :3에서 index [0 ~ 2]의 배열을 출력.
print("{}의 비밀번호는 {}입니다.".format(url, password))
'''
# ------------------------------------------------------------------------------------------------------------------------------------

#퀴즈

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

from random import *
client = range(1, 21, 1)
print(type(client))
client = list(client)
print(client, type(client))
shuffle(client)


winner = sample(client, 4) # tip if문을 사용하지 않고도 4명을 뽑고 4명을 format을 사용해 리스트로 나누어 출력하는것이 더 쉽다. 

print("--당첨자 발표--")
print("치킨 당첨자 : {}".format(winner[0])) # practice.py 참고
print("커피 당첨자 : {}".format(winner[1:4])) # index 1-3까지 출력
print("--축하합니다.--")
