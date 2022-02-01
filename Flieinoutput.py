# 파일 입출력 write하는법
'''
score_file = open("score.txt","w", encoding="utf8") # 'w'는 write(쓰다)라는 목적 utf8을 해줘야 한글이 깨지지 않는다.
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()
'''
# 파일을 항상 열었으면 닫아야한다.

# 파일 입출력 append하는법
'''
score_file = open("score.txt", "a", encoding="utf8") # 'a'는 append(덮어쓰기)라는 목적.
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
# print는 자동으로 줄바꿈이 되지만 score_file.write는 write를 통했을때는 \n(줄바꿈)을 해줘야한다.
score_file.close()
'''
# 파일 입출력 read하는법 방법 1)
'''
score_file = open("score.txt", "r", encoding="utf8") # 'r'은 read(읽기)라는 목적
print(score_file.read())
score_file.close()
'''
# 파일 입출력 read하는법 방법 2)
'''
score_file = open("score.txt", "r", encoding="utf8") # 'r'은 read(읽기)라는 목적
print(score_file.readline()) # 이러면 한줄만 읽어 온다. 커서는 다음 줄로 이동.
print(score_file.readline()) # 이러면 한줄만 읽어 온다. 커서는 다음 줄로 이동.
print(score_file.readline()) # 이러면 한줄만 읽어 온다. 커서는 다음 줄로 이동.
print(score_file.readline(), end="") # 이러면 한줄만 읽어 온다. 커서는 다음 줄로 이동. 줄바꿈 안하고 싶으면 end = ""하면된다.
score_file.close()
'''

# 파일 입출력 read할때, 몇줄인지 모를때 사용 방법
'''
score_file = open("score.txt", "r", encoding="utf8") # 'r'은 read(읽기)라는 목적
while True :
    line = score_file.readline()
    if not line : # 읽어올 line이 없다면 종료 없을때를 가정한는 것은 not으로 선언하자.
        break
    print(line, end="")
score_file.close()
'''
# list에다가 값을 다 처리해서 가져오는 방법
score_file = open("score.txt", "r", encoding="utf8") # 'r'은 read(읽기)라는 목적
lines = score_file.readlines() # 모든 line들을 가져와 list형태로 저장.
for line in lines :
    print(line, end ="")
score_file.close()