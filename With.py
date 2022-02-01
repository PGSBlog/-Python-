# Pickle에서 파일을 열고 - 처리작업 - 닫는것을 했는데 with를 써서 같은 효과를 볼 수 있다.
'''
import pickle

with open("profile.pickle","rb") as profile_file : 
    print(pickle.load(profile_file))
'''

# Pickle를 사용하지 않고 with를 사용해 2문장으로 같은 효과를 적용하는 방법

with open("study.txt", "w", encoding="utf8") as study_file :
    study_file.write("파이썬을 열심히 공부해보자!")

with open("study.txt", "r", encoding="utf8") as study_file :
    print(study_file.read())