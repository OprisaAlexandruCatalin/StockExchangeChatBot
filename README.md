# StockExchangeChatBot
A ChatBot used to provide information about Stock Exchanges. It has a small interface built in tkinter and functionality that relies on data from an input JSON file.

# Installation
1.Clone the repository
2.Install the tkinter library with 'pip install tk'

# Run 'main.py' to start the application

# Functionality 
1.Graphical user interface - using Tkinter to create a user-friendly interface for the interaction with the chatbot 
2.StockExchange information - display information about different stock exchanges from an input json file 
3.Naviation - you can navigate on each "level" by using the back keyword or the menu button. Also the Quit button will close the app 
4.Placeholder - used a placeholder feature in the messagebox

# Error handling
1. Handling exceptions when the input json file is missing or the file is empty.
2. Checks the json file integrity
3. Each level in the information stack provides its own errors for better understanding. For example, if you are in the main menu and try to press the menu button, you are notified that you are already there. If you send an empty message, you are prompted to write something. If you input a wrong value, it tells you that it's not the correct stock or stock exchange. If you reach the end, it informs you that you can't go any further and suggests the steps you can take next.

# Contribution - online resources are used for the definition of the placeholder class
I used the code snippet from the link https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter on Stack Overflow, which defines the placeholder class, to implement a placeholder in the message box. This makes it easier to visualize the message box for the first time.

# Future Improvements
1.A potential improvement to the code in order to increase the scalability of this project, is to use a JSON file structured in a way that allows for easier iteration through it without having elements with different key names.
2.Additionally, utilizing a while loop instead of predefining only three levels in the levelStack could enhance flexibility.
3.Implementing a spell-checking feature. For example, if the user enters "telsa" instead of "tesla," the chatbot could prompt a message asking if they meant "tesla." If confirmed, the chatbot would proceed to the next level of interaction.
