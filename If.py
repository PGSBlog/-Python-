# If문 예시 1) 
'''
weather = input("오늘의 날씨를 입력하시오. : ") # input는/은 사용자의 입력을 받는다. 그리고 input은 str형태만 입력 받는다.
if(weather == "비" or weather == "눈") :
    print("우산을 챙겨라.") 
elif(weather =="미세먼지") :
    print("마스크를 챙겨라")
else :
    pass
'''

# If문 예시 1) 

temp = int(input("오늘의 온도를 입력 하시오. : "))
if 30 <= temp :
    print("폭염주의보")
elif 10 <= temp and temp <=29 : 
    print("화창하다.")
else :
    pass