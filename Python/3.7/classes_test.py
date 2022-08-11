from tkinter import *
import random

root = Tk()
root.title("Maths Quiz")
root.geometry("800x600")


# Classes
class Page():
    def __init__(self, master):
        self.mainFrame = Frame(master)
        self.mainFrame.place(relx=0, rely=0, relheight=1, relwidth=1)


class StartMenu(Page):
    def __init__(self, master):
        super().__init__(master)
        
        self.title = Label(self.mainFrame, text="Maths Quiz!", font=("Arial", 50, "bold"))
        self.title.place(relx=0.005, rely=0.005, relheight=0.24375, relwidth=0.99)

        self.easyButton = Button(self.mainFrame, text="Easy", font=("Arial", 50, "bold"), bg="#1ade5e", activebackground="#10d16a")
        self.easyButton.place(relx=0.255, rely=0.25375, relheight=0.14375, relwidth=0.49)

        self.mediumButton = Button(self.mainFrame, text="Medium", font=("Arial", 50, "bold"), bg="#dfa71b", activebackground="#d58312")
        self.mediumButton.place(relx=0.255, rely=0.5025, relheight=0.14375, relwidth=0.49)

        self.hardButton = Button(self.mainFrame, text="Hard", font=("Arial", 50, "bold"), bg="#de1c27", activebackground="#d51443")
        self.hardButton.place(relx=0.255, rely=0.75125, relheight=0.14375, relwidth=0.49)



class EasyQuiz(Page):
    def __init__(self, master):
        super().__init__(master)

        global questionVar
        global answerVar
        global score
        global maxQuestions
        global currentQuestion

        # Setup
        self.score = 0
        self.maxQuestions = 10
        self.currentQuestion = 0

        self.mainFrame = Frame(master)
        self.mainFrame.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Quiz
        self.quizFrame = Frame(self.mainFrame)
        self.quizFrame.place(relx=0, rely=0, relheight=1, relwidth=0.5)

        self.questionVar = StringVar(self.quizFrame, self.GetQuestion())
        self.questionLabel = Label(self.quizFrame, textvariable=self.questionVar, font=("Arial", 50, "italic"))
        self.questionLabel.place(relx=0.005, rely=0.005, relheight=0.3266, relwidth=0.99)

        self.answerVar = StringVar(self.quizFrame, "0")
        self.answerLabel = Label(self.quizFrame, textvariable=self.answerVar, font=("Arial", 50, "bold"))
        self.answerLabel.place(relx=0.005, rely=0.3366, relheight=0.3266, relwidth=0.99) 

        self.scoreVar = StringVar(self.quizFrame, "{}/{}".format(self.score, self.maxQuestions))
        self.scoreLabel = Label(self.quizFrame, textvariable=self.scoreVar, font=("Arial", 50, "bold"))
        self.scoreLabel.place(relx=0.005, rely=0.6683, relheight=0.3266, relwidth=0.99)

        # Keypad
        self.keypadFrame = Frame(self.mainFrame, bg="#cccccc", borderwidth=5, relief="ridge")
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

            self.NextScreen()

    def CheckAnswer(self):
        global score
        if int(self.answerVar.get()) == self.added:
            self.score += 1
            self.scoreVar.set("{}/{}".format(self.score, self.maxQuestions))
            self.newQuestion = self.GetQuestion()
            self.questionVar.set(self.newQuestion)
        else:
            self.newQuestion = self.GetQuestion()
            self.questionVar.set(self.newQuestion)

    def NextScreen(self):
        self.mainFrame.destroy()
            

            
app = StartMenu(root)
# Mainloop
root.mainloop()