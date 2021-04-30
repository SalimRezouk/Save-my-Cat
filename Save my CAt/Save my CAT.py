#Devloped vy 
import tkinter

#only press return once
okToPressReturn = True

#the player's attributes
hunger = 10
thirsty = 10
sleep = 10
fun = 10
condition = "Good"
average = 0
age = 0
#-------------------------------------------------------------------

def startGame(event):

    global okToPressReturn
    
    global name

    if okToPressReturn == False:
        pass
    
    else:
        #update the time left label.
        startLabel.config(text="")
        #start updating the values
        updatehunger()
        updatethirsty()
        updateage()
        updateDisplay()
        updateSleep()
        updateCondition()
        updateFun()

        okToPressReturn = False

#-------------------------------------------------------------------
 
def updateDisplay():

    #use the globally declared variables above.
    global hunger
    global age
    global thirsty
    global sleep
    global condition

    if hunger > 10:
        catPic.config(image = catfullphoto)
    if hunger == 10:
        catPic.config(image = titlephoto)
    elif hunger>=9 and hunger <10:
        catPic.config(image = normalphoto)
    elif hunger>8 and hunger<9:
        catPic.config(image=yeahphoto)
    elif hunger>=7 and hunger <=8:  
        catPic.config(image=stickyphoto)
    elif hunger>6 and hunger <7:
        catPic.config(image=nothingphoto)
    elif hunger >=5 and hunger <=6:
        catPic.config(image = calmphoto)    
    elif hunger >=4 and hunger<5:
        catPic.config(image = hungryphoto)
    elif hunger >=3 and hunger<4:
        catPic.config(image = hungerphoto)
    elif hunger >=2 and hunger<3:
        catPic.config(image = almostphoto)
    elif hunger>=1 and hunger<2:
        catPic.config(image = baseballbatphoto)
    elif hunger ==0:
        catPic.config(image = revengephoto)    
    else: 
        catPic.config(image = titlephoto)

    #update the food label.
    hungerLabel.config(text="hunger: " + str(hunger))

    #update the drink label.
    thirstyLabel.config(text="thirsty: " + str(thirsty))

    #update the sleep term label.
    sleepLabel.config(text="sleep: " + str(sleep))

    #update the condition's label.
    conditionLabel.config(text="Condition: " + str(condition))

    #update the fun's label.
    funLabel.config(text="fun: " + str(fun))

    #update the age's label.
    ageLabel.config(text="age: " + str(age))   

    #run the function again after 50ms.       
    catPic.after(50, updateDisplay)

#-------------------------------------------------------------------
 
def updatehunger():

    #use the globally declared variables above.
    global hunger

    #decrement the hunger.
    hunger -= 1

    if isAlive():
        #run the function again after 1200ms.
        hungerLabel.after(1200, updatehunger)

#-------------------------------------------------------------------
 
def updatethirsty():

    #use the globally declared variables above.
    global thirsty

    #decrement the thirst.
    thirsty -= 1

    if isAlive():
        #run the function again after 2000ms.
        thirstyLabel.after(2000, updatethirsty)

#-------------------------------------------------------------------

def updateSleep():

    #use the globally declared variables above.
    global sleep

    #decrement the sleep.
    sleep -= 1

    if isAlive():
        #run the function again after 3000ms.
        sleepLabel.after(3000, updateSleep)

#-------------------------------------------------------------------

def updateFun():

    #use the globally declared variables above.
    global fun

    #decrement the fun.
    fun -= 1

    if isAlive():
        #run the function again after 3000ms.
        funLabel.after(4000, updateFun)

#-------------------------------------------------------------------

def updateCondition():
	global condition
	global fun
	global hunger
	global thirsty
	global sleep
	global average

	average = (hunger+fun+thirsty+sleep)/4

	if average >= 8 :
		condition = "Very Good"
	elif average >= 5 and hunger >= 5 and thirsty >= 5:
		condition = "Good"
	elif average >= 3 and hunger >= 3 and thirsty >= 3:
		condition = "not good"
	#elif average >= 1 :
	#	condition = "Not Good"
	elif average < 1 or hunger <1 or thirsty < 1:
		condition = "Died"
	
	#run the function again after 500ms.
	conditionLabel.after(500, updateCondition)

#-------------------------------------------------------------------

def updateage():

    #use the globally declared variables above.
    global age

    #decrement the hunger.
    age += 1

    if isAlive():
        #run the function again after 3 seconds.
        ageLabel.after(3000, updateage)

#-------------------------------------------------------------------

def feed():

    global hunger
    
    if hunger <= 9:
        hunger += 1
    else:
        hunger -=1

#-------------------------------------------------------------------

def drink():

    global thirsty
    
    if thirsty <= 9:
        thirsty += 1
    else:
        thirsty -=1

#-------------------------------------------------------------------        

def goToBed():

    global sleep
    
    if sleep <= 9:
        sleep += 1
    
#-------------------------------------------------------------------

def play():

    global fun
    
    if fun <= 9:
        fun += 1
    
#-------------------------------------------------------------------

def isAlive():

    global hunger
    
    if hunger <= 0 or thirsty <=0:
        #update the start info label.
        startLabel.config(text="""GAME OVER! 
        YOU KILLED YOUR CAT!
        Remember, cats have nine lives.
        Now, it's the cat's turn!

        Thanks for playing!
        ***Your score is : """ + str(age) + """***""")
    
        return False
    else:
        return True

#-------------------------------------------------------------------

def close_window():
    import sys
    sys.exit()       
#-------------------------------------------------------------------


#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Save my CAT")
#set the size.
root.geometry("600x700")

#Enter tha cat's name.
value = tkinter.StringVar(root)
value.set("Entrer nom du chat")
entree = tkinter.Entry(root, textvariable=value, width=30)
entree.pack()

#add a label for the start text.
startLabel = tkinter.Label(root, text="Press 'Return/Enter' to start!", font=('Helvetica', 12))
startLabel.pack()

#add a condition label.
conditionLabel = tkinter.Label(root, text="Condition: " + str(condition), font=('Helvetica', 12))
conditionLabel.pack()

#add a hunger label.
hungerLabel = tkinter.Label(root, text="hunger: " + str(hunger), font=('Helvetica', 12))
hungerLabel.pack()

#add a drink label.
thirstyLabel = tkinter.Label(root, text="thirsty: " + str(thirsty), font=('Helvetica', 12))
thirstyLabel.pack()

#add a sleep label.
sleepLabel = tkinter.Label(root, text="sleep: " + str(sleep), font=('Helvetica', 12))
sleepLabel.pack()

#add a drink label.
funLabel = tkinter.Label(root, text="fun: " + str(fun), font=('Helvetica', 12))
funLabel.pack()


#add a age label.
ageLabel = tkinter.Label(root, text="age: " + str(age), font=('Helvetica', 12))
ageLabel.pack()

titlephoto = tkinter.PhotoImage(file = "cover.gif")
yeahphoto = tkinter.PhotoImage(file = "yeah.gif")
normalphoto = tkinter.PhotoImage(file="regular.gif")
stickyphoto = tkinter.PhotoImage(file = "sticky.gif")
nothingphoto = tkinter.PhotoImage(file = "nothing.png")
calmphoto = tkinter.PhotoImage(file = "calm.gif")
hungryphoto = tkinter.PhotoImage(file="hungrycat.gif")
hungerphoto =tkinter.PhotoImage(file ="feed_me.gif")
almostphoto = tkinter.PhotoImage(file = "hunger.gif")
baseballbatphoto = tkinter.PhotoImage(file = "baseballbat.gif")
revengephoto = tkinter.PhotoImage(file = "revenge.gif")
catfullphoto = tkinter.PhotoImage(file = "catfull.gif")

#add a cat image
catPic = tkinter.Label(root, image=titlephoto)
catPic.pack()

buttonFeed = tkinter.Button(root, text="Need to Eat", font = "Arial", fg = "black", activebackground="blue",
                            activeforeground="black", bg = "blue", width=20, command=feed)
buttonFeed.pack()

buttonDrink = tkinter.Button(root, text="Need to Drink", font = "Arial", fg = "black", activebackground="blue",
                            activeforeground="black", bg = "green", width=20, command=drink)
buttonDrink.pack()

buttonSleep = tkinter.Button(root, text="Need to Sleep", font = "Arial", fg = "black", activebackground="blue",
                            activeforeground="black", bg = "red", width=20, command=goToBed)
buttonSleep.pack()

buttonPlay = tkinter.Button(root, text="Need to Play", font = "Arial", fg = "black", activebackground="blue",
                            activeforeground="black", bg = "purple", width=20, command=play)
buttonPlay.pack()

buttonEnd = tkinter.Button (root, text="Goodbye", fg = "purple", bg = "black", activebackground="blue", 
                            font = "Arial", activeforeground="yellow",width=10, command=close_window)
buttonEnd.pack()

#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)

#start the GUI
root.mainloop()
