# 키워드 값
def profile(name, age, main_lang) :
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바",  age = 25, name = "김태호")

# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") 
    # 앞 문장을 출력한 후 밑에 있는 문장을 이어서 출력함
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 20, "Pythom", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")


def profile(name, age, *languege) :
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") 
    for lang in languege :
       print(lang, end = " ")
    print()

profile("유재석", 20, "Pythom", "Java", "JavaScript", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")