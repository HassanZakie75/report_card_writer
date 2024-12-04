# Report card writer for MYP 2 Science by Hassan Zakie Yusoff 
# version: 3.12.2024
import random
import csv

def generate_comment(student):
    """Generates subject comments based on name, gender, and grades.

    Args:
        name: The student's name.
        gender: The student's gender (male or female).
        grade_a: The grade for criterion A.
        grade_b: The grade for criterion B.
        grade_c: The grade for criterion C.
        grade_d: The grade for criterion D.

    Returns:
        A dictionary containing subject comments for each criterion.
    """
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

        #template for report writing
    crit_a_weak = [
            f"{name} uses scientific knowledge and insight to offer solutions to challenges that occur in everyday life. {gender4} also uses information to make decisions with the help of {gender2} teacher.",
            f"By completing worksheets assigned as homework, {name} is encouraged to revisit subject and concepts. In addition, {gender1} should make an attempt to read the material and take effective notes in class strategies like Cornell note-taking/Collaborative note-making/Note-taking/mapping/T-Notes method/5R's of Notes/Sketchnote/Visual Note-taking.",
            f"{name} is also strongly encouraged to consult the teacher and peers on a regular basis in hopes of gaining a deeper understanding of the subject at hand so that {gender1} is able to state and apply scientific knowledge and understanding to solve problems set in familiar situations."
            ]
    crit_a_average = [
            f"{name} can recollect and convey scientific information and understanding to solve problems set in familiar situations. {gender4} also applies information to make scientifically supported judgments with some examples and explanations, though this may not be consistent. {gender4} is encouraged to consistently review the content and concepts by completing worksheets given as homework/post lessons.",
            f"{name} should frequently make an effort to read the textbook and make effective summary notes for studying using the Cornell note-taking method so that {gender2} is able to apply scientific knowledge and understanding to solve problems set in familiar situations and suggest solutions to problems set in unfamiliar situations."
            ]
    crit_a_strong = [
            f"{name} is able to outline and analyze scientific knowledge to solve problems set in familiar situations and unfamiliar situations. {gender4} interprets information to make scientifically supported arguments by giving a detailed justification of opinions and ideas with a range of examples, and thorough explanations. {gender4} also uses accurate terminology.Well done! Keep up the good work!",
            f"{name} is expected to continue exploring challenging ideas to further deepened conceptual understanding. {gender4} could adopt the See Think Wonder model and or Question Starters which enables {gender3} to constantly connect to {gender2} prior knowledge and generate ideas and develop curiosity.Well done! Keep up the good work!"
            ]

    crit_b_weak = [
            f"{name} states a problem or question to be tested by a scientific investigation. {gender4} outlines a testable hypothesis using scientific reasoning and knows how to manipulate the variables. {gender4} states how relevant data is collected and designs a safe method.",
            f"{name} needs to practice writing hypotheses with complete scientific reasoning. Also, needs to practice describing how the variables are manipulated for the experiment using the guiding questions in the task sheet.",
            f"{name} needs to practice writing hypotheses using guiding questions in the task sheet/lab template. ",
            f"To maximize the standard of work submitted, he is advised to do a self-assessment using the rubrics provided.",
            f"{name} is encouraged to do self-checking using the checklist given in the task sheet before the final submission.",
            f"{name} is advised to submit the draft to the teacher for constructive feedback.",
            f"{name} is encouraged to take part in the class discussion to deepen {gender2} understanding and acquire skills to develop effective scientific investigation."
        ]
    crit_b_average = [
            f"{name} outline a problem or question to be tested by a scientific investigation. {gender4} explains a testable hypothesis using scientific reasoning. {gender4} outlines how to manipulate the variables and also outlines how relevant data is collected. {gender4} designs a safe and complete method in which he selects appropriate materials and equipment.",
	    f"{name} is encouraged to practice core components needed in an experiment in a different context.",
            f"To improve the hypothesis writing, he is advised to explain the hypothesis using different variables and scientific reason.",
            f"{name} is encouraged to initiate class discussions to deepen {gender2} understanding and acquire skills to develop effective scientific investigation.",
            f"{name} is encouraged to design and refine the experiment using ATL skill PDCA.",
            f"{name} is advised to submit the draft to the teacher for constructive feedback.",
            f"{name} is encouraged to do self-checking using the checklist given in the task sheet before the final submission.",
            f"A more logical, complete, and safe method is needed to improve the quality of the experiment. This can be done by exploring more scientific investigation via Phet or Science buddies website.",
        ]
    crit_b_strong = f"{name} describes a problem or a question to be tested by a scientific investigation. {gender4} explains a testable hypothesis using scientific reasoning and also describes how to manipulate the variables. {gender1} describes how sufficient, relevant data is collected as well as design a logical, complete and safe method in which he selects materials and equipment. Well done! Keep up the good work!"

    crit_c_weak = [
            f"{name} could collect and present the data correctly either in numbers or visual formats. {gender4} analyses the facts and claims the validity of the hypothesis as well as the approach. {gender4} can suggest modifications to the method, but with little reference to scientific research.",
            f"{gender1} has to work on {gender2} data presentation skills by learning how to organize and present data using correct graphical representations such as bar graphs or line graphs.",
            f"{gender1} is encouraged to interpret data and outline results using scientific reasoning that he learned in the lesson.",
            f"{gender1} is advised to outline the validity of a method based on the outcome of a scientific investigation. This can be done by doing a self/peer assessment after the experiment.",
            f"{gender1} is advised to submit the draft to the teacher for constructive feedback",
            f"{gender1} is advised to explore the method that would benefit the scientific investigation",
            f"{gender1} should also focus on {gender2} comprehension of scientific vocabulary and refer to rubrics to achieve the task-specific requirements or expectations."
            ]
    crit_c_average = [
            f"{name} could collect, organize and present data in numerical and/or visual forms. {gender4} could interpret data and outline results using scientific reasoning accurately. In addition, he outlines the validity of a prediction and method based on the outcome of a scientific investigation. Finally, he is able to outline the validity of the method and suggest improvement based on the outcome of a scientific investigation.",
            f"{name} is encouraged to transform the data and interpret the results using scientific reasoning that he learned in the lesson.",
            f"{name} is encouraged to give constructive suggestions to improve the validity of a method based on the outcome of a scientific investigation. This can be done by doing a discussion after the experiment with teacher or peer.",
            f"{name} should also master data interpretation skills like graph drawing and data tabulation. This could be done by exploring more experiments via reference book, Phet online simulation."
            ]
    crit_c_strong = f"{name} could collect, organize, transform, and present data in numerical and/or visual forms. {gender4} is able to interpret data and outlines results using correct scientific reasoning accurately. {gender4} also discusses the validity of a hypothesis and the methodology of a scientific investigation. {gender4} describes improvements or extensions to the method that would benefit the scientific investigation. {gender4} is expected to follow the same consistency when processing and evaluating scientific investigations. Well done! Keep up the good work!"
    
    crit_d_weak = [
            f"{name} has stated how science is used to solve a particular problem or situation. {gender4} demonstrates the consequences of applying science to a specific problem. {gender4} tries to communicate information using scientific terminology, but he had limited success. Moreover, he documents the sources with a teacher's guidance.",
            f"{name} is encouraged to read science news in a variety of media on a daily basis. {gender4} is also encouraged to use the guided example provided in class to practice researching.",
            f"It is strongly recommended that the student review the rubrics provided for each activity before submitting their work in order to improve the quality of {gender2} work. {gender4} could use criterion D sentence starters/templates to enhance {gender2} information literacy skills he could create references and citations using strategies such as MLA 8 Poster/ In-text citation/ Citation for beginners."
            ]
    crit_d_average = [
            f"{name} outlines the ways in which science is used to address a specific problem or {gender2} outlines the implicatfions of using science to solve that specific problem. {gender4} sometimes applies scientific language to communicate understanding and sometimes documents sources correctly.",
            f"{name} is encouraged to broaden {gender2} scientific knowledge by reading scientific journals and watching scientific films on YouTube and in plenty of other ways. Grades will improve if you go over the rubrics before submitting work to ensure that all of the needed components are addressed.",
            f"When {name} writes, {gender1} is encouraged to use more scientific language as this will allow {gender3} to describe the ways science is used to address a specific problem or issue. {gender4} could use criterion D sentence starters/templates to enhance information literacy skills."
            ]
    crit_d_strong = f"{name} describes the ways in which science is used to address a specific problem or issue. {gender4} describes and analyses the implications of using science to solve for a specific problem. {gender4} consistently applies scientific language to communicate understanding clearly and accurately documents sources. Well done! Keep up the good work!"
    

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

        comments = commentA + commentB + commentC + commentD + '\n' + '\n'

    return comments

def random_sentence_selector(sentences):
    """Selects and returns a random sentence from a given list of sentences.

    Args:
      sentences: A list of sentences.

    Returns:
      A randomly selected sentence.
    """

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
input_csv = 'grades.csv'
output_txt = 'report_cardsM2_new.txt'
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