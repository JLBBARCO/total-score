from random import randint

subjects = [
    'Mathematics', 'Chemical', 'Physic', 'Biology', 'English', 'Portuguese', 
    'Spanish', 'French', 'Philosophy', 'Sociology', 'Geography', 'History', 
    'Financial Education', 'Physical Education'
]

num_questions = int(input('Enter the number of questions: '))
test_score = int(input('Enter the total test score: '))

score_per_question = test_score / num_questions

counter = 0
with open('answer_key.csv', 'a', encoding='utf-8') as f:
    f.write('Score;Question;Answer;Class\n')
    print('Score;Question;Answer;Class')
    total_score_str = str(test_score)
    f.write(total_score_str)
    print(total_score_str)
    while counter < num_questions:
        counter += 1
        answer_score = randint(0, 1023)
        subject_index = randint(0, len(subjects) - 1)
        subject = subjects[subject_index]

        f.write(f';{counter};{answer_score};{subject}\n')
        print(f';{counter};{answer_score};{subject}')

counter = 0
with open('answer.csv', 'a', encoding='utf-8') as f:
    f.write('Question;Answer;Class\n')
    print('Question;Answer;Class\n')
    while counter < num_questions:
        counter += 1
        answer_score = randint(0, 1023)
        subject_index = randint(0, len(subjects) - 1)
        subject = subjects[subject_index]

        f.write(f'{counter};{answer_score};{subject}\n')
        print(f'{counter};{answer_score};{subject}')
