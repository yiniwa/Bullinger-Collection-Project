import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('/Users/wwendy/Desktop/1.csv')


def process_addressee_info(addressee_info):
    if not isinstance(addressee_info, str):
        return 'Unknown'

    # Use regular expressions to find and replace all occurrences of the specified pattern
    def replace_pattern(match):
        sender_id, title = match.groups()
        return f'title: {title}_{sender_id}'

    # Apply the replacement pattern to the sender_info string
    new_info = re.sub(r'<sender-id>(\d+) title: (\w+)',
                      replace_pattern, addressee_info)

    return new_info


# Apply the function to the 'Sender Info' column
df['Sender Info'] = df['Sender Info'].apply(process_addressee_info)

# Save the result to a new CSV file
df.to_csv('/Users/wwendy/Desktop/1.csv', index=False)
