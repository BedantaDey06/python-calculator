from chatterbot import ChatBot

# I name the bot "Calculator", because well, he is a calculator
# Kinda big brain TBH, using Mathematical AI to run calculations
# The calculator AI will NOT learn from User Input, what if you teach him some bad stuff?
Bot = ChatBot(name = 'Calculator',
                read_only = True,                  
                logic_adapters = ["chatterbot.logic.MathematicalEvaluation"],                 
                storage_adapter = "chatterbot.storage.SQLStorageAdapter")
    

# Clearing the screen and running the actual program
print('\033c')
print("Calculator bot developed by Bedanta. Enter a command or type 'exit' to quit.")
while (True):
    # Taking input from the user
    user_input = input("Type a command: ")
    
    # Check if the user has typed exit, to well, exit the program 
    if user_input.lower() == 'exit':
        print("Eliminating process, exiting the program...")
        break

    # Easter egg ooh, let's make the bot feel nice
    if user_input.lower() == 'nice':
        print("Calculator: Thanks! NOW YOU MUST RESTART ME, MWAHAHAHA!")
        break
    
    # Help section for people who have smol brain, unlike the bot and... me of course.
    if user_input.lower() == 'help':
        print("1. Do include spaces between operators and numbers.")
        print("2. Try using simple language while calculating.")
        print("3. Multiplying is phrased as 'times'.")
        print("4. Division is phrased as 'divided by'.")
        print("5. Addition and subtraction are phrased as 'plus' and 'minus' respectively.")
        print("RESTART THE PROGRAM TO CONTINUE.")
        break
        

    # Otherwise, evaluate the user input
    # Print the infamous invalid input dialog to annoy the user
    try:
        response = Bot.get_response(user_input)
        print("Calculator:", response)
    except:
        print("Calculator: Sorry, didn't catch that. Try again.")