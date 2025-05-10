import os
import matplotlib.pyplot as plt
from data_extraction_M1 import extract_answers_sequence 
from data_preparation_M2 import collate_answer_files


def generate_means_sequence(collated_answers_path):
    """
    Input: Path to collated_answers.txt
    Output: List of 100 floats (mean per question, excluding 0s)
    """
    with open(collated_answers_path, 'r', encoding='utf-8') as file:
        raw_data = file.read()

    # Split data by respondent
    respondent_blocks = raw_data.strip().split('\n*\n')
    all_sequences = []

    for block in respondent_blocks:
        # Write temporary individual respondent file
        temp_path = 'temp_response.txt'
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(block.strip())
        # Extract sequence (using extract_answers_sequence from M1)
        seq = extract_answers_sequence(temp_path)
        os.remove(temp_path)
        if seq and len(seq) == 100:
            all_sequences.append(seq)

    means = []
    for i in range(100):
        values = [seq[i] for seq in all_sequences if seq[i] != 0]
        mean = sum(values) / len(values) if values else 0.0
        means.append(mean)

    return means


def visualize_data(collated_answers_path, n):
    """
    Input: Path to collated_answers.txt, integer n (1 or 2)
    Output: Plots scatter (n=1), line chart (n=2), or error
    """
    with open(collated_answers_path, 'r', encoding='utf-8') as file:
        raw_data = file.read()

    respondent_blocks = raw_data.strip().split('\n*\n')
    all_sequences = []

    for block in respondent_blocks:
        temp_path = 'temp_response.txt'
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(block.strip())
        seq = extract_answers_sequence(temp_path)
        os.remove(temp_path)
        if seq and len(seq) == 100:
            all_sequences.append(seq)

    if n == 1:
        means = generate_means_sequence(collated_answers_path)
        plt.scatter(range(1, 101), means, color='blue')
        plt.title('Mean Answer Value per Question (Scatter)')
        plt.xlabel('Question Number')
        plt.ylabel('Mean Value')
        plt.grid(True)
        plt.show()

    elif n == 2:
        for seq in all_sequences:
            plt.plot(range(1, 101), seq, alpha=0.4)
        plt.title('Individual Respondent Answer Patterns (Line Plot)')
        plt.xlabel('Question Number')
        plt.ylabel('Answer Value')
        plt.grid(True)
        plt.show()

    else:
        print("Error: Invalid visualization type. Use 1 for scatter, 2 for line.")
