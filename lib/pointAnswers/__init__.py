def decode_alternatives(value):
    """Decompõe um número em potências de 2 (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)"""
    # Lista com as potências de 2 possíveis na sua prova
    possible_powers = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    alternatives = list()
    
    # Passa uma única vez por cada potência, da maior para a menor
    for power in possible_powers:
        if value >= power:
            alternatives.append(power)
            value -= power
            
    return alternatives


def answer_single_question(alt, correct, pointsForQuestion):
    """Calcula pontuação de uma única questão
    
    Args:
        alt (int): resposta do aluno
        correct (int): resposta correta
        pointsForQuestion (float): pontos disponíveis
        
    Returns:
        float: pontos obtidos nesta questão
    """
    # Decodificar alternativas
    alt_decoded = decode_alternatives(int(alt))
    correct_decoded = decode_alternatives(int(correct))
    
    # Se o aluno não assinalou nada, a nota é 0.0
    if not alt_decoded:
        return 0.0
        
    # Se o aluno selecionou alguma alternativa que não existe no gabarito, zera a questão
    for a in alt_decoded:
        if a not in correct_decoded:
            return 0.0

    # Contar quantas alternativas do aluno são corretas
    countCorrect = sum(1 for i in alt_decoded if i in correct_decoded)

    # Calcular pontos desta questão
    if len(correct_decoded) > 0:
        pointsPerAlternative = pointsForQuestion / len(correct_decoded)
        questionPoint = pointsPerAlternative * countCorrect
    else:
        questionPoint = 0.0

    return questionPoint


def answer(alternatives_array, correctAlternatives_array, pointsForQuestion):
    """Calcula a pontuação comparando respostas com gabarito"""
    totalPoints = 0
    
    for question_num, (alt, correct) in enumerate(zip(alternatives_array, correctAlternatives_array), start=1):
        questionPoint = answer_single_question(alt, correct, pointsForQuestion)
        totalPoints += questionPoint
        print(f'Question {question_num} - {questionPoint}')
    
    return totalPoints