import os  # Import the os module for interacting with the operating system
import requests  # Import the requests module for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup from the bs4 module for parsing HTML
import pandas as pd  # Import pandas for data manipulation and analysis

# Create a folder to store the text files
output_folder = "ExtractedArticles"  # Define the folder name for storing extracted articles
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Load the input Excel file
input_file = "C:\\Senment analysis\\20211030 Test Assignment\\Input.xlsx"  # Define the path to the input Excel file
input_data = pd.read_excel(input_file)  # Read the Excel file into a pandas DataFrame

# Iterate through each row in the input file
for index, row in input_data.iterrows():  # Loop through each row in the DataFrame
    url_id = row["URL_ID"]  # Get the URL_ID from the current row
    url = row["URL"]  # Get the URL from the current row
    
    try:
        # Fetch the webpage content
        response = requests.get(url)  # Make an HTTP GET request to the URL
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML content using BeautifulSoup
        
        # Extract the title and article text
        title = soup.find("title").get_text(strip=True) if soup.find("title") else "No Title"  # Extract the title text if available
        article_body = soup.find("article")  # Find the <article> tag in the HTML
        if article_body:  # Check if the <article> tag is found
            article_text = article_body.get_text(separator="\n", strip=True)  # Extract and clean the article text
        else:
            article_text = "No article content found"  # Set a default message if no article content is found
        
        # Combine title and article text
        extracted_text = f"Title: {title}\n\n{article_text}"  # Combine the title and article text
        
        # Save to a text file named after the URL_ID
        output_path = os.path.join(output_folder, f"{url_id}.txt")  # Define the output file path
        with open(output_path, "w", encoding="utf-8") as file:  # Open the file for writing with UTF-8 encoding
            file.write(extracted_text)  # Write the extracted text to the file
        
        print(f"Successfully extracted URL_ID {url_id}")  # Print a success message
    
    except Exception as e:  # Handle exceptions 
        print(f"Failed to process URL_ID {url_id}: {e}")  # Print an error message with the exception

print("Data extraction completed.")  # Print a completion message