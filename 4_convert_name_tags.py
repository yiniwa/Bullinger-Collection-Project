import pandas as pd
import re

file_path = 'output14/output14_clean.csv'
df = pd.read_csv(file_path)

# Function to replace <persName ref="ID">Name</persName> with Name_ID


def replace_name_tag(text):
    return re.sub(r'<persName ref="(\d+)">(.+?)</persName>', r'\2_\1', text)


# Apply the function to the 'Extracted Sentences' column
df['Extracted Sentences'] = df['Extracted Sentences'].apply(replace_name_tag)

# Save the modified DataFrame back to CSV
df.to_csv('output14/output14_tags.csv', index=False)
