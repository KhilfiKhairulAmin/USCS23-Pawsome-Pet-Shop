from breezypythongui import EasyFrame

class PrompterBoxDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Feedback Counter", width=300, height=100)
        self.label = self.addLabel(text="", row=0, column=0, sticky="NSEW")
        self.addButton(text="Feedback", row=1, column=0, command=self.getFeedback)
        self.feedback_list = [] #to store products
    
    def getFeedback(self):
        feedback = self.prompterBox(title="Customer Feedback", promptString="Drop your feedbacks here!")
        if feedback:
            self.feedback_list.append(feedback)
            self.label["text"] = "Thank you for your feedback!"  
    
    def saveFeedback(self):
        with open("db/feedback.txt", 'a') as file: 
            file.write(",".join(self.feedback_list) + " , ")
        self.feedback_list = [] #empty the list again

if __name__ == "__main__":
    app = PrompterBoxDemo()
    app.mainloop()
    app.saveFeedback()