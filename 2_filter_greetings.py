import csv
import re


def extract_keywords_sentences(text):
    # Define a regex pattern for matching the keywords and their variants
    pattern = r'\b(?:regards|greet|salute?)(s|ing|ed|ings)?\b'
    sentences = re.findall(r'(<s[^>]*>.*?</s>)', text, re.DOTALL)
    extracted = [sentence for sentence in sentences if re.search(
        pattern, sentence, re.IGNORECASE)]
    return extracted


input_file_path = 'output14/output14.csv'
intermediary_file_path = 'output14/output14_extract.csv'
output_csv_path = 'output14/output14_filter.csv'

# First part: Extract sentences and create an intermediary CSV
with open(input_file_path, mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = list(reader)
    header = rows[0]
    data = rows[1:]

header.append('Extracted Sentences')

for row in data:
    translation_text = row[4]
    extracted_sentences = extract_keywords_sentences(translation_text)
    row.append('\n'.join(extracted_sentences))

with open(intermediary_file_path, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(data)

# Second part: Filter rows and create the final CSV
with open(intermediary_file_path, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows_to_write = [
        row for row in reader if row['Extracted Sentences'].strip()]

with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
    if rows_to_write:
        writer = csv.DictWriter(outfile, fieldnames=rows_to_write[0].keys())
        writer.writeheader()
        writer.writerows(rows_to_write)
