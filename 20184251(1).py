import RPi.GPIO as GPIO #LED를 제어하기 위한 GPIO 부분을 사용하기 위해 RPI.GPIO를 import 함
import time
import random
GPIO.setmode(GPIO.BCM) #GPIO.setmode()함수는 핀 번호를 정할때 어떤 참조 방식을 사용하는지를 설정하는 함수
                       #GPIO.BCM은 브로드컴칩의 번호를 참조함.(BCM = Broadcom chip-specific pin numbers)

GPIO.setup(5, GPIO.OUT) #BCM 모드는 05을, BOARD 모드는 29를 사용
GPIO.setup(6, GPIO.OUT) #BCM 모드는 06을, BOARD 모드는 31를 사용
GPIO.setup(13, GPIO.OUT) #BCM 모드는 13을, BOARD 모드는 33를 사용
GPIO.setup(19, GPIO.OUT) #BCM 모드는 19을, BOARD 모드는 35를 사용
GPIO.setup(21, GPIO.IN) #BCM 모드는 21을, BOARD 모드는 40를 사용
GPIO.setup(27, GPIO.IN) #BCM 모드는 27을, BOARD 모드는 13를 사용

GPIO.output(5, False)
GPIO.output(6, False)
GPIO.output(13, False)
GPIO.output(19, False)

LED_list=[5, 6, 13, 19]

i = 0
int(i)
m = 0
try:
    while True:
        if GPIO.input(21) == 0: #스위치를 한 번 누를 때마다 숫자가 한 개씩 증가
            i = i + 1
            if(i%10== 3)or(i%10==6)or(i%10==9)or(int(i/10)==3)or(int(i/10)==6)or(int(i/10)==9):
                GPIO.output(a[m],False)
                GPIO.output(a[m-1],False)
                m = (m+1)%4
                time.sleep(0.3)
            else:
                GPIO.output(a[m],True)
                GPIO.output(a[m -1],False)
                m = (m+1)%4
                time.sleep(0.3)

        if GPIO.input(27) == 0: #스위치를 누르면 LED가 랜덤으로 작동
            while(1):
                randTemp = random.randrange(1,4) #1부터 4범위까지 랜덤 숫자

                GPIO.output(5, True)
                time.sleep(randTemp) #1초 부터 4초까지 랜덤
                GPIO.output(5, False)
                time.sleep(randTemp)
                
                GPIO.output(6, True)
                time.sleep(randTemp) 
                GPIO.output(6, False)
                time.sleep(randTemp)

                GPIO.output(13, True)
                time.sleep(randTemp) 
                GPIO.output(13, False)
                time.sleep(randTemp)

                GPIO.output(19, True)
                time.sleep(randTemp) 
                GPIO.output(19, False)
                time.sleep(randTemp)

except KeyboardInterrupt:
    GPIO.cleanup()
