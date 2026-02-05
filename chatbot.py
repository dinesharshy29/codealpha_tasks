import re

def basic_chatbot():
    # Predefined rules: Pattern -> Response
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you today?',
        r'how are you': 'I am just a script, but I am doing great! How about you?',
        r'what is your name': 'I am a simple Python chatbot created for the CodeAlpha internship.',
        r'who created you': 'I was created by a developer as part of a Python programming task.',
        r'bye|goodbye|exit': 'Goodbye! Have a great day!',
        r'weather': 'I cannot check the weather yet, but it looks like a great day to code!',
        r'help': 'I can respond to greetings, tell you about myself, or just chat. Try saying "hello"!',
        r'python|code': 'Python is an amazing language! Are you enjoying the CodeAlpha internship?',
    }

    print("--- Simple Rule-Based Chatbot ---")
    print("Type 'bye' to exit the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        # Check for exit command
        if re.search(r'bye|goodbye|exit', user_input):
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        # Find a matching response
        matched = False
        for pattern, response in rules.items():
            if re.search(pattern, user_input):
                print(f"Chatbot: {response}")
                matched = True
                break
        
        if not matched:
            print("Chatbot: I'm sorry, I don't understand that. Could you try rephrasing?")

if __name__ == "__main__":
    basic_chatbot()
