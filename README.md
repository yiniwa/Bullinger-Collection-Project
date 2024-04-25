# Overview 
The Bullinger Collection text analysis project analyzes historical letters stored in XML format, focusing on extracting, processing, and analyzing greeting information along with linguistic data. This project includes several stages of data manipulation, textual analysis, and predictive modeling to uncover insights into the greeting patterns within the collection.
# Script Descriptions
1_store_in_csv.py: \
The script processes XML files from a specific directory, extracts sender and addressee information, reads and cleans the last ten sentences from each file, and uses the OpenAI API to translate these sentences from Latin to English. 

2_filter_greetings.py: \
The script extracts sentences containing greeting information, writes those sentences into an intermediary CSV, and then filters and saves rows with extracted sentences into a final CSV file. 

3_clean_data.py: \
The Python splits extracted sentences into individual lines, cleans them by removing specific XML tags. 

4_convert_name_tags.py: \
The Python modifies the 'Extracted Sentences' column by replacing specific XML tags with a custom format as Name_ID by using regular expressions. 

5_predict_sender.ipynb & 6_predict_receiver.ipynb: \
These two scripts develop predictive models for identifying the senders and receivers of greetings within the Bullinger Collection. 

7_convert_letter_tags_part1.py & 8_convert_letter_tags_part2.py: \
The first script extracts sender IDs, first names, and last names from the 'Sender Info' and 'Addressee Info' columns, formats them into a new string combining these elements. The second script modifies the two columns by extracting and formatting titles with sender IDs from a pattern, replacing the original format with a more concise version. 

9_replace_names.py: \
The Python script replaces specific keywords related to sender and receiver identities within the 'predicted_sender' and 'predicted_receiver' columns, using names extracted from 'Sender Info' and 'Addressee Info'. 

10_identifier_counting.py: \ 
The script extracts and matches identifiers and names from specific columns, aggregates these names by identifier, compiles and counts these occurrences, and finally exports the summarized data into a new CSV file. 

11_keywords_counting.py: \
The script counts predefined keywords in specified columns, combines these counts into a DataFrame, and exports the results to a new CSV file for both sender and receiver data. 

12_count_lang_frequency.ipynb: \
The script recursively loops through all XML files of the big folder, counts the occurrences of each language attribute within 's' elements, calculates the percentage of each language's occurrence. 

annotated_data.csv: \
It contains greeting data from folders 10 and 13, with sender and receiver labels manually added to each sentence. 

prediction.csv: \
It contains greeting data from the 'greeting information models' predictions. 

final_greeting_data.csv: \
Data in this file is the final greeting data that has been post-processed. 

identifier_and_names_counts.csv \
keyword_counts.csv 



