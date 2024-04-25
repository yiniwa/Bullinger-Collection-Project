import openai
import re
import os
import xml.etree.ElementTree as ET
import csv

# Set OpenAI API key
openai.api_key = ''

# Define the directories
path = './Bullinger_letters_volumes_10_to_20/14/'
outfile_path = './output14/'
output_csv_file = 'output14.csv'

os.makedirs(outfile_path, exist_ok=True)

# Function to process each file


def process_file(filename):
    my_tree = ET.parse(path + filename)
    meta_info_sender = ''
    meta_info_addressee = ''

    # Extract sender information
    for x in my_tree.iter('sender'):
        meta_info_sender += '<sender-id>' + x[0].attrib['id']
        if x[0].tag == 'person':
            meta_info_sender += ' <firstname>' + x[0][1].text
            meta_info_sender += ' <name>' + x[0][0].text + '\n'
        else:
            meta_info_sender += ' ' + x[0].tag + ': ' + x[0].text + '\n'

    # Extract addressee information
    for x in my_tree.iter('addressee'):
        meta_info_addressee += '<addressee-id>' + x[0].attrib['id']
        if x[0].tag == 'person':
            meta_info_addressee += ' <firstname>' + x[0][1].text
            meta_info_addressee += ' <name>' + x[0][0].text + '\n'
        else:
            meta_info_addressee += ' ' + x[0].tag + ': ' + x[0].text

    XML_infile = open(path + filename, 'r')
    sent_list = []

    for line in XML_infile:
        if re.search('<s ', line):
            sent_list.append(line)
        if re.search('</letter>', line):
            break

    XML_infile.close()

    my_content = 'Translate the following Latin text to English. Preserve the XML tags.\n'
    my_sentences = ''
    for sent in sent_list[-10:]:
        my_sentences += sent
    my_match = re.search('([Cc]a?esar)', my_sentences)
    if my_match:
        my_term = my_match.group(1)
        my_content += 'Translate "' + my_term + '" as "emperor".\n'

    my_sentences = re.sub('\t+', '', my_sentences)
    my_sentences = re.sub(' state="auto(_name)?"', '', my_sentences)
    my_sentences = re.sub(' state="(manual|verified)"', '', my_sentences)
    my_sentences = re.sub('<fl[^>]*>\w+</fl>', '', my_sentences)
    my_sentences = re.sub('<ipron>(\w+)</ipron>', '\1', my_sentences)
    my_sentences = re.sub('\[', '', my_sentences)
    my_sentences = re.sub('\]', '', my_sentences)
    my_sentences = re.sub('<lb/>', '', my_sentences)
    my_sentences = re.sub('<pb[^>]+>', '', my_sentences)
# Remove <placeName ref=" "></placeName> tags
    my_sentences = re.sub(
        r'<placeName ref="[^"]*">.*?</placeName>', '', my_sentences)
    my_content += my_sentences

    if len(sent_list) >= 5:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": my_content}
            ]
        )
        translated_text = completion.choices[0].message.content
    else:
        translated_text = "Not enough sentences for translation."

    return filename, meta_info_sender, meta_info_addressee, my_sentences, translated_text


# Write to CSV file
with open(os.path.join(outfile_path, output_csv_file), mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename', 'Sender Info', 'Addressee Info',
                    'Original Text', 'GPT-4 Translation'])

    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            try:
                file_name, sender_info, addressee_info, original_text, translation = process_file(
                    filename)
                writer.writerow(
                    [file_name, sender_info, addressee_info, original_text, translation])
                print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
