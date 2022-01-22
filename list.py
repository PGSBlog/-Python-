# 리스트[]

#지하철 칸별로 10명, 20명, 30명 etc...
'''
subway1 = 10
subway2 = 20
subway3 = 30

subwaylist = [10, 20, 30]   # 10는/은 index [0]에, 20은 index [1]에, 30은 index [2]에 위치함.
print(subwaylist)
'''
# 212보디빌딩은 몇번 째 순서 인가?               # Tip 인덱스 + 1을 해줘야한다.
'''  
subwaylist2 = ["스포츠모델", "피지크", "클래식 피지크", "212보디빌딩"]
print(subwaylist2)                              #list형태인 subwaylist2를 출력함.

print(subwaylist2.index("212보디빌딩") + 1 )    #index는 해당 변수 값안에 찾고자 하는 단어의 index 위치를 출력. [0 ~ 4] 중에 [3]에 위치함.


# 다음 종목에서 "오픈 보디빌딩"을 추가하시오.     #Tip append를 사용해 리스트 뒤에 추가할 수 있다.

subwaylist2.append("오픈 보디빌딩")             # 해당 리스트 변수명 뒤에 append를 사용하면 해당 리스트 맨 마지막에 stack처럼 추가됌.
print(subwaylist2)

#다음 "피지크"와 "클래식 피지크" 종목 사이에 "오른쪽부턴 하체도 심사"를 추가하시오. # Tip insert를 사용해 리스트 사이에 추가할 수 있다.
subwaylist2.insert(2, str("오른쪽부턴 하체도 심사")) # 피지크가 index[1]이고 클래식 피지크가 index[2]이기에 클래식 피지크를 밀어내고
print(subwaylist2)                                  # index[2]자리에 "오른쪽부턴 하체도 심사"를 추가한다.

subwaylist2.pop()                                   #pop는/은 지정된 삭제 리스트가 없을시 뒤(가장 최근)에서부터 리스트를 삭제후 출력.
print(subwaylist2)

# 같은 종목이 있는지 확인                       #Tip count를 사용해 몇번 확인되는지 찾을 수 있다.
subwaylist2.append("클래식 피지크")
print(subwaylist2.count("클래식 피지크"))
'''

# 리스트 정렬하기

num_list = [5, 2, 4, 3, 1]
num_list.sort()             # 'sort'는/은 오름차순으로 정렬 후 출력.
print(num_list)

# 순서 뒤집기

num_list.reverse()          #'reverse'는/은 리스트를 뒤집은 후 출력.
print(num_list)

# 모두 지우기
num_list.clear()            # 1) 'clear'는/은 리스트 내용을 삭제 후 출력. ==> 결과값 []
print(num_list)

print(num_list.clear())     # 2) 결과값 None

# 2)으로 할 경우 '알 수 없음'으로 정의되어 진다. 즉, 1) 처럼 먼저 정의하고 그 다음을 출력해야 올바르게 실행이 된다.

# 다양한 자료형과 함께 사용 가능하다.
mix_list = ["클래식 피지크", 2022, True]  # []안에 str, int, boolean 같이 사용 가능하다.

# 리스트 확장
mix_list = ["클래식 피지크", 2022, True]  # []안에 str, int, boolean 같이 사용 가능하다.
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)


