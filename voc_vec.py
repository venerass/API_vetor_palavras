def gerador_voc_1(texto,vocabulario = []):
    texto = texto.replace('.','').replace('-',' ').lower().split()
    vocabulario_1 = [v for v in vocabulario]
    [vocabulario_1.append(palavra) for palavra in texto if palavra not in vocabulario_1]
    return vocabulario_1

def gerador_voc_2(texto,vocabulario = []):
    texto = texto.replace('.','').replace('-',' ').lower().split()
    vocabulario_2 = [v for v in vocabulario]
    gram_texto = [' '.join(texto[i:i+2]) for i  in range(len(texto))][:-1]
    [vocabulario_2.append(v) for v in gram_texto if v not in vocabulario_2]
    return vocabulario_2

def gerador_vetor_freq_1(texto,vocabulario):
    texto = texto.replace('.','').replace('-',' ').lower().split()
    vetor_text = []
    vetor_text = [str(texto.count(v)) for v in vocabulario]
    return vetor_text

def gerador_vetor_freq_2(texto,vocabulario_2):
    texto = texto.replace('.','').replace('-',' ').lower().split()
    repetido = [' '.join(texto[i:i+2]) for i  in range(len(texto))][:-1]
    freq_2 = [str(repetido.count(v)) for v in vocabulario_2]
    return freq_2