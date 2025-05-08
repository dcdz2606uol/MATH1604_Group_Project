"""
MATH1604 Group Project - Main Integration Script
Team Member 4 (Team Leader)

Orchestrates:
1. Data preparation (download/collation)
2. Answer sequence extraction
3. Statistical analysis and visualization
"""

#run_full_analysis_M4.py - Final Integration Script for Python Quiz Response Analysis


import os
import sys
import time
from datetime import datetime
from data_extraction_M1 import extract_answers_sequence, write_answers_sequence
from data_preparation_M2 import download_answer_files, collate_answer_files
from data_analysis_M3 import generate_means_sequence, visualize_data

# Configuration
CONFIG = {
    'cloud_url': "https://example.com/quiz_data",
    'num_respondents': 40,
    'data_folder': "data",
    'output_folder': "output",
    'log_file': "analysis_log.txt"
}

def setup_environment():
    """
    Creates necessary directories and initializes the log file.
    """
    os.makedirs(CONFIG['data_folder'], exist_ok=True)
    os.makedirs(CONFIG['output_folder'], exist_ok=True)
    with open(CONFIG['log_file'], 'w') as f:
        f.write(f"Analysis Log - {datetime.now()}\n{'='*40}\n")


def log_message(message):
    """
    Logs messages with timestamps to both console and log file.

    Parameters:
    message (str): The message to log.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(CONFIG['log_file'], 'a') as f:
        f.write(log_entry + "\n")


def generate_mock_data(num_files=5):
    """
    Generates mock data in the expected quiz answer format for testing purposes.

    Parameters:
    num_files (int): Number of mock respondent files to generate.
    """
    log_message("Generating mock data for testing...")
    for i in range(1, num_files + 1):
        file_path = os.path.join(CONFIG['data_folder'], f"answers_respondent_{i}.txt")
        with open(file_path, 'w') as f:
            for q in range(1, 101):
                f.write(f"Question {q}. Mock question {q}\n")
                for opt in range(1, 5):
                    if q % 4 == opt % 4:
                        f.write(f"[x] Answer {q}.{opt}\n")
                    else:
                        f.write(f"[ ] Answer {q}.{opt}\n")
                f.write("\n")
    log_message(f"Generated {num_files} mock respondent files")


def validate_sequences(sequences):
    """
    Filters out invalid answer sequences and logs issues.

    Parameters:
    sequences (list[list[int] or None]): List of answer sequences.

    Returns:
    list[list[int]]: Validated answer sequences.
    """
    valid_sequences = []
    for i, seq in enumerate(sequences, 1):
        if seq is None:
            log_message(f"Warning: No data for respondent {i}")
            continue
        if len(seq) != 100:
            log_message(f"Warning: Invalid length for respondent {i} ({len(seq)} answers)")
            continue
        valid_sequences.append(seq)
    return valid_sequences


def run_full_analysis():
    """
    Runs the full data processing and analysis pipeline.
    """
    start_time = time.time()
    log_message("Starting complete analysis pipeline")

    try:
        log_message("Phase 1: Data Download and Collation")
        try:
            download_answer_files(CONFIG['cloud_url'], CONFIG['data_folder'], CONFIG['num_respondents'])
        except Exception as e:
            log_message(f"Download failed, using mock data: {str(e)}")
            generate_mock_data()

        collate_answer_files(CONFIG['data_folder'])
        log_message("Data preparation complete")

        log_message("Phase 2: Answer Sequence Extraction")
        sequences = []
        for i in range(1, CONFIG['num_respondents'] + 1):
            file_path = os.path.join(CONFIG['data_folder'], f"answers_respondent_{i}.txt")
            if os.path.exists(file_path):
                seq = extract_answers_sequence(file_path)
                sequences.append(seq)
                write_answers_sequence(seq, i)

        valid_sequences = validate_sequences(sequences)
        log_message(f"Extracted {len(valid_sequences)} valid sequences")

        log_message("Phase 3: Statistical Analysis and Visualization")
        collated_path = os.path.join(CONFIG['output_folder'], "collated_answers.txt")
        means = generate_means_sequence(collated_path)
        log_message("Calculated mean answer values")

        visualize_data(collated_path, 1)
        visualize_data(collated_path, 2)

        duration = time.time() - start_time
        log_message(f"Analysis completed successfully in {duration:.2f} seconds")
        return True

    except Exception as e:
        log_message(f"Analysis failed: {str(e)}")
        return False


def main():
    """
    Entry point for running the entire project.
    """
    setup_environment()
    if not run_full_analysis():
        sys.exit(1)


if __name__ == "__main__":
    main()

