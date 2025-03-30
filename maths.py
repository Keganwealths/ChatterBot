from chatterbot import ChatBot

# Create a chatbot instance
bot = ChatBot(
    "MathBot",
    logic_adapters=["chatterbot.logic.MathematicalEvaluation"]
)

print("___________Math Chatbot___________")

while True:
    user_text = input("Type the math equation that you want to solve (or 'exit' to quit): ")

    if user_text.lower() in ["exit", "quit", "bye"]:
        print("ChatBot: Goodbye!")
        break

    try:
        response =bot.get_response(user_text)
        print("ChatBot:", response)
    except Exception as e:
        print("ChatBot: Sorry, I couldn't process that. Error:", e)