from machine import Pin, I2C
import ssd1306
import time
# Get the nessecary bit together to run the screen

i2c = I2C(0, sda=Pin(22), scl=Pin(23), freq=400000)
# Stating the screen pin out numbers


oled = ssd1306.SSD1306_I2C(128, 32, i2c)
# Stating the screen size and type

oled.fill(0)
oled.text("Testing, testing...", 0, 0)
oled.text("Controller OK!", 0, 16)
oled.show()
# Test text to show on the 0.91 inch display


# Yellow lines are because code is in micropython