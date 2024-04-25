import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('/Users/wwendy/Desktop/1.csv')

# lists of keywords related to sender and receiver
sender_keywords = [
    "I", "me", "my", "my name", "our", "us", "we", "All ours", "on my behalf",
    "All of mine", "on behalf of us all", "myself", "in my name", "sender",
    "our people", "all of ours", "all our people", "on my account", "on our behalf"
]
receiver_keywords = [
    "you", "your", "yours"
]


def replace_keywords(text, keywords, replacement_name):
    # Create a regex pattern to find the keywords
    pattern = r'\b(' + '|'.join(keywords) + r')\b'
    # Replace the found keywords with the name from the Sender/Receiver Info
    return re.sub(pattern, replacement_name, text, flags=re.IGNORECASE)


df['predicted_sender'] = df.apply(lambda row: replace_keywords(
    row['predicted_sender'], sender_keywords, row['Sender Info']), axis=1)

df['predicted_sender'] = df.apply(lambda row: replace_keywords(
    row['predicted_sender'], receiver_keywords, row['Addressee Info']), axis=1)

df['predicted_receiver'] = df.apply(lambda row: replace_keywords(
    row['predicted_receiver'], receiver_keywords, row['Addressee Info']), axis=1)

df['predicted_receiver'] = df.apply(lambda row: replace_keywords(
    row['predicted_receiver'], sender_keywords, row['Sender Info']), axis=1)

# Save the modified CSV file
df.to_csv('/Users/wwendy/Desktop/1.csv', index=False)
