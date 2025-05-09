import os
import requests

def download_answer_files(cloud_url, save_folder, total_files):
    # Create the folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    # Download each file
    for i in range(1, total_files + 1):
        url = f"{cloud_url}/answers_respondent_{i}.txt"
        file_name = f"answers_respondent_{i}.txt"
        file_path = os.path.join(save_folder, file_name)

        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Saved: {file_name}")
        else:
            print(f"Failed to download: {url}")

def collate_answer_files(folder_path):
    # Create output folder
    if not os.path.exists("output"):
        os.mkdir("output")

    # Open the final file for writing
    with open("output/collated_answers.txt", "w", encoding="utf-8") as out_file:
        # Find and sort all respondent files
        files = [f for f in os.listdir(folder_path) if f.startswith("answers_respondent_")]
        files.sort(key=lambda x: int(x.split("_")[-1].split(".")[0]))

        for i, file_name in enumerate(files):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                out_file.write(content)

            # Add separator unless it's the last file
            if i < len(files) - 1:
                out_file.write("\n*\n")
            else:
                out_file.write("\n")

    print("All answers have been successfully collated!")
