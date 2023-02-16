# Wav_Play.GB


![IMG_1291](https://user-images.githubusercontent.com/77835905/219470370-83eaf44b-e3b2-4163-9d47-d5eda31495f9.JPG)

## About the project

This is a rep for the Wav_Play.GB.

The Wav_Play.GB is a handheld Stepsequencer with up to 192 Steps and up too 6 voices.
It allows you to creat your own sample library and creat tracks on the go all in a familiar form factor.
At it´s heart is a Raspberry pi Zero 2W

It was born out of a University project.
Find out more on Instagram @wav_play.gb

##Turning the device on and off

To turn the Wav_Play.GB on, simply swich the power switch to the right.
To turn it off ** dont´t just switch the power switch to the left **
Go into the menue ofthe pyquencer, navigate to Shut Down and press A.
Wait until the led on the raspberry is of (the screen will still be on and white).
Than Switch the power switch to the left.

## Setting up the SD card and USB

Fist you will want to set up the SD card. For that you simply need to flash our custom img file using 
the Raspberry Pi Imager.

To set up the USB first format it to Fat32 and rename it to PYQUENCER (all caps).
Than Download the Usb_Root folder on github.
Unzip the Saves, Library and Songs folders and add all the folders of USB_Root to your USB

Congrats. You are all set. Plug the SD card and USB in your Wav_Play.GB and go wild



## Buildguide

A video build guide can be found here: https://youtu.be/5e7-cO_Iyow

#### Installing the Battery

Battery installation is highly dependent of the size of your battery. 
We recoment using a battery with the dimensions: 54x34x10mm
Those dismensions work perfectly with JRodrigos battery holder design 
over on Thingivers (https://www.thingiverse.com/thing:1418834)![Power_managment](https://user-images.githubusercontent.com/77835905/219465759-4763771f-11c3-41a5-bc06-043ad4fdbab0.png)


Simply guide the two leads of your battery through the little hole on the left of the holder 
and torugh the hole in the gameboy case. 
Put the holder and the battery in the compartment using the springs to hold it in place.
Close the compartment and you are done.

#### Wirering of the power side

![Power_managment](https://user-images.githubusercontent.com/77835905/219465759-4763771f-11c3-41a5-bc06-043ad4fdbab0.png)

#### Wiring of the Audio, Video, and input side: 

![Audio_Input_Video](https://user-images.githubusercontent.com/77835905/219466358-95b15d72-da4f-4a41-ab8e-a165c88f3e51.png)

***Don´t forget to bridge the two pats under the SCK printing on the Headphone Jack board***


#### Combinig both halves:

When everything is wired up, simply connect the micro usb to usb adapter to the Raspberry and solder in the positif and negative leads to the back of the Raspberry marked 5V and the unmarked pin underneath close to the Power in micro usb port.

## Troubleshooting

If your wav_play.gb doesn´t find your USB you can do a USB Recovery by plugin the USB into your computer and renaming it USB_REC than pluging it backl in your Wav_Play.GB

The device will fix the problem and shut down on it´s own.

Put the USB back into your PC and name it back to PYQUENCER and everything should be fine again.

Video explenation: https://youtu.be/XgMAqk8Z5bY

## Adding your own library

This Video explains how to add your own library
https://www.youtube.com/watch?v=3tRRe0SVF7o
