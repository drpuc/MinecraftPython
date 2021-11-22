# Подключаемся к Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
# Присваиваем переменным x, y и z значения координат
x = 10
y = 110
z = 12
# Меняем позицию игрока
mc.player.setTilePos(x, y, z)
time.sleep(10)
# Присваиваем переменным x, y и z значения координат
x = 300
y = 100
z = -740
# Меняем позицию игрока 
mc.player.setTilePos(x, y, z)
