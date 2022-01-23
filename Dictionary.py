# 사전

# if) key == int형

cabinet = {3 : "클래식 피지크", 4 : "보디빌딩"}     # {Key : Value}

# 사전 값 가져오는 방법 1) [] 을/를 이용한 출력.

print(cabinet[3])                                  # key값이 3인 "클래식 피지크" 출력.
print(cabinet[4])                                  # key값이 4인 "보디빌딩" 출력.

# 사전 값 가져오는 방법 1) get.() 을/를 이용한 출력.

print(cabinet.get(3))                              # key값이 3인 "클래식 피지크" 출력.

# 방법1) '[]' 와 방법 2) 'get.()'의 차이점

# 1. 방법 1)이 에러가 발생할 때, 방법 1) 다음에 존재하는 명령어는 실행 안됨. 즉, 방법 1)다음에 뭐가 있는지 모름.
# 2. 방법 2)가 에러가 발생할 때, 방법 2) 다음에 존재하는 명령어는 실행되며 방법 2)는 에러 대신 'None'이 출력. 

# 방법1) 방법2) 비교
# print(cabinet[999])                               # 에러 발생.
print(cabinet.get(999))                             # None 출력.

# 방법 2) 사용 예시

print(cabinet.get(999))
print(cabinet.get(999, "사용가능"))

# 값이 있는지 확인하는 방법

print(3 in cabinet)                                 # True 출력.
print(9 in cabinet)                                 # Flase 출력.

# if) key == str형

cabinet = {"A-3" : "클래식 피지크", "A-4" : "보디빌딩"}     # {Key : Value}
print(cabinet["A-3"])                                      # "클래식 피지크" 출력. 
print(cabinet.get("A-4"))                                  # "보디빌딩" 출력.

# 새로운 Key 삽입
print(cabinet)
cabinet["C-7"] = "로이더!"   # C-7이 없는 Key 값이라면 "로이더!"가 저장되며,
                            # 만약 C-7이 사용중이면 "로이더!"로 새로 업데이트가 된다.
print(cabinet)
print(cabinet.get("C-7"))

# Key 삭제
print(cabinet)
del cabinet["A-4"]  # cabinet 안에 들어있는 Key 삭제. 
print(cabinet)

# Key 들만 출력

print(cabinet.keys())   # dict_keys(['A-3', 'C-7'])로 출력.

# Value 들만 출력

print(cabinet.values()) # dict_values(['클래식 피지크', '로이더!'])로 출력.

# Key, Value 쌍으로 출력

print(cabinet.items())  # dict_items([('A-3', '클래식 피지크'), ('C-7', '로이더!')])

# Dictionary 포맷.

cabinet.clear()     # 포맷되어서 {} 출력.
print(cabinet)
