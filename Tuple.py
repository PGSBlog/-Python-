# 튜플은 리스트와 다르게 내용 변경과 추가를 할수 없다.
# 하지만 속도는 리스트보다 빠르다. 튜플은 추가/ 수정하지 않는 곳에서 사용함.

menu = "닭가슴살", "소고기"
print(menu[0])
print(menu[1])

# menu.add("피자")    # 'tuple' object has no attribute 'add' 라는 에러 메세지 출력.

# 집합(set)
# 중복 안됨, 순서 없음.

my_set = {1, 2,3, 4, 5, 6, 7, 7, 7} # 중복된, 7은 한번만 출력.
print(my_set) # 출력 값 ==> {1, 2, 3, 4, 5, 6, 7} 출력.

java = set(["박기수", "박상철", "조순"])
python = set(["심원준", "오정민", "박기수", "박상철"])

# 교집합 (java & python에 속한 사람 출력.) 
print(java & python) # {'박상철', '박기수'} 출력.
print(java.intersection(python)) # {'박상철', '박기수'} 출력.

# 합집합 (java & python 둘중에 하나 속한 사람 출력.)

print(java | python) # {'심원준', '조순', '박기수', '박상철', '오정민'} 출력.
print(java.union(python)) # {'심원준', '조순', '박기수', '박상철', '오정민'} 출력.

# 집합은 순서가 없기에 위치는 랜덤하게 출력됨.

# 차집합(java는 할줄알지만 python을 할줄모르는 사람.)

print(java - python) # {'조순'} 출력.
print(java.difference(python)) # {'조순'} 출력.

# 집합 python에 명단 추가(튜플이 아닌, 집함(set)이라 가능.)

python.add("오경은") # 집합 python에 "오경은" 명단 생성
print(python) # {'오정민', '오경은', '심원준', '박기수', '박상철'} 출력.

# 집합 java 명단에 삭제하는 방법.

java.remove("박기수") # 집합 java안에 속한 "박기수" 명단 제거.
print(java) # {'박상철', '조순'} 출력.