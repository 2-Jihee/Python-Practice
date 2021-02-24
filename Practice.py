# # 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("이지희", 28, "파이썬")
profile("채승주", 28, "자바")


# 같은 학교, 같은 학년, 같은 수업
def profile(name, age = 19, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("이지희")
profile("채승주")