import display      
import time
# Import modules needed

lcd = display.TFT()

# Initializing a standard large-panel layout (Landscape Mode)
lcd.init(lcd.ST7789, width=800, height=480, rst_from_main=True)
# Stating screen limits and sizing

lcd.clear(lcd.BLACK)
lcd.text(lcd.FONT_DEFAULT, "Testing, testing...", 40, 40, color=lcd.WHITE)
lcd.text(lcd.FONT_DEFAULT, "Console Live!", 40, 80, color=lcd.GREEN)
# Test text to show on display.


# Yellow lines are because code is in micropython