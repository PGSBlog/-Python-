# Pockle은 프로그램상에서 우리가 사용하고 있는 데이터를 파일화 해주는 작업

# 정보를 파일화 하는 법
'''
import pickle
profile_file = open("profile.pickle", "wb") # 'w'는 write(쓰기) , 'b'는 binary이다.profile_file = open("profile.pickle", "wb", encoding="utf8") # 'w'는 write(쓰기) , 'b'는 binary이다.
profile = {"이름" : "박상철", "나이" : 23, "취미":["축구", "헬스","솔로"]}
print(profile)
pickle.dump(profile, profile_file)  # pickle을 사용해 file화 하는 작업
                                    # profile에 있는 정보를 profile_file에 저장
profile_file.close()
'''

# 파일화된 정보를 가져오는 법
import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일(profile_file)에 있는 내용을 가져와서 데이터 형태(profile에다가 정보를 불러옴.)로 불러온다.
print(profile)
profile_file.close()