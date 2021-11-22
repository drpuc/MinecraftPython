from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
z=z+2
blockType = 10
mc.setBlock(x, y, z, blockType)
x=x+1
blockType = 10
mc.setBlock(x, y, z, blockType)
x=x-2
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z-1
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z-1
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z-1
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z-1
blockType = 10
mc.setBlock(x, y, z, blockType)
x=x+1
blockType = 10
mc.setBlock(x, y, z, blockType)
x=x+1
blockType = 10
mc.setBlock(x, y, z, blockType)
x=x+1
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z+1
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z+1
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z+1
blockType = 10
mc.setBlock(x, y, z, blockType)
z=z+1
blockType = 10
mc.setBlock(x, y, z, blockType)