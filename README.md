Basic report card writer from a preset list of comments. Will auto generate according to grade level. This code is written for IB MYP science, math and physics subjects
This code will read a template, adjust the name, pronouns according to their genders automatically. Hence a template txt file is required.
input in .csv
output as a .txt file

input must have name, gender, Grade A, B, C, and D

This Python program automates the generation of report cards for IB MYP subjects, streamlining the process for educators.

The program consist of 2 python file. report_generator.py and preset_report_template.py.
report_generator.py will will take the input from argument and write the whole report. It will aslo call a function from the preset_report_template.py
preset_report_template.py will read the template.text and convert the file into strings that can use with correct format. The string will later than be alter by adding the names and correct gender.
report_generator.py will then recall the output from the preset_report_template according to the students name and their achievement level. The report will choose one from a variety of sentences suitable within their achievement level.

## Features

Leverages pre-defined comment templates for each criterion (A, B, C, D)
Automatically adjusts names and pronouns based on student gender from a CSV file
Generates reports tailored to the specific grade level and subject
Simplifies report generation for IB MYP teachers

## Requirements

Python 3.x (download at https://www.python.org/downloads/)

## Files Needed

grades_{level}_{subject}.csv: A CSV file containing student data in the following format:

name, gender, A, B, C, D

text/{subject}_S1_2223_{level}.txt: A text file containing the comment templates for each criterion (A, B, C, D) at the specified grade level and subject.
The file name format is crucial for the program to identify the correct template. The users have to inititally update the preset_report_template.py wheere LEVEL = {grade_level} and SUBJECT = {subject}.
This is where improvement can still be made so that users did not have to change the code each time using a different templates.


## Installation

No external library installation is required for this program to run. Just simply run the file.

## Usage

### 1- Ensure Files are in the Correct Folders:

Place the grades/grades{level}_{subject}.csv file in a /grades subdirectory within the program's directory.
Place the text/{subject}_S1_2223_{level}.txt file in the /text subdirectory within the program's directory.

### 2- Set Subject and Level in preset_report_template.py:

Open preset_report_template.py in a text editor.
Update the SUBJECT and LEVEL variables with the desired values.

### 3- Run the Program:

Open a command prompt or terminal and navigate to the directory containing report_generator.py.

### 4- Execute the command:

python report_generator.py {LEVEL} {SUBJECT}

Replace {LEVEL} with the actual grade level (e.g., M1 - M5).

Replace {SUBJECT} with the actual subject name (e.g., SC - Science, MA - mathematic CHE - chemistry).

Important: Ensure both level and subject are in uppercase letters.

### 5- Generated Files

The program will generate report cards for each class in the CSV file, named according to the following format:

report_card_{subject}_{grade_level}.txt

## Example

If your CSV file is named gradesM3_SC.csv and the template file is named text/SC_S1_2223_M3.txt, running the command python report_generator.py M# SCIENCE will create report cards like report_card_SC_M3.txt, or report_card_CHE_M4.txt, and so on, for each student listed in the CSV file. The program will print the whole class in a single txt file.

This Python program automates the generation of report cards for IB MYP subjects, streamlining the process for educators.

# Further Coding Detail

## report_generator.py

## Generate Comment (Main Function)

### setting variables

The variables is taken from the argument in comand line.
Variable needed are name, gender, grade achievement for criterion A, B, C and D.

From the gender received, the code will setup the gender words that will be use accordingly. Example male will use he, He, his and him and female will use she, She and her. For the sake of simplicity other kind of gender are not acceptable. Maybe something to be improve in the future.

### Calling comments from the preset_report_template.py

Here is where the templates string are called from the file preset_report_template.py

Each string will be call using function and assign to variables accordingly. Example crit_a_strong will take report templates for crit A and strings for high achiever student. While crit_d_weak will take report template for crit d and strings for weaker student.

### Main algorithm for selecting comments

There is 4 criterion and 3 achievement level. The students will achieve in a range from 1 to 8. The range 1 - 4 will be consider weak, range 5-6 are average and 7-8 are strongs.

Using For loop, the program will choose what is the grade achieve by the students and asign a comment accordingly. Example:

A student who achieve 6 for crit A. The program will identify that grade a is 6 hence it is an average achievement. So it will be assign to crit_a_average to assign comment. The comment assign will be choosen randomly suitable from the template. There are several selection of string to be choosen for each achievement level. This will add variety to final report produced.

After all for criteria comment has been choosen, All the comment will be combine together to create a long cohesive report card for the students.

The main function will return this comments for printing into txt file.

## Random Sentence Selector function

This funtion select a random number from 0 to the number of variety comment available to be choose from. This will be use to add variety to the report generated.

## Generate Report Card function

This function initially load the students data from a csv file. It will then read the name of each student and generate report for each student using the generate_comment function.

This function then will collect all the comment and print them as a single txt file output. It will print by classes as the input file are seperate for each grade level.

## Calling Argument and Setting the input output file

Final code here are use to read the subject and grade level given in the argument for command line. Both argument will be used to call the correct name for input csv file and use to also name the output file.

The last and final code is the run the whole code.

## Update log

Here I update the date and changes I made through out the program.

Author note: This program is initially made for me to ease a repetative process that I have to do as a teacher. As I learn more thorugh CS50 course, I have an idea to create this program. Some part of me also lazy to rewrite the templates. Hence this program is created. I use this program as a submission for my Project as I already worked on it and it will reduce the time for me to work on other new programming projects.

## preset_report_template.py

## Variable

There is only 2 needed variables. I have problem calling the variables from the report_generator.py as it will create a circular reference. Hence for now I hard coded the variables here which will be need to be change if user need to choose a different template.

The variable are subject and level for grade level.

## Calling the template read_text function

This function use to call the template txt file using the variable setup previously.  The function will parse the comment from the template file and extract the comments from different achievement levels (weak, average, strong) for each criterion.

key: stores the current criterion being read

grade: stores the current achievement level

criterion: A dictionary of dictionaries that will hold the extracted comments.

If the line contains "COMMENTS", it sets the key to the current criterion name, indicating the start of a new section for comments related to a specific criterion.

Otherwise, if the line is not empty:
If the line is in the format "GRADE=Weak/Average/Strong", it sets the grade to the corresponding achievement level.

If the line format doesn't match a criterion or achievement level, it assumes it's a comment.
It splits the line on "=" and gets the comment text on the right side.
It replaces placeholders in the comment text:
{name}: Replaced with the student's name (likely from another file).
{gender2}, {gender3}, {gender4}: Replaced with appropriate gender pronouns based on the student's gender information (format of these placeholders might need confirmation).
The processed comment is added to the appropriate list within the criterion dictionary based on the current key (criterion name) and grade (achievement level).

After processing all lines, the function returns the final criterion dictionary containing all extracted comments for each criterion and achievement level.

## Returning the function back to report_generator.py

The functions here will return back the strings that has been parse placing {name}, {gender1}, {gender2}, {gender3}, {gender4} to be use to generate the report.

report_generator.py will replace each {variables} for occordingly for each students.
