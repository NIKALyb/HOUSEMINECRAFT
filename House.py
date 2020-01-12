from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import mcpi.block as block
pos = mc.player.getPos()
distance = 3
#door = block.WOOD_DOOR.id

x = round(pos.x+distance)
y = round(pos.y)
z = round(pos.z+distance)

#plat
mc.setBlocks(x-10,y-1,z-10,x+10,y-1,z+10,2)
#house
mc.setBlocks(x,y,z,x+6,y+4,z+8,5)
mc.setBlocks(x+1,y+1,z+1,x+5,y+3,z+7,0)
mc.setBlocks(x,y+1,z+2,x,y+2,z+2,0)
mc.setBlocks(x,y+2,z+4,x,y+3,z+6,20)
mc.setBlocks(x+1,y+1,z+4,x+1,y+1,z+6,228)
mc.setBlock(x+1,y+1,z+7,54)
mc.setBlocks(x-1,y+5,z-1,x+7,y+5,z+9,172)
mc.setBlocks(x,y+6,z,x+6,y+6,z+7,172)
#green
mc.setBlocks(x+2,y,z-3,x+6,y+2,z-3,161)
mc.setBlocks(x+6,y,z-3,x+6,y+2,z-8,161)
mc.setBlocks(x+6,y,z-8,x+2,y+2,z-8,161)
mc.setBlocks(x+2,y-1,z-4,x+5,y-1,z-7,1)
