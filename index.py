from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot instance with correct logic adapter name
bot = ChatBot("chatbot", read_only=False, logic_adapters=[
    {"import_path":"chatterbot.logic.BestMatch",
     "default_response":"Sorry I don't have an answer",
     "maximum_similarity_threshold":0.9
     }
     ])

# Training data
list_to_train = [
    "hi",
    "hi there",
    "What's your name?",
    "I'm a chatbot",
    "How old are you?",
    "I'm ageless!",
    "Why are you so mad",
    "I'm not!"
    "Do you have an iphone?"
    "I've everything",
    "What's your Favorite food?",
]

# Train the chatbot
trainer = ListTrainer(bot)
trainer.train(list_to_train)

print("Chatbot trained successfully!")

while True:
    user_response= input("User: ")
    print("Chatbot:" + str(bot.get_response(user_response)))