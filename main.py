import yaml
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

from pytz import UTC
"""
Chat Bot Calculator - To run you need to enter an exercise with spaces for example 2 + 2
"""
def chatbotmath():
    bot = ChatBot("Math",
                  logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

    print("----------- Math Chatbot -------------")



    while True:
        message = input("type the math equation that you want to solve:"
                        " OR to end enter 0 ")
        if message.strip() != '0':
            print("Chatbot: " + str(bot.get_response(message)))
        if message.strip() == '0':
            print('ChatBot : Bye')
            break

"""
Chat Bot Text - The words that help the bot speak are within the list_to_train
"""
def chatbotText():

    bot = ChatBot("chatbot", read_only = False,
                logic_adapters=
                [
                      {
                         "import_path":'chatterbot.logic.BestMatch',
                        "default_response": "Sorry I do not know",
                        "maximum_similarity_threshold": 0.9
                    }
                ])


    list_to_train= [
        "hi",
        "hi there",
        "what's your name",
        "i'm chatbot",
        "how old are you",
        "i'm ageless",
        "What do you like to eat?",
        "pizza",
        "where do you live?",
        "USA",
        "Goodbye",
        "byebye"
    ]

    list_trainer = ListTrainer(bot)
    list_trainer.train(list_to_train)



    while True:
        message = input('You:')
        if message.strip()!= 'bye':
            reply = bot.get_response(message)
            print('ChatBot :',reply)
        if message.strip() == 'bye':
            print('ChatBot : Bye')
            break

if __name__ == "__main__":
    print("enter chatbot math or text")
    choice = input()
    if choice.strip() == 'math':
        chatbotmath()
    elif choice.strip()== 'text':
        chatbotText()
    else:
        exit(0)