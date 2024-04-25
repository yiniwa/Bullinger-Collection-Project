import pandas as pd

# Load the CSV file
df = pd.read_csv('./modified_2.csv')

# Function to extract identifiers and their corresponding names


def extract_identifiers_and_names(column):
    # Regular expression to match 'Name Surname_ID' and capture both parts
    pattern = r'(\b\w+\s+\w+)_(\d+)\b'
    # Extract matches using the regex pattern with capture groups for the name and identifier
    matches = column.str.extractall(pattern)
    # Rename columns for clarity
    matches.columns = ['Name', 'Identifier']
    return matches


# Extract from both columns
sender_matches = extract_identifiers_and_names(df['predicted_sender'])
receiver_matches = extract_identifiers_and_names(df['predicted_receiver'])

# Aggregate names associated with each identifier, separating multiple names with new lines


def aggregate_names(group):
    return '\n'.join(group.unique())


# Group by identifier and aggregate names
sender_aggregated = sender_matches.groupby(
    'Identifier')['Name'].apply(aggregate_names)
receiver_aggregated = receiver_matches.groupby(
    'Identifier')['Name'].apply(aggregate_names)

# Combine the counts into a DataFrame
combined_counts = pd.DataFrame({
    'Sender Identifier Counts': sender_matches['Identifier'].value_counts(),
    'Sender Names': sender_aggregated,
    'Receiver Identifier Counts': receiver_matches['Identifier'].value_counts(),
    'Receiver Names': receiver_aggregated
})

# Fill NaN values with 0 for counts and an empty string for names if any
combined_counts.fillna({'Sender Identifier Counts': 0, 'Receiver Identifier Counts': 0,
                       'Sender Names': '', 'Receiver Names': ''}, inplace=True)

# Save the combined counts to a CSV file
combined_counts.to_csv('./identifier_and_names_counts.csv',
                       index=True, index_label='Identifier')
