import random
leftPort = "vleft"
rightPort = "vright"

###########################################################################
### special virtual blender handling - not in "regular" scripts - begin ###

# start blender service
blender = Runtime.start("blender", "Blender")

# connect blender service to running Blender (2.72b) instance
if (not blender.connect()):
	print("could not connect")

# get Blender.py version 
# FIXME - compare expected version !
blender.getVersion()

# pre-create Arduinos 
i01_left = Runtime.start("i01.left", "Arduino")
i01_right = Runtime.start("i01.right", "Arduino")

# blender "attach" will connect Arduinos with serial ports running
# over tcp/ip sockets to Blender.py
blender.attach(i01_left)
sleep(6)
blender.attach(i01_right)

### special virtual blender handling - not in "regular" scripts - end  ###
##########################################################################

i01 = Runtime.start("i01", "InMoov")
i01.startHead(leftPort)

i01.startLeftArm(leftPort)
i01.startRightArm(leftPort)
i01.startMouthControl(leftPort)
i01.startMouth()

#to tweak the default voice
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")

# tweaking default settings of eyes
i01.head.eyeY.setMinMax(0,180)
i01.head.eyeY.map(0,180,75,95)
i01.head.eyeY.setRest(85)
i01.head.eyeX.setMinMax(0,180)
i01.head.eyeX.map(0,180,70,100)
i01.head.eyeX.setRest(85)
i01.head.neck.setMinMax(0,180)
i01.head.neck.map(0,180,15,155)
i01.head.neck.setRest(70)
i01.head.rothead.setMinMax(0,180)
i01.head.rothead.map(0,180,30,150)
i01.head.rothead.setRest(86)

# tweaking default settings of jaw
i01.head.jaw.setMinMax(6,25)
#i01.head.jaw.map(0,180,10,35)
i01.mouthControl.setmouth(6,25)
##############
i01.startEar()
##############
torso = i01.startTorso(leftPort)
# tweaking default torso settings
torso.topStom.setMinMax(0,180)
torso.topStom.map(0,180,67,110)
torso.midStom.setMinMax(0,180)
torso.topStom.map(0,180,60,120)
#torso.lowStom.setMinMax(0,180)
#torso.topStom.setRest(90)
#torso.midStom.setRest(90)
#torso.lowStom.setRest(90)
##############
i01.startLeftHand(leftPort)
# tweaking default settings of left hand
i01.leftHand.thumb.setMinMax(0,180)
i01.leftHand.index.setMinMax(0,180)
i01.leftHand.majeure.setMinMax(0,180)
i01.leftHand.ringFinger.setMinMax(0,180)
i01.leftHand.pinky.setMinMax(0,180)
i01.leftHand.thumb.map(0,180,45,140)
i01.leftHand.index.map(0,180,40,140)
i01.leftHand.majeure.map(0,180,30,176)
i01.leftHand.ringFinger.map(0,180,25,175)
i01.leftHand.pinky.map(0,180,15,112)
################
i01.startLeftArm(leftPort)
#tweak defaults LeftArm
#i01.leftArm.bicep.setMinMax(0,90)
#i01.leftArm.rotate.setMinMax(46,160)
#i01.leftArm.shoulder.setMinMax(30,100)
#i01.leftArm.omoplate.setMinMax(10,75)
################
i01.startRightHand(rightPort,"atmega2560")
# tweaking defaults settings of right hand
i01.rightHand.thumb.setMinMax(0,180)
i01.rightHand.index.setMinMax(0,180)
i01.rightHand.majeure.setMinMax(0,180)
i01.rightHand.ringFinger.setMinMax(0,180)
i01.rightHand.pinky.setMinMax(0,180)
i01.rightHand.thumb.map(0,180,55,135)
i01.rightHand.index.map(0,180,35,140)
i01.rightHand.majeure.map(0,180,8,120)
i01.rightHand.ringFinger.map(0,180,40,125)
i01.rightHand.pinky.map(0,180,10,110)
#################
i01.startRightArm(rightPort)
# tweak default RightArm
#i01.rightArm.bicep.setMinMax(0,90)
#i01.rightArm.rotate.setMinMax(46,160)
#i01.rightArm.shoulder.setMinMax(30,100)
#i01.rightArm.omoplate.setMinMax(10,75)

def takeball():
  i01.setHandSpeed("right", 0.85, 0.75, 0.75, 0.75, 0.85, 0.75)
  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(30,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,76,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,140,140,3,0,11)
  i01.moveTorso(120,100,90)


def studyball():
##keepball():
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",54,77,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,90,90)
  sleep(3)
##approachlefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,84)
  i01.moveArm("left",67,52,62,23)
  i01.moveArm("right",55,61,45,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
##uselefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(10,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,61,50,16)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,140,145,3,0,11)
  sleep(4)
##more():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.80, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(13,80)
  i01.moveArm("left",64,52,59,23)
  i01.moveArm("right",75,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",80,114,114,3,0,11)
  sleep(3)
##handdown():
  i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 1.0)
  i01.setArmSpeed("right", 0.85, 0.65, 0.65, 0.65)
  i01.moveHead(18,75)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",54,95,66,0,0,11)
  sleep(2)
#isitaball():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 0.8, 0.8, 0.90)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 0.95, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.90, 0.85)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(70,82)
  i01.moveArm("left",70,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)
  i01.mouth.speakBlocking("I will start tracking the object")
  sleep(2)
  i01.mouth.speakBlocking("you need to set the point")
  
def surrender():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(90,90)
  i01.moveArm("left",90,139,15,79)
  i01.moveArm("right",90,145,37,79)
  i01.moveHand("left",50,28,30,10,10,76)
  i01.moveHand("right",10,10,10,10,10,139)
  
def cyclegesture3():
    ##for x in range(3):
    rest()
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.9)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(50,110)
    i01.moveArm("left",88,90,70,23)
    i01.moveArm("right",73,90,70,27)
    i01.moveHand("left",2,2,2,2,2,90)
    i01.moveHand("right",2,2,2,2,2,90)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(50,70)
    i01.moveArm("left",88,90,75,28)
    i01.moveArm("right",80,90,76,21)
    i01.moveHand("left",180,180,180,180,180,90)
    i01.moveHand("right",180,180,180,180,180,90)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.setHandSpeed("left", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
    i01.setHandSpeed("right", 0.95, 0.95, 0.95, 0.95, 0.95, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(40,70)
    i01.moveArm("left",90,82,70,23)
    i01.moveArm("right",80,82,68,27)
    i01.moveHand("left",2,2,2,2,2,90)
    i01.moveHand("right",2,2,2,2,2,90)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveHead(50,100)
    i01.moveArm("left",88,90,70,28)
    i01.moveArm("right",75,90,76,21)
    i01.moveHand("left",180,180,180,180,180,10)
    i01.moveHand("right",180,180,180,180,180,170)
    i01.moveTorso(90,90,90) 
    sleep(2)
    i01.moveHead(50,70)
    i01.moveArm("left",88,90,75,28)
    i01.moveArm("right",80,90,76,21)
    i01.moveHand("left",180,180,180,180,180,170)
    i01.moveHand("right",180,180,180,180,180,10)
    i01.moveTorso(90,90,90)   
    sleep(3)
    i01.setHandSpeed("left", 0.9, 0.9, 0.9, 0.9, 0.9, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.9, 0.9)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(79,160)
    i01.moveArm("left",5,84,32,80)
    i01.moveArm("right",87,82,123,74)
    i01.moveHand("left",0,0,0,0,0,25)
    i01.moveHand("right",0,0,0,0,0,113)
    i01.moveTorso(170,90,90)
    sleep(6)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.setHeadSpeed(0.8, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(79,100)
    i01.moveArm("left",18,84,55,71)
    i01.moveArm("right",65,82,118,15)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 0.9,  0.9,  0.9,  0.9)
    i01.setArmSpeed("right",  0.9,  0.9,  0.9,  0.9)
    i01.setHeadSpeed(0.8, 0.8)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(60,50)
    i01.moveArm("left",18,84,54,69)
    i01.moveArm("right",65,82,118,13)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",180,180,180,180,180,113)
    i01.moveTorso(40,90,90)
    sleep(2)
    i01.moveHead(79,100)
    i01.moveArm("left",33,84,136,80)
    i01.moveArm("right",34,82,160,13)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",180,180,180,180,180,113)
    i01.moveTorso(90,90,90)
    sleep(2)
    ##arm right up
    i01.moveHead(100,100)
    i01.moveArm("left",33,84,136,80)
    i01.moveArm("right",34,82,160,20)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(90,90,90)
    sleep(3)
    i01.moveHead(110,120)
    i01.moveArm("left",33,140,136,80)
    i01.moveArm("right",34,82,170,30)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.moveHead(125,140)
    i01.moveArm("left",33,90,36,60)
    i01.moveArm("right",34,80,170,40)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(30,90,90)
    sleep(2)
    ##arm left up
    i01.moveHead(120,130)
    i01.moveArm("left",33,90,36,60)
    i01.moveArm("right",34,65,160,40)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",92,33,37,71,66,113)
    i01.moveTorso(50,90,90)
    sleep(2)
    i01.moveHead(79,100)
    i01.moveArm("left",18,84,54,69)
    i01.moveArm("right",65,78,118,13)
    i01.moveHand("left",92,33,37,71,66,30)
    i01.moveHand("right",180,180,180,180,180,113)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.moveHead(79,100)
    i01.moveArm("left",18,84,55,71)
    i01.moveArm("right",75,80,120,45)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(90,90,90)
    sleep(1)
    i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 0.85)
    i01.setHeadSpeed(0.9, 0.9)
    i01.setTorsoSpeed(1.0, 1.0, 1.0)
    i01.moveHead(79,160)
    i01.moveArm("left",24,84,32,74)
    i01.moveArm("right",87,82,123,74)
    i01.moveHand("left",0,0,0,0,0,25)
    i01.moveHand("right",0,0,0,0,0,113)
    i01.moveTorso(130,90,90)
    sleep(3)
    i01.moveHead(60,20)
    i01.moveArm("left",87,82,123,74)
    i01.moveArm("right",5,84,32,80)
    i01.moveHand("left",92,33,37,71,66,25)
    i01.moveHand("right",81,66,82,60,105,113)
    i01.moveTorso(30,90,90)
    sleep(6)
    i01.setHeadSpeed(1.0,1.0)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.moveHead(80,86)
    i01.moveArm("left",5,90,30,10)
    i01.moveArm("right",5,90,30,10)
    i01.moveTorso(90,90,90)
    sleep(2)
    i01.mouth.speakBlocking("wow, I feel good, I love this")
    sleep(2)
    rest()
    sleep(1)
    relax()
    
def rest():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(80,86,82,78,76)
  i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",2,2,2,2,2,90)
  i01.moveHand("right",2,2,2,2,2,90)
  i01.moveTorso(90,90,90)

def relax():
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
  i01.setArmSpeed("right", 0.75, 0.85, 0.65, 0.85)
  i01.setArmSpeed("left", 0.95, 0.65, 0.75, 0.75)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(79,100)
  i01.moveArm("left",5,84,28,15)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(90,90,90)

# create services
python = Runtime.start("python", "Python")
keyboard = Runtime.start("keyboard", "Keyboard")

counter = 0
 
# non blocking event example
keyboard.addKeyListener(python);
 
def onKey(key):
    global counter
    print "you pressed ", key
    counter = counter + 1
    print counter
    i01.speakBlocking("ok")

    if (counter == 1):
      rest()
    elif (counter == 2):
      i01.daVinci()
    elif (counter == 3):
      rest()
    elif (counter == 4):
      i01.giving()
    elif (counter == 5):
      i01.armsFront()
    elif (counter == 6):
      i01.armsUp()
    elif (counter == 7):
      surrender()
    elif (counter == 8):
      rest()
    elif (counter == 9):
      i01.victory()
    elif (counter == 10):
      rest()
    elif (counter == 11):
      cyclegesture3()
    elif (counter == 12):
      i01.speakBlocking("are we done? i am not tired. I could do more. my servos are not even hot")

# blocking example
# print "here waiting"
# keypress = keyboard.readKey()
# print "finally you pressed", keypress, "!"
  
i01.speakBlocking("I think I am ready")
i01.rest()
i01.speakBlocking("this is rest")
sleep(4)
i01.speakBlocking("this is takeball")
takeball()
i01.speakBlocking("this is studyball")
studyball()

# print (i01.captureGesture())

def Y():
  i01.moveHead(99,82,82,78,6)
  i01.moveArm("left",9,180,57,133)
  i01.moveArm("right",9,180,30,133)
  #i01.moveHand("left",61,0,14,38,15,0)
  #i01.moveHand("right",0,24,54,50,82,180)
  #i01.moveTorso(90,90,90)

def M():
  #i01.moveHead(104,80,82,78,6)
  i01.moveArm("left",129,180,57,133)
  i01.moveArm("right",124,180,57,133)
  #i01.moveHand("left",61,0,14,38,15,128)
  #i01.moveHand("right",0,24,54,50,82,180)
  #i01.moveTorso(90,90,90)

def C():
  #i01.moveHead(100,94,82,78,6)
  i01.moveArm("left",61,180,57,88)
  i01.moveArm("right",53,180,57,133)
  #i01.moveHand("left",61,0,14,38,15,128)
  #i01.moveHand("right",0,24,54,50,82,180)
  i01.moveTorso(90,36,90)

def A():
  #i01.moveHead(99,82,82,78,6)
  i01.moveArm("left",61,180,57,160)
  i01.moveArm("right",73,178,57,150)
  #i01.moveHand("left",61,0,14,38,15,134)
  #i01.moveHand("right",0,0,54,50,82,154)
  i01.moveTorso(90,90,90)
  

sleep(2)
Y()
sleep(2)
M()
sleep(2)
C()
sleep(2)
A()
sleep(2)
i01.rest()
