# Data-Science---Sentiment-Analysis
This project aims to extract textual data from articles available at specified URLs and perform comprehensive text analysis to compute various linguistic and readability metrics. The primary objectives include: Data Extraction, Data Analysis
# 📰 Article Extractor and Sentiment Analysis Tool

Welcome to the Article Extractor and Sentiment Analysis Tool! This project allows you to extract articles from a list of URLs, analyze their content, and generate insightful metrics about the text. 📊✨

## 📁 Project Structure

├── ExtractedArticles/ # Folder where extracted articles are saved ├── StopWords/ # Folder containing stop words for analysis ├── MasterDictionary/ # Folder containing sentiment word lists ├── Input.xlsx # Input Excel file with URLs and IDs ├── Output Data Structure.xlsx # Output Excel file with analysis results └── README.md # Project documentation


## 🚀 Features

- **Article Extraction**: Fetches and saves articles from provided URLs. 🌐
- **Text Analysis**: Computes various metrics including:
  - Positive and negative scores 🟢🔴
  - Polarity and subjectivity scores ⚖️
  - Average sentence length and word length 📏
  - FOG index and percentage of complex words 📈
  - Count of personal pronouns 🗣️
- **Easy Integration**: Works seamlessly with Excel files for input and output. 📊

## 📦 Requirements

To run this project, you'll need the following Python packages:

- `requests` 📦
- `beautifulsoup4` 🍲
- `pandas` 🐼
- `nltk` 📚
- `textstat` 📊

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 pandas nltk textstat

📋 Usage

1. Prepare your input file: Create an Excel file named Input.xlsx with columns URL_ID and URL.
2. Set up stop words and master dictionary: Place your stop words and sentiment dictionaries in the respective folders.
3. Run the script: Execute the Python script to extract articles and perform sentiment analysis.
4. Check the output: Results will be saved in Output Data Structure.xlsx.
