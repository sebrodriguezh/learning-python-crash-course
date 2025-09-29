def show_messages(messages):
    """Display every message from a list"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Display each text message and
    move each message to a new list"""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

# Dummy list of messages
messages = [
    "Hello, how are you?",
    "Python is awesome!",
    "Learning functions is fun",
    "Keep coding!",
    "Practice makes perfect"
]

sent_messages = []

show_messages(messages)
send_messages(messages[:], sent_messages)
print(sent_messages)
print(messages)
