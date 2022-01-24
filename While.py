# While 문
'''
custmoer = "박기수"
index = 5

while index >= 1 :
    print("{0}님, 커피가 준비 되었습니다. 다음 대기자는 {1}명이 있습니다.".format(custmoer, index)) # custmoer는 {0}, index는 {1}
    index -= 1
    if index == 0 :
        print("모든 손님에게 커피를 제공해 드렸습니다.")
'''

# While문 무한루프
'''
custmoer = "박기수"
index = 5

while True >= 1 : # 이러면 무한 루프 강제 종료는 Ctrl + C를 누르자.
    index += 1
    print("{0}님, 커피가 준비 되었습니다. 다음 대기자는 {1}명이 있습니다.".format(custmoer, index)) # custmoer는 {0}, index는 {1}
'''
# While문 break
'''
custmoer = "박기수"
person = "UnKnown"

while person != custmoer :
    print("{0}님, 커피가 준비 되었습니다.".format(custmoer))
    person = input("성함이 어떻게 되세요? : ")
    print("%s님! 아직 주문하신 커피가 없습니다." %person)
    break
'''

# While문 break와 continue
'''
absent = [2, 5] # 결석 번호
no_book = [4]
for student in range(1, 6, 1) :
    if student in absent :  
        continue
    # print("{0}, 나와서 발표해!".format(student))
    elif student in no_book : # 여기선 else를 사용할 수 없다.
        print("{0}번, 책 없어? 교무실로 따라오렴.".format(student))
        break
    print("{0}번, 책읽어보렴.".format(student))
print("오늘은? 여기까지")
'''

# 효율적인 for문 
'''
student = [1,2,3,4,5,6,7]
print(student)
student = [ i + 100 for i in student] # i 값에 100을 더하는데 i는 student에 있는 리스트 값들을 가져와 더한다는 의미이다.
print(student)
'''

# 학생들 이름을 길이로 변환
'''
student = ["qkrrltn", "qkrtkdcjf", "dhwjdals"] # "박기수", "박상철", "오정민"
# student = [len(student)]          # 이러면 student안에 있는 리스트 갯수를 출력
student = [len(i) for i in student] # 이렇게 해야 리스트 안에 있는 단어 각각의 길이를 출력할 수 있다.
print(student)
'''

# 학생 이름을 대문자로 변환
'''
student = ["qkrrltn", "qkrtkdcjf", "dhwjdals"] # "박기수", "박상철", "오정민"
student = [i.upper() for i in student] # upper다음 ()꼭 넣기 넣지 않으면 16진수로 출력됌.
print(student)
'''
