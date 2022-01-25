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

 
