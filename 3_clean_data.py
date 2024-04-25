import csv
import re


def split_sentences(text):
    # Split the text into sentences based on newline character
    return text.split('\n') if text else []


def clean_sentence(sentence):
    # Remove <s n=...> and </s> tags
    return re.sub(r'<s[^>]*>|</s>', '', sentence)


input_file_path = 'output14/output14_filter.csv'
output_csv_path = 'output14/output14_clean.csv'

# Read the original CSV file
with open(input_file_path, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    new_rows = []

    for row in reader:
        # Split the 'Extracted Sentences' into individual sentences
        sentences = split_sentences(row.get('Extracted Sentences', ''))

        # Create a new row for each sentence
        for sentence in sentences:
            # Clean up the sentence
            cleaned_sentence = clean_sentence(sentence)

            # Copy the original row but remove unwanted columns and update 'Extracted Sentences'
            new_row = {k: v for k, v in row.items() if k not in [
                'Original Text', 'GPT-4 Translation']}
            new_row['Extracted Sentences'] = cleaned_sentence
            new_rows.append(new_row)

# Write the updated data to the output CSV file
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
    if new_rows:
        writer = csv.DictWriter(outfile, fieldnames=new_rows[0].keys())
        writer.writeheader()
        writer.writerows(new_rows)
