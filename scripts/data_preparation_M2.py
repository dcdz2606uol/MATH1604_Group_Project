import os
import glob
import requests
from urllib.parse import urljoin
import sys
import time
from datetime import datetime
import matplotlib.pyplot as plt
from data_extraction_M1 import extract_answers_sequence, write_answers_sequence

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    # Create the data directory if it doesn't exist
    os.makedirs(path_to_data_folder, exist_ok=True)
    
    # Construct the source URL for the respondent's file
    file_name = f'a{respondent_index}.txt'
    source_url = urljoin(cloud_url, file_name)
    
    # Send a GET request to download the file
    response = requests.get(source_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Define the destination path and save the file
    dest_file = f'answers_respondent_{respondent_index}.txt'
    dest_path = os.path.join(path_to_data_folder, dest_file)
    with open(dest_path, 'wb') as file:
        file.write(response.content)

def collate_answer_files(data_folder_path):
    # Find all answer files in the data folder
    file_pattern = os.path.join(data_folder_path, 'answers_respondent_*.txt')
    answer_files = glob.glob(file_pattern)
    
    # Extract and sort files by respondent index
    sorted_files = []
    for file_path in answer_files:
        base_name = os.path.basename(file_path)
        parts = base_name.split('_')
        index = int(parts[2].split('.')[0])
        sorted_files.append((index, file_path))
    sorted_files.sort(key=lambda x: x[0])
    
    # Prepare the output directory
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'collated_answers.txt')
    
    # Write all contents into the collated file with separators
    with open(output_file, 'w') as outfile:
        for i, (_, file_path) in enumerate(sorted_files):
            with open(file_path, 'r') as infile:
                content = infile.read().rstrip('\n')  # Remove trailing newlines
                outfile.write(content)
                # Add a separator line if not the last file
                if i < len(sorted_files) - 1:
                    outfile.write('\n*\n')
