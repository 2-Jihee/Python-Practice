''' Quiz) 당신은 회사에서 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형식으로 출력되어야 합니다.

- x 주차 주간 보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램으 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차 txt', ...와 같이 만듭니다. '''

report_file = open("{0}주차.txt".format(1), "w", encoding="utf8")
print("- {0} 주차 주간 보고 -".format(1), file=report_file)
print("부서 : ", file=report_file)
print("이름 : ", file=report_file)
print("업무 요약 : ", file=report_file)
report_file.close()