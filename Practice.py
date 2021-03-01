# 표준 입출력
# print("Python" + "Java")
# print("Python", "Java", sep = ",", end = "?")
# print("무엇이 더 재밌을까여?")
# print("Python", "Java", "JavaScript", sep = " vs ")

import sys
print("Python", "Java", file = sys.stdout) # 표준 입력 처리
print("Python", "Java", file = sys.stderr) # 표준 에러 처리