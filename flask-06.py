# -*- coding: utf-8 -*-
from flask import Flask, redirect
from gpiozero import LEDBoard

app = Flask(__name__)

# LED 그룹 설정 (BCM 14, 15번 핀)
leds = LEDBoard(17, 27)

# 메인 화면: 버튼 3개를 화면에 배치
@app.route('/')
def home():
    return """
        <html>
            <head>
                <title>LED 웹 제어판</title>
                <style>
                    .button {
                        padding: 15px 25px;
                        font-size: 20px;
                        margin: 10px;
                        cursor: pointer;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }
                    .btn-led1 { background-color: #4CAF50; } /* 초록 */
                    .btn-led2 { background-color: #2196F3; } /* 파랑 */
                    .btn-off  { background-color: #f44336; } /* 빨강 */
                </style>
            </head>
            <body>
                <h1>라즈베리파이 LED 제어센터</h1>
                <hr>
                <button class="button btn-led1" onclick="location.href='/led1'">LED 1 켜기</button>
                <button class="button btn-led2" onclick="location.href='/led2'">LED 2 켜기</button>
                <button class="button btn-off"  onclick="location.href='/off'">모두 끄기</button>
                <hr>
            </body>
        </html>
    """

@app.route('/led1')
def led1_on():
    leds[0].on()
    leds[1].off()
    return redirect('/')  # 팝업 없이 바로 메인화면으로 돌아감

@app.route('/led2')
def led2_on():
    leds[0].off()
    leds[1].on()
    return redirect('/')

@app.route('/off')
def all_off():
    leds.off()
    return redirect('/')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000)