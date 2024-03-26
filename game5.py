from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
import json
from tkinter import Tk, Text, Button, Label, Frame, PhotoImage
import tkinter.messagebox as messagebox
from tkinter import StringVar
from tkinter import Tk,Text,Button,StringVar,Label
import random


   

engine= pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)

mixer.init()
mixer.music.load("kbc.mp3")
mixer.music.play(-1)
#correct_answer=StringVar()
#from tkinter import messagebox
#================================FUNCTION TO SELECT AND CHANGE OPTION====================================#


# Uncomment the following lines to create an account and login
#create_account()
#login()





def select(event):
    callButtton.place_forget()
    progressBarA.place_forget()
    progressBarB.place_forget()
    progressBarC.place_forget()
    progressBarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()
    b=event.widget
    value=b["text"]

    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()
                def playagain():
                    lifeline50Button.config(state=NORMAL,image=image50)
                    audiencePoleButton.config(state=NORMAL,image=audiencePole)
                    phoneLifeLineButton.config(state=NORMAL,image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0,END)
                    questionArea.insert(END,question[0])
                    optionButton1.config(text=First_options[0])
                    optionButton2.config(text=Second_options[0])
                    optionButton3.config(text=Third_options[0])
                    optionButton4.config(text=Fourth_options[0])
                    amountLabel.config(image=amountImages)
               # load_new_questions()
                mixer.music.stop()
                mixer.music.load("kbcwon.mp3")
                mixer.music.play()
                root2=Toplevel()
                root2.config(bg="black")
                root2.geometry("500x400+140+30")
                root2.title("You won 100,000,000 pounds")
                imgLabel=Label(root2,image=centerImage,bd=0)
                imgLabel.pack(pady=30)

                winLabel=Label(root2, text="You Won",font=("arial", 40, "bold",), bg='black', fg="white")
                winLabel.pack()

                playagainButton=Button(root2, text="Play Again",font=("arial",20,"bold"),bg="black", fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=playagain)
                playagainButton.pack()

                closeButton=Button(root2, text="Close",font=("arial",20,"bold"),bg="black", fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=close)
                closeButton.pack()

                
                happyimage=PhotoImage(file="happy.png")
                happyLabel=Label(root2,image=happyimage,bg="black")
                happyLabel.place(x=30,y=280)
                    
                happyLabel1=Label(root2,image=happyimage,bg="black")
                happyLabel1.place(x=400,y=280)
               
                #sadimage = PhotoImage(file="sad.png")
                #sadLabel1=Label(root2,image=sadimage,bg="black")
              #  sadLabel1.place(x=400,y=280)
                root2.mainloop()
                break
            questionArea.delete(1.0,END)
            questionArea.insert(END,question[i+1])
            optionButton1.config(text=First_options[i+1])
            optionButton2.config(text=Second_options[i+1])
            optionButton3.config(text=Third_options[i+1])
            optionButton4.config(text=Fourth_options[i+1])
            amountLabel.configure(image=amountImages[i])
            amountLabel.image = amountImages[i]  # This line is important to prevent the image from being garbage collected

            #amountLabel.config(image=amountImage[i])
            #image = PhotoImage(file=amountImage[i])
           #amountLabel.config(image=image)
            #amountLabel.image = image  # This line is important to prevent the image from being garbage collected


        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
            def tryagain():
                lifeline50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audiencePole)
                phoneLifeLineButton.config(state=NORMAL,image=phoneImage)
                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,question[0])
                optionButton1.config(text=First_options[0])
                optionButton2.config(text=Second_options[0])
                optionButton3.config(text=Third_options[0])
                optionButton4.config(text=Fourth_options[0])
                amountLabel.config(image=amountImages[0])
          #  load_new_questions()
            
            
            root1=Toplevel()
            root1.config(bg="black")
            root1.geometry("500x400+140+30")
            root1.title("You won 0 pounds")
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loseLabel=Label(root1, text="You lose",font=("arial", 40, "bold",), bg='black', fg="white")
            loseLabel.pack()

            tryagainButton=Button(root1, text="Try Again",font=("arial",20,"bold"),bg="black", fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=tryagain)
            tryagainButton.pack()

            closeButton=Button(root1, text="Close",font=("arial",20,"bold"),bg="black", fg="white",activebackground="black",activeforeground="white",bd=0,cursor="hand2",command=close)
            closeButton.pack()

            sadimage=PhotoImage(file="sad.png")
            sadLabel=Label(root1,image=sadimage,bg="black")
            sadLabel.place(x=30,y=280)
                
            sadLabel1=Label(root1,image=sadimage,bg="black")
            sadLabel1.place(x=400,y=280)
            root1.mainloop()
            break



#=========================Function to do 50 50 ======================================================#
def lifeline50():
    lifeline50Button.config(image=image50X,state=DISABLED)
    if questionArea.get(1.0,"end-1c")==question[0]:
       optionButton2.config(text='')
       optionButton4.config(text="")
    if questionArea.get(1.0,"end-1c")==question[1]:
       optionButton1.config(text='')
       optionButton2.config(text="")
    if questionArea.get(1.0,"end-1c")==question[2]:
       optionButton1.config(text="")
       optionButton4.config(text="")
    if questionArea.get(1.0,"end-1c")==question[3]:
       optionButton2.config(text="")
       optionButton4.config(text="")
    if questionArea.get(1.0,"end-1c")==question[4]:
       optionButton1.config(text="")
       optionButton3.config(text="")
    if questionArea.get(1.0,"end-1c")==question[5]:
       optionButton2.config(text="")
       optionButton4.config(text="")
    if questionArea.get(1.0,"end-1c")==question[6]:
       optionButton1.config(text="")
       optionButton3.config(text="")
    if questionArea.get(1.0,"end-1c")==question[7]:
       optionButton1.config(text="")
       optionButton3.config(text="")
    if questionArea.get(1.0,"end-1c")==question[8]:
       optionButton2.config(text="")
       optionButton4.config(text="")
    if questionArea.get(1.0,"end-1c")==question[9]:
       optionButton1.config(text="")
       optionButton3.config(text="")
    if questionArea.get(1.0,"end-1c")==question[10]:
       optionButton1.config(text="")
       optionButton2.config(text="")
    if questionArea.get(1.0,"end-1c")==question[11]:
       optionButton3.config(text="")
       optionButton4.config(text="")
    if questionArea.get(1.0,"end-1c")==question[12]:
       optionButton1.config(text="")
       optionButton4.config(text="")
    if questionArea.get(1.0,"end-1c")==question[13]:
       optionButton1.config(text="")
       optionButton3.config(text="")
    if questionArea.get(1.0,"end-1c")==question[14]:
       optionButton2.config(text="")
       optionButton4.config(text="")
   
   

   
   
   
   
   
   
    #lifeline50Button.config(image=image50X,state=DISABLED)
    #current_question_text = questionArea.get(1.0, "end-1c")

    # Check if the current question is in the shuffled list
   # if current_question_text in question:
    #    current_question_index = question.index(current_question_text)

        # Get the correct answer for the current question
     #   correct_answer = correct_answers[current_question_index]

        # Get the options for the current question
     #   current_options = [
     #       First_options[current_question_index],
     #       Second_options[current_question_index],
      #      Third_options[current_question_index],
     #       Fourth_options[current_question_index]
       # ]

        # Find the index of the correct answer
       # correct_index = current_options.index(correct_answer)

        # Create a list of incorrect indices
       # incorrect_indices = [i for i in range(4) if i != correct_index]

        # Randomly choose two incorrect indices to hide
     #   indices_to_hide = random.sample(incorrect_indices, 2)

     #   # Hide the chosen incorrect options
      #  for index, option_button in enumerate([optionButton1, optionButton2, optionButton3, optionButton4]):
     #       if index in indices_to_hide:
       #         option_button.config(text="")
#====================================Function to Load Audience Pole)
#def audiencePoleLifeLine():
# ... (previous code)

# Assuming option_mapping is a dictionary mapping options to progress bar labels

#option_mapping = {"A": progressBarA, "B": progressbarLabelB, "C": progressbarLabelC, "D": progressbarLabelD}
#function for audience lifeline
def audiencePoleLifeLine():
    audiencePoleButton.config(image=audiencePoleX, state=DISABLED)
    progressBarA.place(x=580, y=190)
    progressBarB.place(x=620, y=190)
    progressBarC.place(x=660, y=190)
    progressBarD.place(x=700, y=190)

    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)
 #Audiencepole progress loop    
    if questionArea.get(1.0,"end-1c")==question[0]:
       progressBarA.config(value=30)
       progressBarB.config(value=50)
       progressBarC.config(value=90)
       progressBarD.config(value=60)
    if questionArea.get(1.0,"end-1c")==question[1]:
       progressBarA.config(value=30)
       progressBarB.config(value=50)
       progressBarC.config(value=70)
       progressBarD.config(value=40)
    if questionArea.get(1.0,"end-1c")==question[2]:
       progressBarA.config(value=20)
       progressBarB.config(value=70)
       progressBarC.config(value=40)
       progressBarD.config(value=30)
    if questionArea.get(1.0,"end-1c")==question[3]:
       progressBarA.config(value=70)
       progressBarB.config(value=20)
       progressBarC.config(value=40)
       progressBarD.config(value=50)
    if questionArea.get(1.0,"end-1c")==question[4]:
       progressBarA.config(value=20)
       progressBarB.config(value=30)
       progressBarC.config(value=40)
       progressBarD.config(value=70)
    if questionArea.get(1.0,"end-1c")==question[5]:
       progressBarA.config(value=70)
       progressBarB.config(value=40)
       progressBarC.config(value=20)
       progressBarD.config(value=10)
    if questionArea.get(1.0,"end-1c")==question[6]:
       progressBarA.config(value=40)
       progressBarB.config(value=60)
       progressBarC.config(value=30)
       progressBarD.config(value=50)
    if questionArea.get(1.0,"end-1c")==question[7]:
       progressBarA.config(value=10)
       progressBarB.config(value=60)
       progressBarC.config(value=40)
       progressBarD.config(value=30)
    if questionArea.get(1.0,"end-1c")==question[8]:
       progressBarA.config(value=20)
       progressBarB.config(value=40)
       progressBarC.config(value=70)
       progressBarD.config(value=50)
    if questionArea.get(1.0,"end-1c")==question[9]:
       progressBarA.config(value=30)
       progressBarB.config(value=70)
       progressBarC.config(value=50)
       progressBarD.config(value=20)
    if questionArea.get(1.0,"end-1c")==question[10]:
       progressBarA.config(value=20)
       progressBarB.config(value=50)
       progressBarC.config(value=70)
       progressBarD.config(value=30)
    if questionArea.get(1.0,"end-1c")==question[11]:
       progressBarA.config(value=20)
       progressBarB.config(value=70)
       progressBarC.config(value=50)
       progressBarD.config(value=40)
    if questionArea.get(1.0,"end-1c")==question[12]:
       progressBarA.config(value=20)
       progressBarB.config(value=70)
       progressBarC.config(value=40)
       progressBarD.config(value=50)
    if questionArea.get(1.0,"end-1c")==question[13]:
       progressBarA.config(value=20)
       progressBarB.config(value=70)
       progressBarC.config(value=30)
       progressBarD.config(value=40)
    if questionArea.get(1.0,"end-1c")==question[14]:
       progressBarA.config(value=20)
       progressBarB.config(value=40)
       progressBarC.config(value=70)
       progressBarD.config(value=50)

def phoneLifeLine():
   mixer.music.load("calling.mp3")
   mixer.music.play()
   callButtton.place(x=70,y=260)
   phoneLifeLineButton.config(image=phoneImageX,state=DISABLED)

   
# ... (remaining code)
    #if questionArea.get(1.0, "end-1c") == question[0]:
    #    progressBarA.config(value=30)
    #    progressBarB.config(value=50)
    #    progressBarC.config(value=60)
    #    progressBarD.config(value=90)\
#FUNCTION TO CLICK PHONE AND SAY ANSWER
def phoneclick():
    for i in range(15):
       if questionArea.get(1.0,'end-1c')==question[i]:
          engine.say(f"The answer is {correct_answers[i]}")
          engine.runAndWait()
          mixer.init()
          mixer.music.load("kbc.mp3")
          mixer.music.play(-1)
                       
#MUSIC
correct_answers = [
    "Michael Jackson",
    "Mozart",
    "The Beatles",
    "Elvis Presley",
    "Adele",
    "Led Zeppelin",
    "Beethoven",
    "Madonna",
    "Bach",
    "Queen",
    "Johnny Cash",
    "Taylor Swift",
    "Pink Floyd",
    "Stevie Wonder",
    "Beyoncé"
]

question = [
    "Who is known as the 'King of Pop'?",
    "Who composed 'The Magic Flute'?",
    "Which band is often referred to as the 'Fab Four'?",
    "Who is often referred to as the 'King of Rock and Roll'?",
    "Which artist released the album '21'?",
    "Which band released the iconic song 'Stairway to Heaven'?",
    "Who composed 'Für Elise'?",
    "Who is often referred to as the 'Queen of Pop'?",
    "Which composer is known for composing 'Air on the G String'?",
    "Which band sang 'Bohemian Rhapsody'?",
    "Who is known as the 'Man in Black'?",
    "Which artist released the album '1989'?",
    "Which band released the album 'The Dark Side of the Moon'?",
    "Who is often referred to as the 'Prince of Motown'?",
    "Which artist released the album 'Lemonade'?"
]

First_options = [
    "Michael Jackson",
    "Beethoven",
    "The Rolling Stones",
    "Elton John",
    "Beyoncé",
    "Pink Floyd",
    "J.S. Bach",
    "Madonna",
    "Mozart",
    "The Beatles",
    "Johnny Cash",
    "Adele",
    "The Beatles",
    "Stevie Wonder",
    "Rihanna"
]

Second_options = [
    "Elvis Presley",
    "Mozart",
    "The Beatles",
    "Bob Dylan",
    "Taylor Swift",
    "Led Zeppelin",
    "Mozart",
    "Lady Gaga",
    "Beethoven",
    "Led Zeppelin",
    "Elvis Presley",
    "Katy Perry",
    "The Rolling Stones",
    "Marvin Gaye",
    "Britney Spears"
]

Third_options = [
    "Prince",
    "Bach",
    "The Beach Boys",
    "Chuck Berry",
    "Adele",
    "The Eagles",
    "Johann Strauss II",
    "Whitney Houston",
    "Chopin",
    "The Rolling Stones",
    "David Bowie",
    "Ariana Grande",
    "Pink Floyd",
    "Ray Charles",
    "Mariah Carey"
]

Fourth_options = [
    "Stevie Wonder",
    "Beethoven",
    "The Beatles",
    "Elvis Presley",
    "Mariah Carey",
    "AC/DC",
    "Frederic Chopin",
    "Celine Dion",
    "Brahms",
    "Pink Floyd",
    "Johnny Cash",
    "Taylor Swift",
    "Led Zeppelin",
    "B.B. King",
    "Beyoncé"
]


root=Tk()
root.geometry("1270x652+0+0")
root.title("who want to be a millionaire created by Terry.G.")

root.config(bg="black")
#==============================================Frames=====================================#
leftframe=Frame(root,bg = "black",padx=90)
leftframe.grid()

topFrame = Frame(leftframe,bg="black",pady=15)
topFrame.grid()

centerFrame = Frame(leftframe,bg="black",pady=15)
centerFrame.grid(row=1, column=0)

bottomFrame = Frame(leftframe)
bottomFrame.grid(row=2, column=0)

rightframe=Frame(root,pady=25,padx=50,bg="black")
rightframe.grid(row=0, column=1)
#===============================================IMAGES================================================#
image50=PhotoImage(file="50-50.png")
image50X=PhotoImage(file="50-50-X.png")

lifeline50Button = Button(topFrame, image=image50, bg="black",bd=0,activebackground='black',width=180,height=80,command=lifeline50)
lifeline50Button.grid(row=0,column=0)

audiencePoleX=PhotoImage(file="audiencePoleX.png")
audiencePoleButton = Button(topFrame, image=audiencePoleX,bg="black",bd=0,activebackground="black",width=180,height=80,command=audiencePoleLifeLine)
audiencePoleButton.grid(row=0,column=1)

audiencePole=PhotoImage(file="audiencePole.png")
audiencePoleButton = Button(topFrame, image=audiencePole,bg="black",bd=0,activebackground="black",width=180,height=80,command=audiencePoleLifeLine)
audiencePoleButton.grid(row=0,column=1)

phoneImage=PhotoImage(file="phoneAFriend.png")
phoneImageX=PhotoImage(file="phoneAFriendX.png")

phoneLifeLineButton = Button(topFrame,image=phoneImage,bg="black",bd=0,activebackground='black',width=180,height=80,command=phoneLifeLine)
phoneLifeLineButton.grid(row=0,column=2)

callimage=PhotoImage(file="phone.png")
callButtton=Button(root,image=callimage,bd=0,bg="black",activebackground="black",cursor="hand2", command=phoneclick)

centerImage= PhotoImage(file="center.png")
logoLabel=Label(centerFrame, image=centerImage,bg="black",width=300,height=200)
logoLabel.grid()

amountImage=PhotoImage(file="Picture0.png")
amountImage1=PhotoImage(file="Picture1.png")
amountImage2=PhotoImage(file="Picture2.png")
amountImage3=PhotoImage(file="Picture3.png")
amountImage4=PhotoImage(file="Picture4.png")
amountImage5=PhotoImage(file="Picture5.png")
amountImage6=PhotoImage(file="Picture6.png")
amountImage7=PhotoImage(file="Picture7.png")
amountImage8=PhotoImage(file="Picture8.png")
amountImage9=PhotoImage(file="Picture9.png")
amountImage10=PhotoImage(file="Picture10.png")
amountImage11=PhotoImage(file="Picture11.png")
amountImage12=PhotoImage(file="Picture12.png")
amountImage13=PhotoImage(file="Picture13.png")
amountImage14=PhotoImage(file="Picture14.png")
amountImage15=PhotoImage(file="Picture15.png")

amountImages = [amountImage1, amountImage2, amountImage3, amountImage4, amountImage5,
                amountImage6, amountImage7, amountImage8, amountImage9, amountImage10,
                amountImage11, amountImage12, amountImage13, amountImage14, amountImage15]
amountLabel=Label(rightframe,image=amountImage,bg="black")
amountLabel.grid()

LayoutImage=PhotoImage(file="lay.png")
LayoutLabel=Label(bottomFrame, image=LayoutImage,bg="black")
LayoutLabel.grid()
#shufffle the questions and corresponding options
#questions_and_options = list(zip(question, First_options, Second_options, Third_options, Fourth_options, correct_answers))
#random.shuffle(questions_and_options)

# Unpack the shuffled values
#question, First_options, Second_options, Third_options, Fourth_options, correct_answers = zip(*questions_and_options)
##shuffled_data = list(zip(shuffled_questions, shuffled_options, correct_answers))
#random.shuffle(shuffled_data)
#shuffled_questions, shuffled_options, correct_answers = zip(*shuffled_data)

#=============================================QUESTION AREA==========================================#
questionArea=Text(bottomFrame, font=("arial",18,"bold"),width=34,height=2,wrap="word",bg="black",fg="white",bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,question[0])

labelA = Label(bottomFrame,font=("arial",16,"bold"), text="A: ", bg="black", fg="white",)
labelA.place(x=60,y=110)

optionButton1=Button(bottomFrame, text= First_options[0],font=("arial",16,"bold"),bg="black", fg="white",bd=0,activebackground="black",activeforeground='white',cursor="hand2",wraplength=130)#width=20)
#optionButton1 = Button(bottomFrame, text=First_options[0], font=("arial", 18, "bold"), bg="black", fg="white",
                     #  bd=0, activebackground="black", activeforeground='white', cursor="hand2",
                     #  command=lambda: show_full_text(First_options[0]), wraplength=200)
optionButton1.place(x=100, y=100)

labelB = Label(bottomFrame,font=("arial",15,"bold"), text="B: ", bg="black", fg="white",)
labelB.place(x=330,y=110)
optionButton2=Button(bottomFrame, text= Second_options[0],font=("arial",15,"bold"),bg="black", fg="white",bd=0,activebackground="black",activeforeground='white',cursor="hand2",wraplength=130)#idth=20)
optionButton2.place(x=370, y=100)

labelC = Label(bottomFrame,font=("arial",16,"bold"), text="C: ", bg="black", fg="white",)
labelC.place(x=60,y=190)
optionButton3=Button(bottomFrame, text= Third_options[0],font=("arial",15,"bold"),bg="black", fg="white",bd=0,activebackground="black",activeforeground='white',cursor="hand2",wraplength=130)#,wraplength=200,width=20)
optionButton3.place(x=100, y=180)
labelD = Label(bottomFrame,font=("arial",16,"bold"), text="D: ", bg="black", fg="white",)
labelD.place(x=330,y=190)
optionButton4=Button(bottomFrame, text= Fourth_options[0],font=("arial",15,"bold"),bg="black", fg="white",bd=0,activebackground="black",activeforeground='white',cursor="hand2",wraplength=130)#width=20)
optionButton4.place(x=370, y=180)
#===========================Progress Bar(AUDIENCE POLL BUTTONS AND LABEL)=================================#
progressBarA=Progressbar(root,orient=VERTICAL,length=120)
progressBarB=Progressbar(root,orient=VERTICAL,length=120)
progressBarC=Progressbar(root,orient=VERTICAL,length=120)
progressBarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarLabelA=Label(root, text="A", font=("arial",20,"bold"),bg='black', fg="white")
progressbarLabelB=Label(root, text="B", font=("arial",20,"bold"),bg='black', fg="white")
progressbarLabelC=Label(root, text="C", font=("arial",20,"bold"),bg='black', fg="white")
progressbarLabelD=Label(root, text="D", font=("arial",20,"bold"),bg='black', fg="white")
#option_mapping = {"A": progressBarA, "B": progressbarLabelB, "C": progressbarLabelC, "D": progressbarLabelD}
#correct_answer=StringVar()



#=======================================OPTION FUNCTION==================================================#
optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)



root.mainloop()


