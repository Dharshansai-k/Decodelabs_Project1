#Rule-Based AI Chatbot
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you?": "I'm just a chatbot, but I'm here to help you!",
    "what is your name?": "I am a Rule-Based AI Chatbot.",
    "bye": "Goodbye! Have a great day!",
    "good morning": "Good Morning! Hope you have a productive day.",
    "thanks": "You're welcome!"
}
print("Welcome to the Rule-Based AI Chatbot! Type 'bye' to exit.")

while True:
    ui=input("You: ")
    #Input Sanitization
    user_input = ui.lower().strip()
    if user_input in ["exit", "quit","bye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    response = responses.get(user_input, "I'm sorry, I don't understand that.")

    print("Chatbot:", response)
    

