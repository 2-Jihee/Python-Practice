'''지역변수와 전역변수
* 지역변수 : 함수 내에서만 쓸 수 있다. 
  함수가 호출될 때 만들어졌다가 함수 호출이 끝나면 사라진다.
* 전역변수 :  모든 공간(프로그램 내)에서 부를 수 있는 변수 '''

gun = 10

def checkpoint(soldiers) : # 경계근무
  # gun = 20
  global gun # 전역 공간에 있는 gun 사용
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {}".format(gun))

def checkpoint_ret(gun, soldiers) :
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {}".format(gun))
  return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))