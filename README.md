# Game Station
Game Station is a display and 4 controller. the 5 inch IPS display is powered by a esp32 S3, the controller by a Xiao Seeed esp32C6. the display comprises of a esp32 S3 rgb565 driver and the screen. The controllers include 2 sets of D pads (each with 4 buttons), a slider, a small screen and a imu to measure controller tilt.
<img width="1087" height="589" alt="image" src="https://github.com/user-attachments/assets/468669a8-3b51-4231-8b15-723507b3f746" />

## Purpose 
The purpose of the game station is so you can play retro games like Pong but also code your own compatible games. For example you could use the slider for Pong, and the D pads for something like Mario.

## Iterations
At first I decided I wanted to use batteries to power the 18650. So I created a PCB then did a BOM including the batteries. However once I did the BOM, the batteries were the most expensive thing, costing close to $40, because shipping is expensive. So once I omitted them, I had free budget so I decided I would get more components so I could make 4 controller instead of 2. But losing greater portability, which I didn't mind about. 

## PCB
My final PCB layout has the 0.91 inch oled in the top centre (screen is centred to overall PCB, screen is not centred on breakout board), with the esp32 C6 on the other side. Then I have the capacitors on either side of the screen. Below the screen I have the IMU, so it is almost directly in the middle to give accurate readings. On either side of the IMU, I have the two D pads, these are analog, so whichever button you press, it decreases the voltage output, this was so it didn't use up as many pins on the esp32 C6. Below stretching almost all the way across the PCB is the sliding potentiometer. Below this centred on the middle is the spare pins ***ADD 5V*** on the PCB, also the I2C channel. On either side of the spare pins is the resistor for the analog D pad. 

<img width="676" height="492" alt="image" src="https://github.com/user-attachments/assets/95673db5-16c0-4f24-a7ec-1d734c01b6db" />
*Final Design

<img width="689" height="552" alt="image" src="https://github.com/user-attachments/assets/59026632-d6ae-484d-b79e-2c4f2fffc115" />
*First Design

## Schematic Diagram 
I did my schematic diagram carefully making sure I wired the components up together. Especially the D pads with them amount of resistors and capacitors. Thankfully though when I was changing the PCB layout and getting rid of the batteries, I actually didn't have to change the schematic.

<img width="992" height="654" alt="image" src="https://github.com/user-attachments/assets/aafda7f6-3c4a-4ab4-a8ae-36f869e51bf5" />

## BOM
My bill of materials adds up to quite a lot but is all necessary for the project. You may notice, over half the cost is in the top two items, the display and the esp32C6. This is understandable because they are the main parts and the brains of the entire project. I am also slightly over but because most my stuff is from AliExpress, I should be able to get some good discounts. 
