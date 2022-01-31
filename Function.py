
# 함수 정의

def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

# 전달갑 반환값

def f(x) : 
    result = x**2 + 5*x +3
    return result # return은 선언하면 print역할을 하기에 이 안헤 print를 선언하면 무한 루프
                  # 즉, return을 사용해 result를 실행 시키는 것이다.

def main() :
    for a in range(10, 21, 2) : 
            y = f(a) # 상단의 f(x) 정의한 함수에서 x위치대신 a가 들어가서 계산 진행됌.
            print("%d의 값은 %d입니다." % (a,y))
main()

# 전달값 반환값 # 입금 실행 순서[ ]



def open_account():
    print("새로운 계좌가 생성되었습니다.") # 입금 실행 순서 [3] : balance에 money인 1000원을 입급한다.

def deposit(balance, money): # 입금 함수 : balance, 입금하려는 금액 : money
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money)) # format에 잔액 + 입금 = 총 입금 금액 표시
    return (balance + money)  

def withdraw(balance, money): # 출금 함수
    if balance >= money : # 출금이 잔액보다 많으면... # 출금 실행 순서 [2]
        print("출금이 완료되었습니다. 잔액음 {0}원 입니다.".format(balance - money)) # format에 잔액 - 출금 = 총 잔액 금액 표시
        return (balance - money)
    else :
        print("출금할 수 없습니다. 현재 금액 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 출금할때 붙는 수수료
    commission = 100 # 수수료 잔액
    return commission, balance - money - commission # commission + money

# def commisson_night(commisson, money):
#     count = commission + money
#     return count

# 입금 실행 순서 [1]
balance = 0 # 초기 잔액
# 입금 실행 순서 [2]
balance = deposit(balance, 10000)
# 입금 실행 순서 [4]
print(balance)

# 출금 실행 순서 [1]
balance = withdraw(balance, 500)

# 수수료를 포함한 출금 실행
commission, balance = withdraw_night(balance, 500) # balance, money
# count = commission_night(count,500)
print("저녁에는 수수료가 부가됩니다. 수수료는{0}원이며, 현재 잔액은 {1}원 입니다.".format(commission, balance))

# 입금 실행 순서 [1] => # 입금 실행 순서 [2] => # 입금 실행 순서 [3] => # 입금 실행 순서 [4]
# 출금 실행 순서 [1] => # 출금 실행 순서 [2]

# 기본값

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang)) # 이렇게 \ 하고 엔터를 하면 이 두문장은 한문장처럼 실행시킬 수 있다.

profile("박상철", 23, "모쏠")
profile("심원준", 23, "연애중")

# 같은 학교 같은 학년 같은 반 같은 수업일때 사용되는것이 기본값이다.

def profile(name, age = 23, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang)) # 이렇게 \ 하고 엔터를 하면 이 두문장은 한문장처럼 실행시킬 수 있다.
profile("박상철")
profile("심원준")

# 키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "박기수", main_lang="파이썬", age = 24)
profile(main_lang="자바", age = 23, name = "박상철")

# 가변인자를 사용한 함수 호출

# 가변인자 사용 전

# def profile(name, age, lang1,lang2, lang3, lang4, lang5):
#     print("이름 :{0}\t나이 : {1}\t".format(name, age), end=" ") # end=""는/은 줄바꿈 하지 않고 " "(빈칸)으로 끝내겠다는 뜻.
#     print(lang1,lang2,lang3,lang4,lang5)


# 가변인자 사용 후

def profile(name, age, *lang):
    print("이름 :{0}\t나이 : {1}\t".format(name, age), end=" ") # end=""는/은 줄바꿈 하지 않고 " "(빈칸)으로 끝내겠다는 뜻.
    for lang in lang:
        print(lang, end=" ")
    print()

profile("박기수", 24, "파이썬", "C++", "자바", "연애", "리눅스", "자바스크립트")
profile("박상철", 23, "C++", "JAVA", "Python","쏠로", "C#")

# 지역변수와 전역변수

# 지역 변수 : 함수 내에서만 사용할 수 있는것.
# 전역 변수 : 모든 공간 즉, 프로그램 내에서 모든 공간에서 부를수 있는 것.

# 지역 변수 예시

gun = 10 # 여기에만 gun을 할당하면 def안에 gun이 정의되지 않아 에러
def checkpoint(soldiers): # 경계 근무
    global gun # 전역공간에 있는 gun을 사용한다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내2] 남은 총 : {0}".format(gun))
    return gun

print("[전체 총] : {0}".format(gun))
checkpoint(2) # 2명이 총을 들고 병기 근무 투입.
gun = checkpoint_return(gun, 2)

print("[남은 총] : {0}".format(gun))