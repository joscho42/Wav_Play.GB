import time
from subprocess import call
import keyboard
#rename the usb too    USB_REC  put USB in device,
#turn device on. After Autoshutdown, rename USB to PYQUENCER 
#rename the usb too    USB_REC
#turn device on. After Autoshutdown, rename USB to PYQUENCER 
#rename the usb too    USB_REC
#turn device on. After Autoshutdown, rename USB to PYQUENCER 
#rename the usb too    USB_REC
#turn device on. After Autoshutdown, rename USB to PYQUENCER 
#rename the usb too    USB_REC
#turn device on. After Autoshutdown, rename USB to PYQUENCER 
#rename the usb too    USB_REC

call("sudo rm -r /media/pi/PYQUENCER", shell=True)
for i in range (20):
    call("sudo rm -r /media/pi/PYQUENCER{}".format(i), shell=True)
    
call("sudo shutdown -h now", shell=True)
    