def simple_chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. You can say hello, ask how I am, or say goodbye.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks!")
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm just a simple bot. I understand greetings and goodbyes.")
    
    print("Chatbot: It was nice talking to you!")

# Start the chatbot
simple_chatbot()