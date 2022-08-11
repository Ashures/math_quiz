from tkinter import *
import random

# Classes
class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        mainFrame = Frame(self)

        mainFrame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.pageList = {}

        for page in (StartMenu, EasyQuiz):

            frame = page(mainFrame, self)

            self.pageList[page] = frame

            frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.ShowPage(StartMenu)

    def ShowPage(self, cont):

        page = self.pageList[cont]
        page.Reset()
        page.tkraise()


class StartMenu(Frame):
    def __init__(self, master, mainFrame):
        Frame.__init__(self, master)
        
        self.title = Label(self, text="Maths Quiz!", font=("Arial", 50, "bold"))
        self.title.place(relx=0.005, rely=0.005, relheight=0.24375, relwidth=0.99)

        self.easyButton = Button(self, text="Easy", font=("Arial", 50, "bold"), bg="#1ade5e", activebackground="#10d16a", command=lambda: mainFrame.ShowPage(EasyQuiz))
        self.easyButton.place(relx=0.255, rely=0.25375, relheight=0.14375, relwidth=0.49)

        self.mediumButton = Button(self, text="Medium", font=("Arial", 50, "bold"), bg="#dfa71b", activebackground="#d58312")
        self.mediumButton.place(relx=0.255, rely=0.5025, relheight=0.14375, relwidth=0.49)

        self.hardButton = Button(self, text="Hard", font=("Arial", 50, "bold"), bg="#de1c27", activebackground="#d51443")
        self.hardButton.place(relx=0.255, rely=0.75125, relheight=0.14375, relwidth=0.49)

    def Reset(self):
        pass

        



class EasyQuiz(Frame):
    def __init__(self, master, mainFrame):
        Frame.__init__(self, master)

        # Menu
        self.menuFrame = Frame(self)
        self.menuFrame.place(relx=0, rely=0.6666, relheight=0.3334, relwidth=0.5)

        self.menuButton = Button(self.menuFrame, text="Main Menu", font=("Arial", 50, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: mainFrame.ShowPage(StartMenu))
        self.menuButton.place(relx=0.055, rely=0.1, relheight=0.5, relwidth=0.89) 

        # Setup 
        self.RunQuiz()

    def RunQuiz(self):
        global questionVar
        global answerVar
        global score
        global maxQuestions
        global currentQuestion

        # Setup
        self.score = 0
        self.maxQuestions = 10
        self.currentQuestion = 0

        # Quiz
        self.quizFrame = Frame(self)
        self.quizFrame.place(relx=0, rely=0, relheight=0.6666, relwidth=0.5)

        self.questionVar = StringVar(self.quizFrame, self.GetQuestion())
        self.questionLabel = Label(self.quizFrame, textvariable=self.questionVar, font=("Arial", 50, "italic"))
        self.questionLabel.place(relx=0.005, rely=0.005, relheight=0.445, relwidth=0.99)

        self.answerVar = StringVar(self.quizFrame, "0")
        self.answerLabel = Label(self.quizFrame, textvariable=self.answerVar, font=("Arial", 50, "bold"))
        self.answerLabel.place(relx=0.005, rely=0.455, relheight=0.445, relwidth=0.99) 

        self.scoreVar = StringVar(self.quizFrame, "Score: {}/{}".format(self.score, self.maxQuestions))

        # Keypad
        self.keypadFrame = Frame(self, bg="#cccccc", borderwidth=5, relief="ridge")
        self.keypadFrame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        self.button1 = Button(self.keypadFrame, text="1", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(1))
        self.button1.place(relx=0.005, rely=0.005, relheight=0.24375, relwidth=0.3266)
        self.button2 = Button(self.keypadFrame, text="2", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(2))
        self.button2.place(relx=0.3366, rely=0.005, relheight=0.24375, relwidth=0.3266)
        self.button3 = Button(self.keypadFrame, text="3", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(3))
        self.button3.place(relx=0.6683, rely=0.005, relheight=0.24375, relwidth=0.3266)
        self.button4 = Button(self.keypadFrame, text="4", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(4))
        self.button4.place(relx=0.005, rely=0.25375, relheight=0.24375, relwidth=0.3266)
        self.button5 = Button(self.keypadFrame, text="5", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(5))
        self.button5.place(relx=0.3366, rely=0.25375, relheight=0.24375, relwidth=0.3266)
        self.button6 = Button(self.keypadFrame, text="6", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(6))
        self.button6.place(relx=0.6683, rely=0.25375, relheight=0.24375, relwidth=0.3266)
        self.button7 = Button(self.keypadFrame, text="7", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(7))
        self.button7.place(relx=0.005, rely=0.5025, relheight=0.24375, relwidth=0.3266)
        self.button8 = Button(self.keypadFrame, text="8", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(8))
        self.button8.place(relx=0.3366, rely=0.5025, relheight=0.24375, relwidth=0.3266)
        self.button9 = Button(self.keypadFrame, text="9", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(9))
        self.button9.place(relx=0.6683, rely=0.5025, relheight=0.24375, relwidth=0.3266)
        self.button0 = Button(self.keypadFrame, text="0", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=lambda: self.SetAnswer(0))
        self.button0.place(relx=0.3383, rely=0.75125, relheight=0.24375, relwidth=0.3266 )
        self.buttonEquals = Button(self.keypadFrame, text="=", font=("Arial", 40, "bold"), bg="#1bcae0", activebackground="#14a6d7", command=self.CheckAnswer)
        self.buttonEquals.place(relx=0.6683, rely=0.75125, relheight=0.24375, relwidth=0.3266)
        self.buttonClear = Button(self.keypadFrame, text="C", font=("Arial", 40, "bold"), bg="#d5253d", activebackground="#c61a5b", command=lambda: self.SetAnswer("clear"))
        self.buttonClear.place(relx=0.005, rely=0.75125, relheight=0.24375, relwidth=0.3266)

    def SetAnswer(self, input):
        if input == "clear":
            self.answerVar.set("0")
            return
        if self.answerVar.get() == "0":
            self.answerVar.set(input)
        else:
            currentAnswer = self.answerVar.get()
            currentAnswer += str(input)
            self.answerVar.set(currentAnswer)

    def GetQuestion(self):
        global added
        global currentQuestion
        if self.currentQuestion < self.maxQuestions:
            self.number1 = random.randint(1, 10)
            self.number2 = random.randint(1, 10)
            self.added = self.number1 + self.number2
            self.currentQuestion += 1
            self.nextQuestion = "{}. {} + {} = ?".format(self.currentQuestion, self.number1, self.number2)
            return self.nextQuestion
        else: 
            self.quizFrame.destroy()
            self.LoadFinish()
            

    def CheckAnswer(self):
        global score
        if int(self.answerVar.get()) == self.added:
            self.answerVar.set("0")
            self.score += 1
            self.scoreVar.set("Score: {}/{}".format(self.score, self.maxQuestions))
            self.newQuestion = self.GetQuestion()
            self.questionVar.set(self.newQuestion)
        else:
            self.answerVar.set("0")
            self.newQuestion = self.GetQuestion()
            self.questionVar.set(self.newQuestion)

    def LoadFinish(self):
        self.finishFrame = Frame(self)
        self.finishFrame.place(relx=0, rely=0, relheight=0.6666, relwidth=0.5)
        
        self.quizFinsihLabel = Label(self.finishFrame, text="Game Over!", font=("Arial", 50, "italic"))
        self.quizFinsihLabel.place(relx=0.005, rely=0.005, relheight=0.495, relwidth=0.99)

        self.scoreVar = StringVar(self.finishFrame, "Final Score: {}/{}".format(self.score, self.maxQuestions))
        self.scoreLabel = Label(self.finishFrame, textvariable=self.scoreVar, font=("Arial", 40, "bold"))
        self.scoreLabel.place(relx=0.005, rely=0.505, relheight=0.495, relwidth=0.99)

    def Reset(self):
        self.RunQuiz()
        app.update()

            
app = App()
app.title("Maths Quiz!")
app.geometry("1000x600")
# Mainloop
app.mainloop()