"""
MATH1604 Group Project - Main Integration Script
Team Member 4 (Team Leader)
"""
from data_extraction_M1 import extract_answers_sequence
from data_preparation_M2 import download_answer_files, collate_answer_files
from data_analysis_M3 import generate_means_sequence, visualize_data

def main():
    # Step 1: Download and collate data
    download_answer_files(cloud_url="[URL_TO_ANSWERS]", 
                        path_to_data_folder="data/", 
                        respondent_index=40)  # Example: 40 respondents
    
    collate_answer_files(data_folder_path="data/")

    # Step 2: Analysis and visualization (placeholder)
    means = generate_means_sequence("output/collated_answers.txt")
    visualize_data("output/collated_answers.txt", n=1)  # Scatter plot

if __name__ == "__main__":
    main()
