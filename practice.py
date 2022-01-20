# 그냥 예제
'''
station = input("지하철 역을 입력하시오 : ")
print("%s 행 열차가 들어오고 있습니다." %station)
'''

# if문 예제
'''
주민번호 = int(input("주민번호 뒷자리 한자리 숫자만 입력하시요 ex) 1xxxxxx : "))

if (주민번호==1) :
    print("당신은 남성입니다.")
elif(주민번호==0) :
    print("당신은 여성입니다.")    
'''

# 문자열처리함수 종류

python = "Python is Good"
print(python.lower())                   # 'lower' 는/은 대문자를 포함한 모든 단어는 소문자로 변경 후 출력.
print(python.upper())                   # 'upper' 는/은 소문자를 포함한 모든 단어는 대문자로 변경 후 출력.
print(python[0].isupper())              # 'isupper' 는/은 []안에 위치한 문자가 대문자인지 Ture / False로 출력.
print(len(python))                      # 'len' 는/은()안에 들어있는 문자열 index를 int형으로 출력. (빈칸도 포함)
print(python.replace("Python", "Java")) # 'replace' 는/은 ()안 "Python" 문자를 "Java"로 변경 후 출력.

index = python.index("o")               # 'index' 는/은 "o"라는 글자의 index 위치를 찾은 후 출력.
print(index)

index = python.index("o", index + 1)    # 'index + 1' 는/은 처음에 찾았던 'o'단어 다음에(두번 째)  'o'의 위치를 찾은 후 출력. 
print(index)

print(python.find("n"))                 # 'find' 는/은 "n"라는 글자의 index 위치를 찾은 후 출력.
print(python.find("Java"))              # 단, 정의한 index에서 찾고자 하는 문자가 없을 경우 -1 출력.
print(python.index("Java"))             # index는 없는 단어를 찾고자 할 때 에러가 출력 된다.

# find 와 index 차이 find는 오류(찾는 단어가 없을 때) 출력이 아닌, -1을 출력해 다음에 있는 명령어를 실행.
# index는 오류(찾는 단어가 없을 때)가 발생하면 에러 출력. 즉, 다음에 있는 명령어 실행 불가.
print("hi")
print("과연 이 명령어가 실행이 될까?")

print(python.count("n"))                # 'count' 는/은 해당하는 'n'이 몇개 들어가 있는지 갯수를 샌다.