
# Casually talk with chat bot.

import random

# Predefined responses

responses = [
    "That's interesting!",
    "Tell me more!",
    "I see, go on.",
    "How does that make you feel?",
    "Why do you think that is?",
    "Can you elaborate on that?",
    "That sounds fun!",
    "I understand.",
    "What else?",
]

def get_response(user_input):
    """Generate a response based on user input."""

    # You can add more complex logic here if needed
    
    return random.choice(responses)

def chat():                                                        # Main function to run the chat system.
    print("Welcome to the Chat System! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chat System:Thankyou for chat")
            break
        
        response = get_response(user_input)
        print(f"Chat System: {response}")

if __name__ == "__main__":
    chat()

# This is normal converston with chat bot.
