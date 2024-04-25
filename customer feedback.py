from breezypythongui import EasyFrame

class PrompterBoxDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Feedback Counter", width=300, height=100)
        self.label = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        self.addButton(text="Feedback", row=1, column=0, command=self.getFeedback)
    
    def getFeedback(self):
        feedback = self.prompterBox(title="Customer Feedback", promptString="Drop your feedbacks here!")
        if feedback:
            with open("feedback.txt", "a") as file:  
                file.write(feedback + "\n")  #add the feedbacks to feedback.txt
            self.label["text"] = "Thank you for your feedback!"  

if __name__ == "__main__":
    PrompterBoxDemo().mainloop()
