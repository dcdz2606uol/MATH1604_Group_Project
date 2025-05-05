import os
import requests
from typing import List

def download_answer_files(cloud_url: str, path_to_data_folder: str, respondent_index: int) -> None:
    # Create data folder if it doesn't exist
    os.makedirs(path_to_data_folder, exist_ok=True)
    
    file_number = 1
    while True:
        # Construct source and destination paths
        source_url = f"{cloud_url}/a{file_number}.txt"
        dest_path = os.path.join(path_to_data_folder, f"answers_respondent_{respondent_index}.txt")
        
        try:
            # Download the file
            response = requests.get(source_url)
            response.raise_for_status()
            
            # Save with new name
            with open(dest_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded and saved: {dest_path}")
            file_number += 1
            respondent_index += 1
            
        except requests.exceptions.RequestException as e:
            # Stop when we can't find the next file
            if file_number == 1:
                raise Exception(f"No answer files found at {cloud_url}")
            break

def collate_answer_files(data_folder_path: str) -> None:
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(data_folder_path), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all answer files in order
    answer_files = sorted(
        [f for f in os.listdir(data_folder_path) if f.startswith('answers_respondent_')],
        key=lambda x: int(x.split('_')[-1].split('.')[0])
    )
    
    if not answer_files:
        raise ValueError(f"No answer files found in {data_folder_path}")
    
    # Create the collated file
    output_path = os.path.join(output_dir, 'collated_answers.txt')
    with open(output_path, 'w') as outfile:
        for i, filename in enumerate(answer_files):
            filepath = os.path.join(data_folder_path, filename)
            
            # Write the respondent's answers
            with open(filepath, 'r') as infile:
                outfile.write(infile.read().strip())
            
            # Add separator (but not after the last file)
            if i < len(answer_files) - 1:
                outfile.write('\n*\n')
    
    print(f"Collated answers saved to {output_path}")
