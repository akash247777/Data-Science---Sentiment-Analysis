import os  # Importing os module for interacting with the operating system
import re  # Importing re module for regular expression operations
import pandas as pd  # Importing pandas for data manipulation and analysis
import nltk  # Importing nltk library for natural language processing
from nltk.corpus import stopwords  # Importing stopwords from nltk corpus
from textstat import textstat  # Importing textstat for text readability statistics

# Ensure necessary NLTK resources are downloaded
nltk.data.path.append("C:\\Users\\APL94855\\AppData\\Roaming\\nltk_data")  # Setting the path for NLTK data
nltk.download('punkt', download_dir="C:\\Users\\APL94855\\AppData\\Roaming\\nltk_data")  # Downloading the punkt tokenizer model

# Define the folder paths for stop words and master dictionary files
stopwords_folder = "C:\\Senment analysis\\20211030 Test Assignment\\StopWords"
master_dict_folder = "C:\\Senment analysis\\20211030 Test Assignment\\MasterDictionary"

# Combine all stopwords into a single set
stopwords_set = set()  # Initialize an empty set for stop words
for file in os.listdir(stopwords_folder):  # Loop through each file in the stopwords folder
    with open(os.path.join(stopwords_folder, file), "r", encoding="utf-8") as f:  # Open each stopword file
        stopwords_set.update(f.read().splitlines())  # Read lines and add them to the stopwords set

# Load Master Dictionary for sentiment analysis
positive_words = set()  # Initialize an empty set for positive words
negative_words = set()  # Initialize an empty set for negative words
with open(os.path.join(master_dict_folder, "positive-words.txt"), "r", encoding="utf-8") as f:  # Open the positive words file
    positive_words.update(f.read().splitlines())  # Read lines and add them to the positive words set
with open(os.path.join(master_dict_folder, "negative-words.txt"), "r", encoding="latin-1") as f:  # Open the negative words file
    negative_words.update(f.read().splitlines())  # Read lines and add them to the negative words set

# Define helper function to count syllables in a word
def count_syllables(word):
    word = word.lower()  # Convert the word to lowercase
    vowels = "aeiouy"  # Define vowels
    count = sum(1 for char in word if char in vowels)  # Count vowels in the word
    if word.endswith(("es", "ed")) and not word.endswith(("le",)):  # Adjust count for specific endings
        count -= 1
    return max(count, 1)  # Return the count, ensuring at least 1 syllable

# Define a function to compute various text metrics
def compute_metrics(text):
    sentences = nltk.sent_tokenize(text)  # Tokenize the text into sentences
    words = nltk.word_tokenize(text)  # Tokenize the text into words
    cleaned_words = [word for word in words if word.isalpha() and word.lower() not in stopwords_set]  # Clean words by removing non-alphabetic and stop words
    word_count = len(cleaned_words)  # Count the total number of cleaned words
    complex_words = [word for word in cleaned_words if count_syllables(word) > 2]  # Identify complex words (more than 2 syllables)
    
    # Calculate sentiment scores
    positive_score = sum(1 for word in cleaned_words if word.lower() in positive_words)  # Count positive words
    negative_score = sum(1 for word in cleaned_words if word.lower() in negative_words)  # Count negative words
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)  # Calculate polarity score
    subjectivity_score = (positive_score + negative_score) / (word_count + 0.000001)  # Calculate subjectivity score
    
    # Calculate various text metrics
    avg_sentence_length = word_count / len(sentences) if sentences else 0  # Average sentence length
    percentage_complex_words = len(complex_words) / word_count if word_count else 0  # Percentage of complex words
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)  # Calculate FOG index
    avg_word_length = sum(len(word) for word in cleaned_words) / word_count if word_count else 0  # Average word length
    syllables_per_word = sum(count_syllables(word) for word in cleaned_words) / word_count if word_count else 0  # Average syllables per word
    personal_pronouns = len(re.findall(r"\b(I|we|my|ours|us)\b", text, flags=re.I))  # Count personal pronouns in the text
    
    # Return a dictionary of computed metrics
    return {
        "POSITIVE SCORE": positive_score,
        "NEGATIVE SCORE": negative_score,
        "POLARITY SCORE": polarity_score,
        "SUBJECTIVITY SCORE": subjectivity_score,
        "AVG SENTENCE LENGTH": avg_sentence_length,
        "PERCENTAGE OF COMPLEX WORDS": percentage_complex_words,
        "FOG INDEX": fog_index,
        "COMPLEX WORD COUNT": len(complex_words),
        "WORD COUNT": word_count,
        "SYLLABLE PER WORD": syllables_per_word,
        "PERSONAL PRONOUNS": personal_pronouns,
        "AVG WORD LENGTH": avg_word_length,
    }

# Perform analysis on extracted text files
input_data = pd.read_excel("C:\\Senment analysis\\20211030 Test Assignment\\Input.xlsx")  # Load input data from Excel file
output_data = []  # Initialize an empty list to store output data

# Loop through each row in the input data
for index, row in input_data.iterrows():
    url_id = row["URL_ID"]  # Extract URL_ID from the row
    text_file = f"ExtractedArticles/{url_id}.txt"  # Construct the filename for the corresponding text file
    
    try:
        with open(text_file, "r", encoding="utf-8") as file:  # Attempt to open the text file
            text = file.read()  # Read the content of the text file
        metrics = compute_metrics(text)  # Compute metrics for the extracted text
        output_data.append({**row, **metrics})  # Append the original row data and computed metrics to output data
        print(f"Processed URL_ID {url_id}")  # Print a success message with the URL_ID
    
    except Exception as e:  # Handle any exceptions that occur during file processing
        print(f"Failed to process URL_ID {url_id}: {e}")  # Print an error message with the URL_ID and exception details

# Save results to the output Excel file
output_df = pd.DataFrame(output_data)  # Convert output data to a DataFrame
output_df.to_excel("Output Data Structure.xlsx", index=False)  # Save DataFrame to an Excel file without index
print("Text analysis completed.")  # Print a completion message
