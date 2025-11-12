# Importations
import pandas as pd
from lib import pointAnswers

# Read Files
try:
    answerFile = pd.read_csv('answer.csv')
    answerKeyFile = pd.read_csv('answer_key.csv', sep=';')
except FileNotFoundError:
    print('File Not Found')

# Limpar espaços nas colunas
answerFile.columns = answerFile.columns.str.strip()
answerKeyFile.columns = answerKeyFile.columns.str.strip()

# System
points = int(input('Input score of the test: '))
# Número de questões baseado no gabarito
num_questions = len(answerKeyFile)
pointsPerQuestion = points / num_questions

# Garantir que os valores de 'Answer' sejam inteiros (removendo espaços)
ans_values = pd.to_numeric(answerFile['Answer'].astype(str).str.strip(), errors='coerce').fillna(0).astype(int)
key_values = pd.to_numeric(answerKeyFile['Answer'].astype(str).str.strip(), errors='coerce').fillna(0).astype(int)

score_for_each = []
totalScore = 0.0

# Abrir arquivo de resultado em modo append e gravar histórico por questão
with open('result.txt', 'a', encoding='utf-8') as f:
    f.write('--- New run ---\n')
    for idx, (q_label, student, correct) in enumerate(zip(answerFile['Question'], ans_values, key_values), start=1):
        qpoint = pointAnswers.answer_single_question(student, correct, pointsPerQuestion)
        score_for_each.append(qpoint)
        totalScore += qpoint
        # Mostrar em tempo real
        print(f'Question {idx} ({q_label}) - {qpoint}')
        # Gravar no histórico
        f.write(f'Question {idx} ({q_label}) - {qpoint}\n')
    f.write(f'Total Score: {totalScore}\n\n')

print(f'\nTotal Score: {totalScore}')
