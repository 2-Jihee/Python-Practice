''' 표준 체중을 구하는 프로그램을 작성하시오.

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(hight), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다. '''

def std_weight(hight, gender) :
    if gender == "남자" :
        std_weight = hight * hight * 22 
        print("키 {0}cm {1}의 표준 체중은 {2}}kg 입니다.".format(round(hight, gender, std_weight_male))
        return std_weight

    elif gender == "여자" :
        std_weight = highthight * hight * 21
        printprint("키 {0}cm {1}의 표준 체중은 {2}}kg 입니다.".format(round(hight, gender, std_weight_female))
        return std_weight
        
hight(161)
gender("여자")
