# ITC110 WN17
# Assignment 4 (taken to extremes)
# Ron Nims
import graphics
import math
import random
from graphics import *

class Face:

    def __init__(self, posX, posY, mood):
    
        self.posX = posX
        self.posY = posY		
        self.mood = mood
		# randomize dimensions and color of head/eyes cuz we celebrate diversity
        self.sizeX = maxFaceSize - random.randrange(maxFaceDelta)
        self.sizeY = maxFaceSize - random.randrange(maxFaceDelta)
        self.sizeEyeX = maxEyeSize - random.randrange(maxEyeDelta)
        self.sizeEyeY = maxEyeSize - random.randrange(maxEyeDelta)
        self.eyeWidth = (self.sizeX / 16) + ((self.sizeX / 12) * random.randrange(10)/10)
        self.eyeWeight = random.randrange(1,3)
        self.pupilHeight = (( self.sizeEyeY / 2 )) * (random.randrange(10)/10)
        self.pupilColor = pupilColor[random.randrange(len(pupilColor))]
        self.color = color[random.randrange(len(color))]
        self.mouthWidth = (self.sizeX * .25) + (self.sizeX * .25 * (random.randrange(10)/10))
        self.mouthHeight = (self.sizeY * .15) + (self.sizeY * .2) * (random.randrange(10)/10)


		
    def draw(self, win):
        # Draw face on win
        
        # keep mood in range of 1-5
        moodNow = self.mood
        if (moodNow < 1):
            moodNow = 1
        elif (moodNow > 5):
            moodNow = 5
                        

        oval1 = Point(self.posX - (self.sizeX / 2), self.posY - (self.sizeY /2))
        oval2 = Point(self.posX + (self.sizeX / 2), self.posY + (self.sizeY /2))
        face = Oval(oval1, oval2)
        face.setFill(self.color)
        face.draw(win)
		
        # draw left eye then clone right
        
        oval1 = Point(self.posX - (self.sizeEyeX + (self.eyeWidth / 2)), self.posY - self.sizeEyeY)
        oval2 = Point(self.posX - (self.eyeWidth / 2), self.posY)
        lEye = Oval(oval1,oval2)
        lEye.setWidth(self.eyeWeight)
        lEye.setFill(eyeColor)
        lEye.draw(win)
        rEye = lEye.clone()
        rEye.move( self.eyeWidth + self.sizeEyeX,0)
        rEye.draw(win)
		
        oval1 = Point(self.posX - ((self.sizeEyeX * .75) + (self.eyeWidth / 2)), self.posY - (self.sizeEyeY / 2) - self.pupilHeight)
        oval2 = Point(self.posX - ((self.sizeEyeX * .25) + (self.eyeWidth / 2)), self.posY - self.pupilHeight)
        lPupil = Oval(oval1,oval2)
        lPupil.setWidth(self.eyeWeight)
        lPupil.setFill(self.pupilColor)
        lPupil.draw(win)
        rPupil = lPupil.clone()
        rPupil.move( self.eyeWidth + self.sizeEyeX,0)
        rPupil.draw(win)
		
        self.drawMouth(self.posX, self.posY + self.mouthHeight, self.mouthWidth, moodNow, win)

    def drawMouth(self, posX, posY, mouthWidth, mood, win):
        # Draw mouth showing mood with a smile or frown
        mouthSeg = mouthWidth / 5
        stepSize = mouthSeg * .27
        xCoord = posX - ( mouthWidth / 2 )
        # offsetFactor determines how many Y-offset stepSizes are applied to endpoints of mouth lines
        offsetFactor = [3,1,0,0,1,3]

        for i in range(5):
            startPoint = Point(xCoord, posY + (((6 - mood) - 3) * stepSize * offsetFactor[i]))
            endPoint = Point(xCoord + mouthSeg, posY + (((6 - mood) - 3) * stepSize * offsetFactor[i+1]))
            mouthLine = Line(startPoint, endPoint)
            mouthLine.setWidth(2)
            mouthLine.draw(win)
            xCoord += mouthSeg
            
def withinX(clickPoint, anchorPoint, chkRange):
    clickX = clickPoint.getX()
    anchorX = anchorPoint.getX()
    if ( clickX > anchorX - chkRange) & ( clickX < anchorX + chkRange):
        return True
    else:
        return False

def adjustCrowd(crowd, newSize):
    while len(crowd) > newSize:
        crowd.pop()
    while len(crowd) < newSize:
        folk = Face((random.randrange(fieldWidth) + (maxFaceSize / 2)),(random.randrange(fieldHeight) + (maxFaceSize / 2)),random.randrange(5)+1)
        crowd.append(folk)       
    refreshCrowd(crowd)
    
def refreshCrowd(crowd):
    # rewrite display content
    displayArea.undraw()
    displayArea.draw(faceWin)
    for i in range(len(crowd)):
        crowd[i].draw(faceWin)

def bumpMood(crowd, deltaMood):
    for i in range(len(crowd)):
        crowd[i].mood += deltaMood
    refreshCrowd(crowd)


# define our universe of faces
winWidth = 880
winHeight = 640
consoleHeight = 40

# define face characteristics
maxFaceSize = winWidth / 8

# create a safe field so faces fit in window
fieldWidth = winWidth - maxFaceSize
fieldHeight = winHeight - maxFaceSize 

maxFaceDelta = int(round(maxFaceSize * .4))

# define face characteristics
maxEyeSize = int(round(maxFaceSize * .25))
maxEyeDelta = int(round(maxEyeSize * .4))

color = ['light blue','yellow','orange','purple','grey','cyan','grey','light green','pink','red','maroon']
pupilColor = ['blue','purple','dark grey','green','black','orange','red','maroon']
eyeColor = "white"

# set the initial number of faces
crowdSize = 12

   
faceWin = GraphWin("The Many Faces of Us", winWidth, winHeight + consoleHeight)

# create console area
console = Rectangle(Point(0,winHeight), Point(winWidth, winHeight + consoleHeight))
console.setFill('light blue')
console.draw(faceWin)

displayArea = Rectangle(Point(0,0), Point(winWidth, winHeight))
displayArea.setFill('beige')
displayArea.draw(faceWin)

# build console UI
crowdSizeLable = Text(Point(winWidth/8 ,winHeight + (consoleHeight/2)), "Current Crowd")
crowdSizeLable.setFill('grey')
crowdSizeLable.draw(faceWin)

crowdSizeInput = Entry(Point(winWidth/8 + 80,winHeight + (consoleHeight/2)), 4)
crowdSizeInput.setText(crowdSize)
crowdSizeInput.setFill('white')
crowdSizeInput.draw(faceWin)

root = crowdSizeInput.getAnchor()

adjustCrowdButton = Text(root, "Adjust Crowd")
adjustCrowdButton.move(winWidth/8, 0)
adjustCrowdButton.setFill('blue')
adjustCrowdButton.draw(faceWin)

buildBridgesButton = Text(root, "Build Bridges")
buildBridgesButton.move(winWidth/6 * 2, 0)
buildBridgesButton.setFill('green')
buildBridgesButton.draw(faceWin)

buildWallsButton = Text(root, "Build Walls")
buildWallsButton.move(winWidth/6 * 3, 0)
buildWallsButton.setFill('red')
buildWallsButton.draw(faceWin)

exitButton = Text(root, "EXIT")
exitButton.move(winWidth/6 * 4, 0)
exitButton.setFill('Black')
exitButton.draw(faceWin)

crowd = []
for i in range(crowdSize):
    folk = Face((random.randrange(fieldWidth) + (maxFaceSize / 2)),(random.randrange(fieldHeight) + (maxFaceSize / 2)),random.randrange(5)+1)
    folk.draw(faceWin)
    crowd.append(folk)

click = Point(0,0)
checkSpan = 50
while (click.getX() < ((winWidth / 8) * 7)) | (click.getY() < winHeight):
    if (click.getY() > winHeight):
        # click is in console area
        if withinX(click, adjustCrowdButton.getAnchor(), checkSpan):
            # click is adjustCrowdButton
            if (int(crowdSizeInput.getText()) < 10000):
                # make sure requested crowd size is not too large
                adjustCrowd(crowd, int(crowdSizeInput.getText()))
        if withinX(click, buildBridgesButton.getAnchor(), checkSpan):
            # click is buildBridgesButton
            bumpMood(crowd, 1)
        if withinX(click, buildWallsButton.getAnchor(), checkSpan):
            # click is buildWallsButton
            bumpMood(crowd, -1)
           
    click = faceWin.getMouse()

   
faceWin.close()	

