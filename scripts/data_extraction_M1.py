def extract_answers_sequence(file_path):
    answers = [0] * 100
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Split content into question blocks
        question_blocks = content.split('Question')[1:]  # Skip the first split element
        
        for i, block in enumerate(question_blocks):
            if i >= 100:
                break  # Ensure we don't exceed 100 questions
            lines = block.split('\n')
            option_number = 1
            for line in lines:
                line = line.strip()
                if line.startswith('[x]'):
                    answers[i] = option_number
                    break
                elif line.startswith('[ ]'):
                    option_number += 1
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    return answers

def write_answers_sequence(answer = list, n = int):
    file_name = f"answers_list_respondent_{n}.txt"
    f = open(file_name, "w")
    answer = str(answer)
    f.write(answer)
    f.close()    
