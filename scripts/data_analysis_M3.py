"""
data_analysis_M3.py

This module performs analysis and visualisation on the collated Python quiz responses.

Functions:
- generate_means_sequence(collated_answers_path): Calculates the average answer value per question.
- visualize_data(collated_answers_path, n): Visualizes the data based on input style (scatter or line plot).
"""

import os
import matplotlib.pyplot as plt

from data_extraction_M1 import extract_answers_sequence


def generate_means_sequence(collated_answers_path):
    """
    Computes the mean value of answers per question from a collated answers file.

    Parameters:
    collated_answers_path (str): Path to the 'collated_answers.txt' file.

    Returns:
    list of float: A list of 100 floats representing the mean answer values (1–4), excluding unanswered (0s).
    """
    with open(collated_answers_path, 'r') as file:
        content = file.read()

    respondent_blocks = content.strip().split('\n*\n')
    num_questions = 100
    question_sums = [0] * num_questions
    question_counts = [0] * num_questions

    for block in respondent_blocks:
        answers = []
        for line in block.strip().split('\n'):
            try:
                val = int(line.strip())
                answers.append(val)
            except ValueError:
                continue  # Skip lines like "Question 1. What is a program?"

        if len(answers) != num_questions:
            continue  # Skip if the block isn't 100 integers long

        for i, answer in enumerate(answers):
            if answer != 0:
                question_sums[i] += answer
                question_counts[i] += 1

    means = [
        round(question_sums[i] / question_counts[i], 2) if question_counts[i] > 0 else 0.0
        for i in range(num_questions)
    ]
    return means

def visualize_data(collated_answers_path, n):
    """
    Visualizes the answer data either as a scatter plot of means or as a line plot of individual answers.

    Parameters:
    collated_answers_path (str): Path to the 'collated_answers.txt' file.
    n (int): Type of plot. 1 for scatter (means), 2 for line plot (all responses).

    Returns:
    None. Displays the appropriate plot.
    """
    import matplotlib.pyplot as plt

    if n == 1:
        means = generate_means_sequence(collated_answers_path)
        plt.figure(figsize=(12, 5))
        plt.scatter(range(1, 101), means, color='blue', s=10)
        plt.title("Mean Answer Value Per Question")
        plt.xlabel("Question Number")
        plt.ylabel("Mean Answer Value")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    elif n == 2:
        with open(collated_answers_path, 'r') as file:
            content = file.read()
        respondent_blocks = content.strip().split('\n*\n')

        plt.figure(figsize=(12, 6))
        for block in respondent_blocks:
            answers = []
            for line in block.strip().split('\n'):
                try:
                    val = int(line.strip())
                    answers.append(val)
                except ValueError:
                    continue
            if len(answers) == 100:
                plt.plot(range(1, 101), answers, alpha=0.3)
        plt.title("All Respondent Answer Sequences")
        plt.xlabel("Question Number")
        plt.ylabel("Answer (1–4)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    else:
        print("Invalid value for parameter n. Please use 1 (scatter) or 2 (line plot).")



"""
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
"""
