To setup your Raspberry Pi at home, connect the RasPi to your network
router with the ethernet cable, and then connect it to power with the
µUSB cable.

The router will assign an IP address to the RasPi.  The easiest way to
find out what IP address it's using is to download and run the
[Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder).

That will provide an address like `192.168.1.100`.  You can use this
address to `ssh` into the RasPi.  On a Mac, `ssh` is already
installed.  Open terminal, and type `ssh pi@192.168.1.100`
(substituting the IP address from above) The RasPi will then ask for a
password.

Once you're logged in, you can change the password by typing: `passwd`
(note the missing letters)
