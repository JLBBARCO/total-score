import pandas as pd
import sys
from lib import pointAnswers

# Try to read answer files (CSV first, then TSV as fallback)
try:
    answerFile = pd.read_csv('answer.csv', sep=';')
    answerKeyFile = pd.read_csv('answer_key.csv', sep=';')
except FileNotFoundError:
    try:
        answerFile = pd.read_csv('answer.tsv', sep=';')
        answerKeyFile = pd.read_csv('answer_key.tsv', sep=';')
    except FileNotFoundError:
        print('None of the files answer.csv, answer_key.csv, answer.tsv, or answer_key.tsv were found.')
        sys.exit()
    except Exception as e:
        print('An error occurred while trying to read answer.tsv or answer_key.tsv:', e)
        sys.exit()
except Exception as e:
    print('An error occurred while trying to read answer.csv or answer_key.csv:', e)
    sys.exit(1)

# Remove spaces from column names
answerFile.columns = answerFile.columns.str.strip()
answerKeyFile.columns = answerKeyFile.columns.str.strip()

# Check if "Class" column exists
if 'Class' not in answerKeyFile.columns:
    print("Column 'Class' was not found in answer_key file.")
    class_column_exists = False
else:
    class_column_exists = True

score_total = int(input('Enter the total score for the test: '))
num_questions = len(answerKeyFile)
score_per_question = score_total / num_questions

student_answers = pd.to_numeric(answerFile['Answer'].astype(str).str.strip(), errors='coerce').fillna(0).astype(int)
correct_answers = pd.to_numeric(answerKeyFile['Answer'].astype(str).str.strip(), errors='coerce').fillna(0).astype(int)

scores_per_question = []
total_score = 0.0

# Dictionary to keep total per subject (Class)
class_scores = {}

with open('result.txt', 'a', encoding='utf-8') as f:
    f.write('--- New run ---\n')
    for idx, (q_label, student, correct) in enumerate(zip(answerFile['Question'], student_answers, correct_answers), start=1):
        q_score = pointAnswers.answer_single_question(student, correct, score_per_question)
        scores_per_question.append(q_score)
        total_score += q_score
        print(f'Question {idx} ({q_label}) - {q_score}')
        f.write(f'Question {idx} ({q_label}) - {q_score}\n')

        # Add the score to the respective class total
        if class_column_exists:
            class_name = answerKeyFile['Class'].iloc[idx-1]
            if class_name not in class_scores:
                class_scores[class_name] = q_score
            else:
                class_scores[class_name] += q_score

    # Write class score summary if available
    if class_column_exists:
        f.write('Score per subject (Class):\n')
        for cls, pts in class_scores.items():
            f.write(f'{cls}: {pts}\n')

    f.write(f'Total Score: {total_score}\n\n')

# Also print class scores to console
if class_column_exists:
    print('\nScore per subject (Class):')
    for cls, pts in class_scores.items():
        print(f'{cls}: {pts}')

print(f'\nTotal Score: {total_score}')