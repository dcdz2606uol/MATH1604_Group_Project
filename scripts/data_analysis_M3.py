import os
import sys
import time
from datetime import datetime
import matplotlib.pyplot as plt
from team_member1_module import extract_answers_sequence
from team_member2_module import generate_means_sequence

def generate_means_sequence(collated_answers_path):
    answer_sequences = extract_answers_sequence(collated_answers_path)
    means = []
    for question_index in range(100):
        total = 0
        count = 0
        for sequence in answer_sequences:
            value = sequence[question_index]
            if value != 0:
                total += value
                count += 1
        if count == 0:
            means.append(0.0)
        else:
            means.append(total / count)
    return means

def visualize_data(collated_answers_path, n):
    if n not in (1, 2):
        plt.figure()
        plt.text(0.5, 0.5, 'Error: n must be 1 or 2', ha='center', va='center')
        plt.axis('off')
        plt.show()
        return

    if n == 1:
        means = generate_means_sequence(collated_answers_path)
        x = list(range(1, 101))
        plt.scatter(x, means)
        plt.xlabel('Question Number')
        plt.ylabel('Mean Answer Value')
        plt.title('Scatter Plot of Mean Answer Values per Question')
        plt.xlim(1, 100)
        plt.xticks(range(1, 101, 10))
        plt.show()

    elif n == 2:
        answer_sequences = extract_answers_sequence(collated_answers_path)
        x = list(range(1, 101))
        plt.figure()
        for seq in answer_sequences:
            plt.plot(x, seq, alpha=0.5)  # Using alpha for better visibility
        plt.xlabel('Question Number')
        plt.ylabel('Answer Value')
        plt.title('Line Plot of Individual Answer Sequences')
        plt.xlim(1, 100)
        plt.xticks(range(1, 101, 10))
        plt.show()

   
