# Task 5.2C - Change the Light Intensity Using GUI

## 1. Project Overview

This project extends Task 5.1P by adding a brightness control to the
Living Room light. A GUI slider is used to change the intensity of
the LED using PWM.

## 2. Objective

The objective of this task is to control the intensity of the Living
Room LED through a graphical user interface.

The user can move the slider to increase or decrease the brightness
of the LED.

## 3. Hardware Required

- Raspberry Pi 4
- LED
- Resistor
- Breadboard
- Jumper wires

## 4. Software Used

- Raspberry Pi OS
- Python
- Tkinter
- GPIO library

## 5. Hardware Setup

The Living Room LED is connected to a GPIO pin that supports PWM.
The LED is connected through a resistor to protect the LED.

Add your hardware setup image here.

![Hardware Setup](images/hardware_setup.png)

## 6. GUI Design

The GUI contains:

- Living Room light control
- ON button
- OFF button
- Brightness slider

The brightness slider allows the user to select the required
intensity level.

Add your GUI screenshot here.

![GUI](images/gui.png)

## 7. PWM Implementation

PWM is used to control the brightness of the LED. Changing the PWM
duty cycle changes the amount of time the LED is switched on during
each cycle.

A lower duty cycle produces lower brightness, while a higher duty
cycle produces higher brightness.

## 8. Program Structure

The Python program contains the following main parts:

1. Importing the required libraries.
2. Setting up the Living Room LED.
3. Creating the GUI window.
4. Creating the ON and OFF controls.
5. Creating the brightness slider.
6. Updating the LED brightness according to the slider value.
7. Starting the GUI event loop.

## 9. Testing

The system was tested by:

- Turning the Living Room LED ON.
- Turning the Living Room LED OFF.
- Moving the brightness slider to different values.
- Checking that the physical LED brightness changed.
- Checking that the GUI responded correctly.

## 10. Results

The GUI successfully controls the Living Room LED and allows its
brightness to be adjusted using the slider.

Add screenshots of your testing here.

### LED OFF

![LED Off](images/led_off.png)

### Low Brightness

![Low Brightness](images/low_brightness.png)

### High Brightness

![High Brightness](images/high_brightness.png)

## 11. Video Demonstration

Video link:

PASTE YOUR YOUTUBE OR PANOPTO LINK HERE

## 12. GitHub Repository

Repository link:

PASTE YOUR GITHUB LINK HERE