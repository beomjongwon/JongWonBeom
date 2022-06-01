import RPi.GPIO as GPIO #LED를 제어하기 위한 GPIO 부분을 사용하기 위해 RPI.GPIO를 import 함
GPIO.setmode(GPIO.BCM) #GPIO.setmode()함수는 핀 번호를 정할때 어떤 참조 방식을 사용하는지를 설정하는 함수
                       #GPIO.BCM은 브로드컴칩의 번호를 참조함.(BCM = Broadcom chip-specific pin numbers)
LED_0 = 22
LED_1 = 23
LED_2 = 24
LED_3 = 25

BUTTON_0 = 4
BUTTON_1 = 5

BUTTON_PRESS = 0
ON = 1
OFF = 0

GPIO.setup(LED_0, GPIO.OUT) #GPIO 22을, 핀번호 15를 사용
GPIO.setup(LED_1, GPIO.OUT) #GPIO 23을, 핀번호 16를 사용
GPIO.setup(LED_2, GPIO.OUT) #GPIO 24을, 핀번호 18를 사용
GPIO.setup(LED_3, GPIO.OUT) #GPIO 25을, 핀번호 22를 사용

GPIO.setup(BUTTON_0, GPIO.IN) #GPIO 04을, 핀번호 07를 사용
GPIO.setup(BUTTON_1, GPIO.IN) #GPIO 05을, 핀번호 29를 사용

while 1:
    but0_value = GPIO.input(BUTTON_0)
    but1_value = GPIO.input(BUTTON_1)

    if((but1_value != BUTTON_PRESS) and (but0_value != BUTTON_PRESS)):
        GPIO.output(LED_0, ON) # 버튼이 둘 다 안눌렸을때 0번 LED ON
        GPIO.output(LED_1, OFF)
        GPIO.output(LED_2, OFF)
        GPIO.output(LED_3, OFF)
    elif((but1_value != BUTTON_PRESS) and (but0_value == BUTTON_PRESS)):
        GPIO.output(LED_0, ON) # 0번 버튼만 눌렸을때 0번 1번 LED ON
        GPIO.output(LED_1, ON)
        GPIO.output(LED_2, OFF)
        GPIO.output(LED_3, OFF)
    elif((but1_value == BUTTON_PRESS) and (but0_value != BUTTON_PRESS)):
        GPIO.output(LED_0, ON) # 1번 버튼만 눌렸을때 0번 1번 2번 LED ON
        GPIO.output(LED_1, ON)
        GPIO.output(LED_2, ON)
        GPIO.output(LED_3, OFF)
    else:
        GPIO.output(LED_0, ON) # 0번 1번 버튼이 모두 눌렸을때 0번 1번 2번 3번 LED ON
        GPIO.output(LED_1, ON)
        GPIO.output(LED_2, ON)
        GPIO.output(LED_3, ON)
