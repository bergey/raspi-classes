from flask import Flask, render_template

app = Flask(__name__)

chip = spidev.SpiDev()
chip.open(0,0)

def readadc(channel):
    r = chip.xfer2([1,(8+channel)<<4,0])
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout

@app.route("/")
def photoR():
    return render_template("photoR.html", adc_raw=readadc(0))

if __name__ == "__main__":
    app.run()
