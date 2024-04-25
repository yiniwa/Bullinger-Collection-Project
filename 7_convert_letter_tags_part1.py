import pandas as pd
import re

# Load the CSV file
df = pd.read_csv(
    '/Users/wwendy/Desktop/p.csv')


def process_addressee_info(addressee_info):
    if not isinstance(addressee_info, str):
        return addressee_info
    # Use regular expressions to extract the relevant parts
    addressee_id_match = re.search(r'<sender-id>(\d+)', addressee_info)
    firstname_match = re.search(r'<firstname>([^<]+)', addressee_info)
    name_match = re.search(r'<name>([^<]+)', addressee_info)

    # Check if all parts were found
    if addressee_id_match and firstname_match and name_match:
        # Extract the addressee ID, firstname, and name
        addressee_id = addressee_id_match.group(1)
        firstname = firstname_match.group(1)
        name = name_match.group(1)

        # Format the new string
        return f'{firstname} {name}_{addressee_id}'
    else:
        return addressee_info


df['Sender Info'] = df['Sender Info'].apply(process_addressee_info)

# Save the result to a new CSV file
df.to_csv('/Users/wwendy/Desktop/1.csv', index=False)
