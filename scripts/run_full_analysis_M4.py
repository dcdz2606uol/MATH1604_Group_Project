"""
MATH1604 Group Project - Main Integration Script
Team Member 4 (Team Leader)

Orchestrates:
1. Data preparation (download/collation)
2. Answer sequence extraction
3. Statistical analysis and visualization
"""
from data_extraction_M1 import extract_answers_sequence
from data_preparation_M2 import download_answer_files, collate_answer_files
from data_analysis_M3 import generate_means_sequence, visualize_data

def main():
    try:
        # Step 1: Data Preparation
        # Since files are in data/, skip download or mock it
        download_answer_files(cloud_url="", path_to_data_folder="data/", respondent_index=25)  # 25 since there are 25 respondent files
        
        # Collate all 25 respondent files
        collate_answer_files(data_folder_path="data/")
        
        # Step 2: Analysis
        means = generate_means_sequence("output/collated_answers.txt")
        
        # Step 3: Visualization (scatter plot by default)
        visualize_data("output/collated_answers.txt", n=1)  
        
    except FileNotFoundError as e:
        print(f"Error: {e}. Check if data files exist in data/")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
