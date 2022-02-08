try : # 예외 처리문(시작)
    print("나누기 계산기")
    num1 = int(input("첫 번째 숫자를 입력하시오. : "))
    num2= int(input("두 번째 숫자를 입력하시오. : "))
    print("{0} / {1} = {2}입니다.".format(num1, num2, num1/num2))
except ValueError: # 예외 처리문(해당되는 에러가 났을때 출력하는 문구.)
    print("정수만 입력하시오.")
finally: # 마지막 구문으로 출력할 수 있게 사용.
    print("이용해 주셔서 감사합니다.")