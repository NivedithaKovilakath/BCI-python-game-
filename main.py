import pygame
import random
import sys

pygame.init()
pygame.font.init()

display_width=1000
display_height=600
clock=pygame.time.Clock()
WHITE=(255,255,255)
RED = (255,0,0)
GREEN= (0,255,0)
BLUE=(0,0,255)
guess = 1
screen= pygame.display.set_mode((display_width,display_height))

## BACK END

def is_valid(strguess):
    flag = True
    for i in strguess:
        if i not in ("r","g","b"):
            flag = False
    if len(strguess) != 3:
        flag = False
    return flag
    pass

#correct colour wrong or right place
def digitsMatched(anum,gnum):
    m=0
    newGuess = []
    newAnswer = []
    for x,y in zip(gnum,anum):
        if x != y:
            newGuess.append(x)
            newAnswer.append(y)
    print("newg",newGuess)
    print("newa",newAnswer)
    for letter in newGuess:
        for i in range(min(newAnswer.count(letter),newGuess.count(letter))):
            m+=1
    return m
#correct place correct colour
def find_fully_correct(answer, guess):
    res= 0
    for x, y in  zip(guess, answer):
        if x == y:
            res+=1
    return res 
#create adminno/answer
def create_code():
    characters = '123123123123123'
    length = 3 
    l = list(random.sample(characters,length))
    return l
answer = create_code()
print("ANSWER",answer)






##FRONT END
validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font(None, 25)
    self.image = self.font.render(" ", False, [0, 0, 0])
    self.rect = self.image.get_rect()
  def add_chr(self, char):
    if char in validChars:
        self.text += char
    self.update()
  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos
def textb(cordinate):
    textBox = TextBox()
    textBox.rect.center = cordinate
    running = True
    while running:
      #screen.fill([255, 255, 255])
      screen.blit(textBox.image, textBox.rect)
      pygame.display.flip()
      for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                pass
        if e.type == pygame.KEYDOWN:
            textBox.add_chr(pygame.key.name(e.key))
            if e.key == pygame.K_SPACE:
                textBox.text += " "
                textBox.update()
            if e.key == pygame.K_BACKSPACE:
                textBox.text = textBox.text[:-1]
                textBox.update()
            if e.key == pygame.K_RETURN:
                if len(textBox.text) > 0:
                    #print (textBox.text)
                    running = False
    return textBox.text
def play_screen():
    text1=myfont.render("Enter your Guess: ", 1, (211, 229, 219))
    screen.blit(text1, (275,25))
    t2 = myfont.render("Correct colour",1,(254,0,230))
    screen.blit(t2,(700,100-35))
    t3 = myfont.render("Correct place",1,(254,0,230))
    screen.blit(t3,(600,150-35))
    t4 = myfont.render("Wrong place",1,(254,0,230))
    screen.blit(t4,(800,150-35))
    pygame.draw.line(screen,(255,255,255),(770,100),(770,600),1)
    pygame.draw.line(screen,(255,255,255),(590,100),(940,100),1)
    pygame.draw.line(screen,(255,255,255),(590,60),(590,600),1)
    pygame.draw.line(screen,(255,255,255),(940,60),(940,600),1)
    pygame.draw.line(screen,(255,255,255),(590,60),(940,60),1)
    pygame.draw.line(screen,(255,255,255),(590,150),(940,150),1)

    g1=pygame.draw.circle(screen,WHITE,(300-25,100),30,2)
    g2=pygame.draw.circle(screen,WHITE,(400-25,100),30,2)
    g3=pygame.draw.circle(screen,WHITE,(500-25,100),30,2)
    pygame.display.update()
def input_guess():
    flag = False
    while not flag:
        insta = textb([700,10])
        if is_valid(insta):
            flag=True
            invalid("yes")
            print("ya")
            return insta
        else:
            invalid("no")
            print("no")
def invalid(yn):
    if yn=="no":
        t3 = myfont.render("INVALID!!",1,(255,0,0))
        screen.blit(t3,(450,300))
        pygame.display.update()
    elif yn=="yes":
        t3 = myfont.render("INVALID!!",1,(0,0,0))
        screen.blit(t3,(450,300))
        pygame.display.update()
def output_guess(insta):
    global guess
    #guess colours
    textsurface = myfont.render(("Guess #"+str(guess+1)), 1, (255, 255, 255))
    screen.blit(textsurface,(75,180+guess*75))
    colours ={
      "r":RED,
      "g":GREEN,
      "b":BLUE
      }
    col = []
    for letter in insta:
      col.append(colours[letter])
    for g in range(3):  
      op1=pygame.draw.circle(screen,col[g],((g+3)*100-25,185+guess*75),30,0)
    pygame.display.update()
    #clues
    numbers = {
        "r":"1",
        "g":"2",
        "b":"3"
        }
    guesss = []
    for letter in insta:
        guesss.append(numbers[letter])
    print("GUESS",guesss)
    
    match=digitsMatched(answer,guesss)
    print("Correct colour (wrong place  )",match)
    t4 = myfont.render(str(match),1,(255,255,255
                                     ))
    screen.blit(t4,(800,185+guess*75))
    
    count = find_fully_correct(answer,guesss)
    print("Correct colour (right place)   ",count)
    t4 = myfont.render(str(count),1,(255,255,255))
    screen.blit(t4,(600,185+guess*75))
    
    if count == 3:
        game_over_screen("win")
    elif guess == 4:
        game_over_screen("lose")
    pygame.display.update()
    

def game_over_screen(result):
    if result =="win":
        screen.fill((240,128,128))
        t4 = endfont.render(" YOU WIN!",1,(0,0,0))
        screen.blit(t4,(275,225))
        print("GAME OVER")
    elif result == "lose":
        screen.fill((240,128,128))
        t4 = endfont.render(" YOU LOSE!",1,(0,0,0))
        screen.blit(t4,(275,225))
        print("GAME OVER")
        
    pass


    
def main():
    global myfont, screen, guess, endfont
    myfont=pygame.font.SysFont("Times New Roman", 25)
    endfont=pygame.font.SysFont("Times New Roman", 75)
    pygame.display.set_caption('MASTERMIND')
    play_screen()

    for guess in range(5):
        insta = input_guess()
        output_guess(insta)
        guess+=1
        
    done = False
    while not done:
       # --- Event Processing
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

main()





COW:
for i in range(guesses):
           # read guess
           guess = (0,1,2) # this is an example
           # insert backend code
           # if true, game over, else copy current guess, table and continue 
           correct_guess = False # Or False based on backend code
           if (not correct_guess):
             pygame.draw.circle(screen,circle_col[guess[0]],(200,200+75*i),20,0)
             pygame.draw.circle(screen,circle_col[guess[1]],(300,200+75*i),20,0)
             pygame.draw.circle(screen,circle_col[guess[2]],(400,200+75*i),20,0)
             for j in range(3):
                circle = circle_loc[j]
                pygame.draw.circle(screen,WHITE,circle,30,3)
           else: # game over
             # show initial config on big circles and print game over
             for j in range(3):
               circle = circle_loc[j]
               color = guess[j]
               pygame.draw.circle(screen,circle_col[color],circle,30,0)
           
def init_game():
    global initial_config
    # Create initial config , save (G,B,R)
    # code: R = 0, G = 1, B = 2
    
    initial_config = []
    for _ in range(3):
       initial_config.append(random.randrange(3))
        
