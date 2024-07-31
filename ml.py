

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# Define intents and responses
intents = {
    'greeting': ['hi', 'hello', 'hey', 'hello there', 'hi there', 'hey there'],
    'farewell': ['bye', 'see you later', 'goodbye', 'bye bye', 'see you soon'],
    'help': ['help', 'what can you do', 'options', 'commands'],
    'hours': ['hours', 'what time do you open', 'what time do you close'],
    'products': ['products', 'what do you sell', 'what do you offer'],
    'contact': ['contact', 'get in touch', 'email', 'phone number']
}

responses = {
    'greeting': 'Hello! Welcome to our business. How can I assist you today? 😊',
    'farewell': 'Goodbye! Thank you for visiting. Have a great day! 👋',
    'help': 'I can help with hours, products, contact information, and more. What do you need? 🤔',
    'hours': 'We are open from 9am to 5pm, Monday through Friday.',
    'products': 'We offer a wide range of products, including [list your products].',
    'contact': 'You can reach us at [email address] or [phone number].'
}

# Define a function to process user input
def process_input(user_input):
    user_input = user_input.lower()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                return responses[intent]
    return "I didn't understand that. Please try again."

# Create a simple chat loop
while True:
    user_input = input("You: ")
    response = process_input(user_input)
    print("Chatbot:", response)

    # Add a farewell message when the user says goodbye
    if user_input.lower() in intents['farewell']:
        print("Chatbot: It was nice chatting with you!")
        break


