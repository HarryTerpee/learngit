import mcpi.minecraft as mmc
print('''######################################
#                                    #
#    Raspy Control Initialization    #
#                                    #
######################################
''')
while True:
    try:
        natappPort = int(input("Please specify the natapp port if given; input 0 to connect to local host: "))
    except ValueError:
        print("That wasn't a valid integer.")
    else:
        break
if natappPort:
    mc = mmc.Minecraft.create("server.natappfree.cc", natappPort)
else:
    mc = mmc.Minecraft.create()
print('Minecraft connection "mc" established!')
import mcpi.block as block
import mcpi.entity as entity
import mcpi.vec3 as vec3
import math
V3 = vec3.Vec3
import random,math
setb=mc.setBlock
setbs=mc.setBlocks
start=map(int,input('the starting position:').split())
direction=int(input('the starting direction(east=1,north=2,south=3,west=4):'))
pId=mc.getPlayerEntityId(map(mc.entity.getName, mc.getPlayerEntityIds()))
mc.entity.setTilePos(pId,start)
start=mc.entity.getTilePos(pId)
setbs(start.x,start.y-1,start.z-5,start.x+20,start.y,start.z+5,57)
setbs(start.x,start.y,start.z-5,start.y+6,start.z-5,57)
setbs(start.x,start.y,start.z+5,start.x+20,start.y+6,start.z+5,57)
setbs(start.x,start.y+6,start.z-5,start.x+20,start.y+6,start.z+5,57)
setbs(start.x,start.y+3,start.z-5,start.x+20,start.y+3,start.z-5,138)
setbs(start.x,start.y+3,start.z+5,start.x+20,start.y+3,start.z+5,138)
setbs(start.x+3,start.y-3,start.z-4,start.x+17,start.y,start.z+4,10)
for i in range(start.x+3,start.x+17,3):
    for j in range(start.z-4,start.z+4,3):
        m=random.randint(0,3)
        n=random.randint(0,3)
        setbs(i+m,start.y,j+n,i+m+1,start.y,j+n,57)
