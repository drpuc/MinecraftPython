# Подключаемся к Minecraft
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
# Присваиваем переменным x, y и z значения координат
x = 57.0
y = 103.0
z = 31.0
time.sleep(1)
# Меняем позицию игрока
mc.player.setPos(x, y, z)
