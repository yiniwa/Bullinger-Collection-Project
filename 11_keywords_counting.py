import pandas as pd

# Load the CSV file
df = pd.read_csv('./modified_2.csv')

# Keywords to count
keywords = [
    "brother", "everyone", "all", "friends", "family",
    "household", "mother", "wife", "children", "sister",
]

# Function to count keywords in each column


def count_keywords(column):
    # Create a dictionary to hold the count of each keyword
    counts = {keyword: column.str.contains(r'\b{}\b'.format(
        keyword), case=False, na=False).sum() for keyword in keywords}
    return pd.Series(counts)


sender_keyword_counts = count_keywords(df['predicted_sender'])
receiver_keyword_counts = count_keywords(df['predicted_receiver'])

# Combine the counts into a DataFrame
keyword_counts = pd.DataFrame({
    'Sender Keyword Counts': sender_keyword_counts,
    'Receiver Keyword Counts': receiver_keyword_counts
})

# Save the keyword counts to a CSV file
keyword_counts.to_csv('./keyword_counts.csv')
