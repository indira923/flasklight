from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

# sense = SenseHat()

app = Flask(__name__)
led = LED(17)


@app.route('/')

def index():
    return render_template('index.html')

#Accepts post request
@app.route('/message', methods=['POST'])
def post_message():
    message = request.form['message']
    name = request.form['name']

    if (message == ""):
        display = f'no message  Love, {name}'
    print (display)


@app.route('/about')
def blink():
    blink = request.form ['light']
    led.off ()
    if blink =='on':
        print('light on')
        led.on()
    if blink == 'off' :
        print('light off')
        led.off()
    else:
        print('light blinking')









# def color(): 
    
#     # sense.show_message(display, text_colour=[0, 0, 255])
#     return render_template('received.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


