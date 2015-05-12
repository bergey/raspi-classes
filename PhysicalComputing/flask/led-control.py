from flask import Flask

# setup the LED output
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.out)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(index.html)

@app.route("/on")
def led_on():
    GPIO.output(13, True)    
    return render_template("on.html")

@app.route("/off")
def led_off():
    GPIO.output(13, False)
    return render_template("off.html")

if __name__ == "__main__":
    app.run()
