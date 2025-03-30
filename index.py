from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot instance with correct logic adapter name
bot = ChatBot("chatbot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

# Training data
list_to_train = [
    "hi",
    "hi there",
    "What's your name?",
    "I'm a chatbot",
    "How old are you?",
    "I'm ageless!"
]

# Train the chatbot
trainer = ListTrainer(bot)
trainer.train(list_to_train)

print("Chatbot trained successfully!")
