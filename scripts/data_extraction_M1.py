def extract_answers_sequence(file_path):
    answers = [0] * 100
    try: # I've added this to prevent an error if file path is wrong 
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Split content into question block
        question_blocks = content.split('Question')[1:]  # Skip the first split element because it's irrelevant 
        
        # Processing all 100 question blocks
        for i, block in enumerate(question_blocks):
            if i >= 100:
                break  # Making sure we don't go beyond the 100 questions

            lines = block.split('\n')
            option_number = 1 # Counts the options this question

            for line in lines:
                line = line.strip()
                if line.startswith('[x]'): # Looks for marked answer
                    answers[i] = option_number
                    break # Switchs to next question when found

                elif line.startswith('[ ]'):
                    option_number += 1 # increase for each unmarked option
    
    except FileNotFoundError: # Prints error that file's not found if the try doesn't work
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:  # Prints error that there's an error if the try doesn't work
        print(f"An error occurred: {e}")
        return None
    
    return answers

def write_answers_sequence(answer = list, n = int):
    file_name = f"answers_list_respondent_{n}.txt" # Sets file name to n
    f = open(file_name, "w") # Creates file if it's not there before
    answer = str(answer) # Convert to string in order to write
    f.write(answer)
    f.close()    
