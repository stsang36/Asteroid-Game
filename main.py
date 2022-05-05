import math
app.step= 0
app.background = gradient('black', 'darkBlue','lightBlue', start = 'top');

earth = Group(
    Circle(200,700,400, fill = 'dodgerBlue'),
    Polygon(90,355,137,321,169,348,208,366,273,350,340,400,38,400, fill = 'green')
    )
stars = Group()
meteor = Group();
stem = Rect(190,370,20,30);
cannon = Group (
    Circle(200,370,20, fill = 'grey'),
    Rect(180,320,40,50, fill = gradient('darkGrey', 'grey', 'grey', start = 'top'))
    )
missles = Group();
diffBox = Group(
        Rect(310,350,80,30, fill = 'darkRed'),
        Label('Difficulty', 350,365, fill = 'white')
    )

difficulty = Label(int(0), 380,390, fill = 'white')
customDiff =Label('Your set difficulty is:', 310,390, fill = 'white')

difficultyLabel = Group (difficulty, customDiff)
difficultyLabel.visible = False;



def drawStars(x,y):

    star = Circle(x,y, 2, fill='white')
    stars.add(star)
    
for i in range(10):
    drawStars(randrange(1,401),randrange(1,151));
    pass


 

scoreStatic = Group(
    Rect(10,340,100,50, fill = 'blue', opacity = 40),
    Label('Score: ', 50,355, fill = 'white'),
    Label('Lives: ', 50,375, fill = 'white')
    ) 
scoreLabel = Label(int(0), 80,355, fill = 'white');
hitLabel = Label(int(5), 80,375, fill = 'white');
scoreKeep = Group(scoreStatic, scoreLabel,hitLabel);


def gameOver(outCome,endScore):
    Rect(80,120,240,120, fill = 'blue', opacity = 20);
    Label('Game Over!', 200,150, fill = 'white', size = 30);
    Label(outCome + str(endScore) , 200,190, fill = 'white', size = 15);
    app.stop();

def onStep():
    
    for missle in missles.children:
        for rock in meteor.children:
            if (missle.hitsShape(rock)):
                missles.remove(missle);
                meteor.remove(rock);
                scoreLabel.value += 1;

    app.step += 1
    if (app.step % 40 == 0):
        x = randrange(0,401);
        meteorBody = Circle(x,-10, randrange(10,41), fill = 'brown');
        meteorBody.fallSpeed = randrange(1,5) + int(difficulty.value);
        meteor.add(meteorBody)
        pass
    for m in meteor.children:
        m.centerY += m.fallSpeed
        if (m.top > 400):
            meteor.remove(m);
            hitLabel.value -= 1;
    if (hitLabel.value < 0):
        hitLabel.value = 'No lives!';
        hitLabel.size = 8;
        hitLabel.centerX = 85;
        gameOver("You LOST! Your Score is: ",scoreLabel.value );
            
    for m in missles.children:
        m.centerX += m.powerSpeed*m.dx
        m.centerY -= m.powerSpeed*m.dy

        pass

    pass
 
def onMouseMove(mouseX, mouseY):
    cannon.rotateAngle = angleTo(cannon.centerX, cannon.centerY, mouseX,mouseY)
    
    pass
 
def onMousePress(mouseX, mouseY):
    if (diffBox.hits(mouseX,mouseY)):
        difficultySetting = app.getTextInput();
        if (difficultySetting.isnumeric() == True) and (int(difficultySetting) >= 0):
            difficulty.value = int(difficultySetting)
        else:
            print('NOT A VALID RESPONSE!')
        if (int(difficultySetting) > 0 ):
            difficultyLabel.visible = True
        else:
            pass
        
    missle = Group();
    missleBody = Rect(cannon.centerX,cannon.centerY,10,20, fill = 'red');
    missleHead = RegularPolygon(missleBody.centerX, missleBody.top,10, 3, fill = 'red' );
    missle.add(missleBody, missleHead);
    missle.powerSpeed = 10
    missle.foundAngle = False;
    missle.dx = 0;
    missle.dy = 0;
    missles.add(missle);
    
    for m in missles.children:
        cannon.toFront()
        if (m.foundAngle == False):
            m.rotateAngle = angleTo(m.centerX, m.centerY, mouseX,mouseY)
            m.foundAngle = True;
            m.dy = math.cos(math.radians(angleTo(m.centerX, m.centerY, mouseX,mouseY)));
            m.dx = math.sin(math.radians(angleTo(m.centerX, m.centerY, mouseX,mouseY)));
            
        if (m.bottom < 0):
            missles.remove(m)
            pass

    pass
