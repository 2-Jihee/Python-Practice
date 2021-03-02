# 표준 입출력
# print("Python" + "Java")
# print("Python", "Java", sep = ",", end = "?")
# print("무엇이 더 재밌을까여?")
# print("Python", "Java", "JavaScript", sep = " vs ")

# import sys
# print("Python", "Java", file = sys.stdout) # 표준 입력 처리
# print("Python", "Java", file = sys.stderr) # 표준 에러 처리

# # 시험 성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100 }
# for subject, score in scores.items() :
#     # print(subject, score)
#     print(subject.ljust(4), str(score).rjust(4), sep = " : ")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21) :
    print("대기번호 : " + str(num).zfill(3))