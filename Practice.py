# 파일 입출력
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines :
    print(line, end="")

score_file.close()