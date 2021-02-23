def open_account() :
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money) :  # 입금
    print("입금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance + money))
    return balance + money

def withraw(balance, money) : # 출금
    if balance >= money : # 잔액이 출금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance))
        return balance

def withraw_night(balance, money) : # 저녁에 출금
    commision = 100 # 수수료 100원
    return commision, balance - money - commision

# 입금하기, 출금하기
balance = 0
balance = deposit(balance, 1000)
# balance = withraw(balance, 2000)
# balance = withraw(balance, 500)
commision, balance = withraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commision, balance))