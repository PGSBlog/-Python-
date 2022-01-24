# 자료구조의 변경
# 커피숍

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