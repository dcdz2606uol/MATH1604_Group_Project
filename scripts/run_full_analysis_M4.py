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


"""
MATH1604 Group Project - Interim Integration Script
Team Member 4 (Team Leader)

Current Capabilities:
1. Validates all 25 respondent files
2. Tests Team Member 1's answer extraction
3. Prepares for M2/M3 integration

Pending Team Modules:
- data_preparation_M2.py (collation)
- data_analysis_M3.py (stats/visualization)
"""
from data_extraction_M1 import extract_answers_sequence
import os
import time

def log_progress(message: str):
    """Track progress with timestamps"""
    print(f"[{time.strftime('%H:%M:%S')}] {message}")

def validate_files():
    """Verify all 25 respondent files exist and are readable"""
    for i in range(1, 26):
        path = f"data/answers_respondent_{i}.txt"
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing file: {path}")
        
        # Quick format check using M1's parser
        answers = extract_answers_sequence(path)
        if len(answers) != 100 or not all(0 <= x <= 4 for x in answers):
            raise ValueError(f"Invalid format in {path}")

def mock_m2_functions():
    """Placeholder stubs for Team Member 2's work"""
    def download_answer_files(*args, **kwargs):
        log_progress("M2 placeholder: Skipping download (using local files)")

    def collate_answer_files(*args, **kwargs):
        log_progress("M2 placeholder: Collation not yet implemented")
        return True  # Pretend success

    return download_answer_files, collate_answer_files

def mock_m3_functions():
    """Placeholder stubs for Team Member 3's work"""
    def generate_means_sequence(*args, **kwargs):
        log_progress("M3 placeholder: Returning mock means")
        return [2.5] * 100  # Fake uniform distribution

    def visualize_data(*args, **kwargs):
        log_progress("M3 placeholder: No visualization available")
        return True

    return generate_means_sequence, visualize_data

def main():
    try:
        log_progress("Starting validation...")
        validate_files()
        
        # Load stubs or real implementations
        download, collate = mock_m2_functions()
        gen_means, visualize = mock_m3_functions()
        
        log_progress("Testing pipeline...")
        download(cloud_url="", path_to_data_folder="data", respondent_index=25)
        if collate("data"):
            means = gen_means("output/collated_answers.txt")
            visualize("output/collated_answers.txt", n=1)
        
        log_progress("✅ Ready for team integration")
        print("\nPending implementations:")
        print("- M2: Complete collate_answer_files()")
        print("- M3: Implement generate_means_sequence() and visualize_data()")

    except Exception as e:
        log_progress(f"❌ Error: {str(e)}")
        if isinstance(e, FileNotFoundError):
            print("  → Check filenames match 'answers_respondent_[1-25].txt'")

if __name__ == "__main__":
    main()
