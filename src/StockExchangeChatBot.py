import tkinter as tk
from tkinter import Menu, Scrollbar
from src.PlaceHolder import PlaceHolder

class StockExchangeChatbot:
    def __init__(self, data):
        self.exchangeDataDict = {exchange["stockExchange"]: exchange["topStocks"] for exchange in data}
        self.levelStack = []

        self.root = tk.Tk()
        self.root.title("Stock Exchange Chatbot")
        self.root.geometry("700x500")

        self.createMenu()
        self.createMessageBox()
        self.createSendButton()
        self.createChatWindow()
        self.createScrollBar()
        self.displaycurrentLevel()

        self.root.mainloop()

    # Method used to create the 2 menu buttons
    def createMenu(self):
        menu = Menu(self.root)
        menu.add_command(label='Menu', command=lambda: self.menuButtonClicked())
        menu.add_command(label='Quit', command=lambda: self.root.destroy())
        self.root.config(menu=menu)

    # Used to create the message box and uses a placeholder feature implemented in the PlaceHolder class
    def createMessageBox(self):
        self.messageBox = PlaceHolder(self.root, bd=1, width=30, height=8, placeholder="Please pick an option.")
        self.messageBox.place(x=10, y=400, height=90, width=580)

    # Creates the arrow button to send the text message
    def createSendButton(self):
        sendButton = tk.Label(self.root, text="➔", font=("Arial", 20), bg="lightgray", padx=10, pady=5, cursor="hand2")
        sendButton.place(x=620, y=420)
        sendButton.bind("<Button-1>", lambda event: self.sendMessage())

    # Creates the Chat window
    def createChatWindow(self):
        self.chatWindow = tk.Text(self.root, bd=0, width=60, height=20)
        self.chatWindow.place(x=10, y=10, height=380, width=670)

        # Configure tags in order to apply formatting for the use and the bot messages
        self.chatWindow.tag_configure("right", justify="right")
        self.chatWindow.tag_configure("botMessage", background="light blue")

        # Stars with the initiation message from the Bot
        self.chatWindow.insert(tk.END, "Hello! Welcome to LSEG. I'm here to help you.\n", "botMessage")
        self.chatWindow.insert(tk.END, "\n")

    # Creates a vertical scrollbar
    def createScrollBar(self):
        scrollbar = Scrollbar(self.root, command=self.chatWindow.yview)
        scrollbar.place(x=680, y=5, height=380)
        self.chatWindow.config(yscrollcommand=scrollbar.set)

    # Function used to display in the window the information from the current level
    def displaycurrentLevel(self):
        if not self.levelStack:
            self.chatWindow.insert(tk.END, "Please select a Stock Exchange:\n", "botMessage")
            for i, exchange in enumerate(self.exchangeDataDict.keys(), start=1):
                self.chatWindow.insert(tk.END, f"{i}. {exchange}\n")
        elif len(self.levelStack) == 1:
            currentLevel = self.levelStack[-1]
            self.chatWindow.insert(tk.END, f"Please select a stock in {currentLevel}:\n", "botMessage")
            for stock in self.exchangeDataDict[currentLevel]:
                self.chatWindow.insert(tk.END, f"{stock['stockName']}\n")
        elif len(self.levelStack) == 2:
            currentLevel = self.levelStack[-1]
            for stock in self.exchangeDataDict[self.levelStack[-2]]:
                if stock['stockName'] == currentLevel:
                    self.chatWindow.insert(tk.END, f"Stock price of {currentLevel} is {stock['price']}$. Please select an option.\n", "botMessage")
                    self.chatWindow.insert(tk.END, 'Main menu\n')
                    self.chatWindow.insert(tk.END, 'Back\n')

    # The method used to retrieve the message from the message box, display it in the window, and send the information related to the current level in the stack to the method that displays the data.
    def sendMessage(self):
        message = self.messageBox.get("1.0", "end-1c").strip()
        self.chatWindow.insert(tk.END, f"{message}\n", "right")
        self.messageBox.delete("1.0", tk.END)
        if message:
            if message.lower() == "main menu":
                if len(self.levelStack) == 0:
                    self.chatWindow.insert(tk.END, "This is the main menu, you can't go back\n", "botMessage")
                else:
                    self.levelStack.clear()
                    self.displaycurrentLevel()
            elif message.lower() == "back":
                if len(self.levelStack) > 0:
                    self.levelStack.pop()
                    self.displaycurrentLevel()
                else:
                    self.chatWindow.insert(tk.END, "This is the main menu, you can't go back\n", "botMessage")
            elif len(self.levelStack) == 0:
                if message in self.exchangeDataDict:
                    self.levelStack.append(message)
                    self.displaycurrentLevel()
                else:
                    self.chatWindow.insert(tk.END, "Invalid exchange stock name. Please select a value from the list.\n", "botMessage")
            elif len(self.levelStack) == 1:
                CurrentExchange = self.levelStack[-1]
                stockNames = [stock["stockName"] for stock in self.exchangeDataDict[CurrentExchange]]
                if message in stockNames:
                    self.levelStack.append(message)
                    self.displaycurrentLevel()
                else:
                    self.chatWindow.insert(tk.END, "Invalid stock name. Please select a value from the list.\n", "botMessage")
            elif len(self.levelStack) == 2:
                self.chatWindow.insert(tk.END, "You have reached the end of available data.\nTo return to the main menu, type 'Main menu' or 'Back' to navigate back.\n","botMessage")
        else:
            self.chatWindow.insert(tk.END, "Please write a message in the message box before sending\n", "botMessage")

    # The method used to clear the stack and display the main menu info
    def menuButtonClicked(self):
        self.messageBox.delete("1.0", tk.END)
        self.messageBox.insert("1.0", "main menu")
        self.sendMessage()

