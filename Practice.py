# pickle - 프로그램에서 사용하는 데이터를 파일 형태로 저장하는 것
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "윤성혁", "나이" : 32, "취미" : ["킹덤", "로스트아크", "지희생각하기"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# 파일 불러오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()