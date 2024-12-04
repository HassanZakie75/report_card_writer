# Report card writer for MYP Science by Hassan Zakie Yusoff 
# version: 4.12.2024 (completed on 4/12/2024)

''' How to use
        1- Rename the input and output file according to you csv file and desired output
        2- Write the correct SUBJECT and LEVEL in the preset_report_template.py 
        3- Run the report_generator.py and enjoy your report                            '''

import random
import csv
from preset_report_template import get_crit_a_weak, get_crit_a_average, get_crit_a_strong, get_crit_b_weak, get_crit_b_average, get_crit_b_strong, get_crit_c_weak, get_crit_c_average, get_crit_c_strong, get_crit_d_weak, get_crit_d_average, get_crit_d_strong

# generate report card comments from the preset
def generate_comment(student):

    # variables definition
    name = student['name']
    gender = student['gender']
    grade_a = int(student['A'])
    grade_b = int(student['B'])
    grade_c = int(student['C'])
    grade_d = int(student['D'])

    comments = {}
    gender1 = ""
    gender2 = ""
    gender3 = ""

    # Check and setup gender for preset sentence structure
    if gender == "male":
        gender1 = "he"
        gender2 = "his"
        gender3 = "him"
        gender4 = "He"
    elif gender == "female":
        gender1 = "she"
        gender2 = "her"
        gender3 = "her"
        gender4 = "She"
    else:
        print("nonbinary is not acceptable")
        return 1  

    # Calling the comment from preset template
    crit_a_weak = get_crit_a_weak(name, gender1, gender2, gender3, gender4)
    crit_a_average = get_crit_a_average(name, gender1, gender2, gender3, gender4)
    crit_a_strong = get_crit_a_strong(name, gender1, gender2, gender3, gender4)
    crit_b_weak = get_crit_b_weak(name, gender1, gender2, gender3, gender4)
    crit_b_average = get_crit_b_average(name, gender1, gender2, gender3, gender4)
    crit_b_strong = get_crit_b_strong(name, gender1, gender2, gender3, gender4)
    crit_c_weak = get_crit_c_weak(name, gender1, gender2, gender3, gender4)
    crit_c_average = get_crit_c_average(name, gender1, gender2, gender3, gender4)
    crit_c_strong = get_crit_c_strong(name, gender1, gender2, gender3, gender4)
    crit_d_weak = get_crit_d_weak(name, gender1, gender2, gender3, gender4)
    crit_d_average = get_crit_d_average(name, gender1, gender2, gender3, gender4)
    crit_d_strong = get_crit_d_strong(name, gender1, gender2, gender3, gender4)

    # Main algorith for selecting random comment based on each students grade level
    for grade in [grade_a, grade_b, grade_c, grade_d] :
        if grade_a >= 7:
                commentA = random_sentence_selector(crit_a_strong)
        elif grade_a < 7 and grade_a >= 5:
                commentA = random_sentence_selector(crit_a_average)
        else:
                commentA = random_sentence_selector(crit_a_weak)
        if grade_b >= 7:
                commentB = crit_b_strong
        elif grade_b < 7 and grade_b >= 5:
                commentB = random_sentence_selector(crit_b_average)
        else:
                commentB = random_sentence_selector(crit_b_weak)
        if grade_c >= 7:
                commentC = crit_c_strong
        elif grade_c < 7 and grade_c >= 5:
                commentC = random_sentence_selector(crit_c_average)
        else:
                commentC = random_sentence_selector(crit_c_weak)
        if grade_d >= 7:
                commentD = crit_d_strong
        elif grade_d < 7 and grade_d >= 5:
                commentD = random_sentence_selector(crit_d_average)
        else:
                commentD = random_sentence_selector(crit_d_weak)

        comments = ''.join(commentA) + ''.join(commentB) + ''.join(commentC) + ''.join(commentD) + '\n' + '\n'

    return comments

# Randomly select sentences suitable for their achievement level
def random_sentence_selector(sentences):

    random_index = random.randint(0, len(sentences) - 1)
    return sentences[random_index]

# Read the CSV file
def generate_report_card(input_csv, output_txt):
    # Load the data from the CSV file
    with open(input_csv, mode='r') as file:
        reader = csv.DictReader(file)

    # Open the output text file to write the report cards
        with open(output_txt, mode='w') as output_file:
            # Process each student in the CSV
            for student in reader:
                report_card = generate_comment(student)
                output_file.write(report_card)
                print(f"Report card for {student['name']} generated.")

# Example usage:
input_csv = 'grades/gradesM4.csv'
output_txt = 'output/report_cards_M4.txt'
generate_report_card(input_csv, output_txt)


# For testing purposes
#name = "Harshieeeni"
#gender = "male"
#grade_a = 4
#grade_b = 5
#grade_c = 6
#grade_d = 7
#
#subject_comments = generate_comment(name, gender, grade_a, grade_b, grade_c, grade_d)
#
##for criterion, comment in subject_comments.items():
##    print(f"Comment for Criterion {criterion}: {comment}")
#
#print(subject_comments)