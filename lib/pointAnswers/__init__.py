def decode_alternatives(value):
    """Decompõe um número em potências de 2 (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)"""
    alternatives = list()
    while value > 0:
        if value >= 512:
            value -= 512
            alternatives.append(512)
        elif value >= 256:
            value -= 256
            alternatives.append(256)
        elif value >= 128:
            value -= 128
            alternatives.append(128)
        elif value >= 64:
            value -= 64
            alternatives.append(64)
        elif value >= 32:
            value -= 32
            alternatives.append(32)
        elif value >= 16:
            value -= 16
            alternatives.append(16)
        elif value >= 8:
            value -= 8
            alternatives.append(8)
        elif value >= 4:
            value -= 4
            alternatives.append(4)
        elif value >= 2:
            value -= 2
            alternatives.append(2)
        elif value >= 1:
            value -= 1
            alternatives.append(1)
        else:
            break
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
    
    # Se o aluno selecionou alguma alternativa que não existe no gabarito, zera a questão
    for a in alt_decoded:
        if a not in correct_decoded:
            return 0.0

    # Contar quantas alternativas do aluno são corretas
    countCorrect = sum(1 for i in alt_decoded if i in correct_decoded)

    # Calcular pontos desta questão
    # Dividimos os pontos da questão pela quantidade de alternativas corretas (gabarito)
    if len(correct_decoded) > 0:
        pointsPerAlternative = pointsForQuestion / len(correct_decoded)
        questionPoint = pointsPerAlternative * countCorrect
    else:
        questionPoint = 0.0

    return questionPoint


def answer(alternatives_array, correctAlternatives_array, pointsForQuestion):
    """Calcula a pontuação comparando respostas com gabarito

    Args:
        alternatives_array (array): array com respostas do aluno
        correctAlternatives_array (array): array com respostas corretas
        pointsForQuestion (int): pontos disponíveis por questão
    """
    totalPoints = 0
    
    for question_num, (alt, correct) in enumerate(zip(alternatives_array, correctAlternatives_array), start=1):
        questionPoint = answer_single_question(alt, correct, pointsForQuestion)
        totalPoints += questionPoint
        print(f'Question {question_num} - {questionPoint}')
    
    return totalPoints