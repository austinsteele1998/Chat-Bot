#!/usr/bin/env python

"""\
Demo: read own phone number
"""

from __future__ import print_function

import logging


# sudo lsof /dev/ttyUSB0
# remove modemmanager
# sudo apt-get purge modemmanager
# 2c7c:0125
# Need to turn OFF network manager
#ID = 2c7c:0125

# use minicom to send AT commands



#Phone Number:
#18126028338
#Carrier: T-Mobile
#Is Wireless: y
#SMS Gateway Address:8126028338@tmomail.net
#MMS Gateway Address: 8126028338@tmomail.net
# AT+CSCA

PORT = '/dev/ttyUSB2'
BAUDRATE = 9600
PIN = None # SIM card PIN (if any)

from gsmmodem.modem import GsmModem

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

modem = GsmModem(PORT, BAUDRATE)
modem.connect(PIN)

modem.imei

modem.model

modem.networkName
modem.sendSms(destination="+18126321164",text="Hello")


def main():
    print('Initializing modem...')
    # Uncomment the following line to see what the modem is doing:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE)
    modem.connect(PIN)

    #
    print("The SIM card phone number is:")


    # Uncomment the following block to change your own number.
    modem.ownNumber = "+8126028338" # lease empty for removing the phone entry altogether

    number = modem.ownNumber
    print("A new phone number is:")
    print(number)

    # modem.close();

if __name__ == '__main__':
    main()