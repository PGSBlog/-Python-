# sep 사용 # 문장 사이

import imp


print("Python", "Java", sep = ",")  # sep는/은 Python과 Java 사이의 공백을 어떻게 구분할지 지정.
print("Python", "Java", sep = "VS") # 사이에 VS 넣기
print("Python", "Java", sep = " VS ") # 사이에 (공백)VS(공백) 넣기 

# end 사용 # 문장 끝

print("Python", "Java", sep = ",", end ="?") # end는/은 문장끝에 기입.
print("무엇이 더 재미있을까?")

import sys
print("Python", "Java", file = sys.stdout) # 표준 출력로 출력. 
print("Python", "Java", file = sys.stderr) # 표준 에러로 출력.

# 시험 성적(딕셔너리{사잔})
scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items(): # key, valiue가 쌍으로 출력. kry = subject인 "수학", value = score인 "0"값들이 쌍으로 튜플로 보내준다.0 
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    # ljust는 왼쪽으로 정렬. l = left,  8은 총 8칸으로 공간을 확보한 상태에서 왼쪽으로 정렬해달라.
    # rjust는 왼쪽으로 정렬. r = right, 4은 총 4칸으로 공간을 확보한 상태에서 오른쪽으로 정렬해달라.
    '''
    # 출력물
    수학      :   0
    영어      :  50
    코딩      : 100
        8칸   :  4칸
    '''

# 은행 대기순번표
# ex) 001, 002 식으로...
for num in range(1, 21, 1):
    print("대기번호 : " + str(num).zfill(3)) # zfill은 지정한 크기에 나머지 공간을 0으로 채운다. 즉, 3칸을 만들고 나머지 공백은 0으로 채워라.
    
answer = input("아무것이나 입력하시오! : ") # 기본적으로 input은 str이다.   
print(type(answer)) 
print("입력하신 값은" + answer + "입니다.")
