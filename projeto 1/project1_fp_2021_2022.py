'''
Raquel Cardoso - ist199314
raquelfmcardoso@tecnico.ulisboa.pt
5 de Novembro de 2021
'''
 

''' corrigir_palavra: cad. carateres -> cad. carateres '''
''' a funcao corrigir_palavra recebe uma palavra (cadeia de caracteres) que pode
ter sofrido um surto de letras e aplica as reducoes necessarias para a corrigir.
'''

def corrigir_palavra(cad_c):

    i = 0
    count = 0
    
    while i < len(cad_c) - 1:
        c1 = cad_c[i].lower()
        c2 = cad_c[i+1].lower()
        
        '''desta forma podemos ver se sao a mesma letra mais facilmente'''
        if ((cad_c[i].isupper() and cad_c[i+1].islower()) or \
           (cad_c[i].islower() and cad_c[i+1].isupper())) and c1 == c2: 
            ''' sao a mesma letra mas nao sao ambas maisculas ou minusculas,\
            encontramos um erro'''
            count = i + 2
            cad_c = cad_c[:i] + cad_c[count:]
            if i != 0:
                i -= 1
        else:
            i += 1
    return cad_c



''' eh_anagrama: cad. carateres x cad. carateres -> booleano '''
''' a funcao eh_anagrama recebe duas palavras e se forem um anagrama uma da\
outra devolve True. '''

def eh_anagrama(cad_c, cad_c2):
    
    ''' nao existem diferenciacoes entre maisculas e minusculas. sendo assim,\
    e mais pratico transformar ambas em tudo minusculas (ou maisculas). '''    
    palavra_um = cad_c.lower()
    palavra_dois = cad_c2.lower()
    
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    
    ''' se as palavras nao forem a mesma mas tiverem o mesmo numero de cada\
    letra no alfabeto, temos um anagrama. '''
    if len(palavra_um) != len(palavra_dois) or palavra_um == palavra_dois:
        return False

    for e in range(0, len(lst)):
        if palavra_um.count(lst[e]) != palavra_dois.count(lst[e]):
            return False
    return True



''' corrigir_doc: cad. carateres -> cad. carateres '''
''' a funcao corrigir_doc recebe um texto (documento) que contem palavras que\
podem ter sofrido um surto de letras. apos as alteracoes para corrigir as \
palavras vitimas do surto, analisamos a existencia de anagramas e retiramo-los.
caso o argumento nao seja correspondente a um texto com erros da documentacao\
BDB, geramos um erro.
as palavras apenas podem estar separadas por um unico espaco, o texto esta\
formado por uma ou mais palavras, e cada palavra e formada apenas por pelo menos\
uma letra. '''

def corrigir_doc(cad_c):
    
    n = 0
    res = ''
    
    ''' encontrar todas as entradas invalidas. '''
    if not isinstance(cad_c, str) or cad_c.isspace():
        raise ValueError("corrigir_doc: argumento invalido")
    
    
    for i in range(0, len(cad_c)):
        if (ord(cad_c[i]) < 31) or (90 < ord(cad_c[i]) < 97) or \
           (ord(cad_c[i]) > 122) or (33 < ord(cad_c[i]) < 65):
            raise ValueError("corrigir_doc: argumento invalido")
        
    while n < len(cad_c)-1:
        if cad_c[n].isspace():
            if cad_c[n+1].isspace():
                raise ValueError("corrigir_doc: argumento invalido")
        n = n+1
    
    ''' corrigimos primeiro o surto de letras no documento. '''
    palavras = cad_c.split()
    for i in range(0, len(palavras)):
        palavras[i] = corrigir_palavra(palavras[i])
        
    ''' removemos os anagramas presentes no documento corrigido. '''
    for i in range(0, len(palavras)):
        for j in range(i, len(palavras)-1):
            if eh_anagrama(palavras[i], palavras[j]):
                palavras.pop(j)
            if eh_anagrama(palavras[j], palavras[len(palavras)-1]):
                if palavras[len(palavras)-1] in palavras[:len(palavras)-1]:
                    palavras.pop(j)
                else:
                    palavras.pop(len(palavras)-1)
                    
    ''' adicionamos as palavras restantes ao resultado final. '''
    for i in range(0, len(palavras)):
        if i != len(palavras)-1:
            res += palavras[i] + ' '
        else:
            res += palavras[i]
    return res



''' obter_posicao: cad. carateres x inteiro -> inteiro '''
''' a funcao obter_posicao recebe uma cadeia de caracteres que representa um\
movimento ('C', 'B', 'D', 'E') e um inteiro de 1-9 e devolve o inteiro apos\
o movimento que a cadeia de caracteres significa. numa tabela 3x3: 'C' =\
um numero acima, 'B' = um numero abaixo, 'D' = um numero a frente e 'E' =\
um numero atras. se o movimento nao for possivel, devolvemos o inteiro inicial.
'''

def obter_posicao(cad_c, n):
    
    if cad_c == 'C':
        if n in [1,2,3]:
            return n
        return n-3
    
    if cad_c == 'B':
        if n in [7,8,9]:
            return n
        return n+3   
    
    if cad_c == 'D':
        if n in [3,6,9]:
            return n
        return n+1  
    
    if cad_c == 'E':
        if n in [1,4,7]:
            return n
        return n-1
    return n



''' obter_digito: cad. carateres x inteiro -> inteiro '''
''' a funcao obter_digito recebe um conjunto de sequencias e um inteiro que\
corresponde a posicao inicial e devolve a posicao final do digito apos a\
sequencia de movimentos recebida. '''

def obter_digito(cad_c, dig):
    
    ''' ao consequentemente substituir o valor do dig, conseguimos encontrar o\
    digito final no final do forloop. '''
    for i in range(0, len(cad_c)):
        dig = obter_posicao(cad_c[i], dig)
    return dig



''' obter_pin: tuplo -> tuplo '''
''' a funcao obter_pin recebe um tuplo com multiplos movimentos que correspondem\
ao obter_digito desse movimento. a primeira entrada todo como posicao inicial, 5\
e as seguintes tomam como posicao inicial o resultado do indice anterior. se\
o argumento nao for um tuplo com comprimento entre 4 e 10 e cada movimento nao\
for uma string com 1 ou mais caracteres 'C'. 'B', 'D', 'E', geramos um erro. '''

def obter_pin(tpl):
    
    dig = 5
    res = ()
    
    ''' encontrar todas as entradas invalidas e os digitos finais de cada el\
    do tuplo. '''
    if not isinstance(tpl, tuple) or not 4 <= len(tpl) <= 10:
        raise ValueError("obter_pin: argumento invalido")
    
    for el in tpl:
        if len(el) < 1:
            raise ValueError("obter_pin: argumento invalido")
        for el2 in el:
            if el2 not in ['C', 'B', 'D', 'E']:
                raise ValueError("obter_pin: argumento invalido")
        dig = obter_digito(el, dig)
        res += (dig,)
        
    return res



''' eh_entrada: universal -> booleano '''
''' a funcao eh_entrada recebe um argumento universal e verificamos se \
corresponde a uma entrada da BDB. se for, devolvemos True. para ser entrada, e \
preciso ser um tuplo com comprimento 3: cifra, sequencia de controlo e \
sequencia de seguranca '''

def eh_entrada(tpl):
    
    ''' encontrar todos os casos falsos e se a entrada nao corresponder a nenhum\
    deles, entao e verdadeira '''
    if not isinstance(tpl, tuple) or len(tpl)!=3:
        return False
    
    if not isinstance(tpl[0], str) or not isinstance(tpl[1], str) or not\
       isinstance(tpl[2], tuple) or len(tpl[1]) != 7 or len(tpl[2]) < 2:
        return False
    
    
    for el in tpl[0]:
        if el in ['0','1','2','3','4','5','6','7','8','9'] or el.isspace():
            return False

    lst = tpl[0].split("-")
    for el in lst:
        if not el.islower():
            return False
        
    if tpl[1][0] != '[' or tpl[1][6] != ']':
        return False

    for i in range(1, 6):
        if not tpl[1][i].islower():
            return False
    for i in range(0, len(tpl[2])):
        if not isinstance(tpl[2][i], int) or tpl[2][i]< 0:
            return False

    return True



''' validar_cifra: cad. carateres x cad. carateres -> booleano '''
''' a funcao validar_cifra recebe uma cifra e sequencia de controlo e devolve\
True se a sequencia de controlo esta correta de acordo com a cifra. '''

def validar_cifra(cad_c, cad_c2):
    
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letra_n = {}
    cad_c2 = cad_c2[1:6]
    letras = ''
    
    for i in range(0, len(lst)):
        letra_n[lst[i]] = cad_c.count(lst[i])
    
    ''' organizamos por numero de ocorrencia > alfabeticamente e ficamos com os\
    5 primeiros valores. '''
    letra_n_sorted = sorted(letra_n.items(), key=lambda ln: ln[1], reverse=True)
    letra_n_sorted = letra_n_sorted[0:5]
    
    for i in range(0,5):
        letras += letra_n_sorted[i][0]
        
    ''' se a string que contem as 5 letras que aparecem mais vezes ordenadas por\
    numero de vezes que apareceu > alfabeticamente for igual a cifra, ent e\
    valida. '''
    if letras == cad_c2:
        return True
    return False



''' filtrar_bdb: lista -> lista '''
''' a funcao filtrar_bdb recebe uma lista contendo pelo menos uma entrada da\
BDB e devolve a lista das entradas em que o checksum nao e coerente com a cifra\
correspondente, na mesma ordem da lista original. se o argumento nao for uma\
lista de entradas da BDB, geramos um erro.'''

def filtrar_bdb(lst):
    
    if not isinstance(lst, list) or len(lst) < 1:
        raise ValueError("filtrar_bdb: argumento invalido")
    
    
    res = []
    for el in lst:
        if not eh_entrada(el):
            raise ValueError("filtrar_bdb: argumento invalido")
        ''' se a cifra nao corresponder, adicionamos a lista de entradas final.
        '''
        if not validar_cifra(el[0], el[1]):
            res += (el),
    return res



''' obter_num_seguranca: tuplo -> inteiro '''
''' a funcao obter_num_seguranca recebe um tuplo de numeros inteiros positivos e\
e devolve o numero de seguranca: a menor diferenca positiva entre qualquer par\
de numeros. '''

def obter_num_seguranca(tpl):
    
    dif = []
    pos = []
    
    for i in range(0, len(tpl)):
        for j in range(0, len(tpl)):
            diferenca = tpl[i]-tpl[j]
            dif.append(diferenca)
            
    for i in range(0, len(dif)):
        if dif[i]> 0:
            pos.append(dif[i])
            
    return min(pos)



''' decifrar_texto: cad. carateres x inteiro -> cad. carateres '''
''' a funcao decifrar_texto recebe uma cifra e um numero de seguranca e devolve\
o texto decifrado. '''

def decifrar_texto(cad_c, n):
    
    somar = (n%26)
    ''' o resto inteiro de n a dividir por 26 da-nos o indice na lista do\
    alfabeto. '''
    par = somar+1
    impar = somar-1
    res = ''
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic = {}
    
    for i in range(0, len(lst)):
        ''' lst[0] = a, mas a e a primeira letra do alfabeto. '''
        dic[lst[i]] = i+1
        
    for j in range(0,len(cad_c)):
        ''' cada - e um espaco. '''
        if cad_c[j] == '-':
            res += ' '
        else:
            if j%2 == 0:
                novo_numero = dic[cad_c[j]]+par
                if novo_numero > 26:
                    novo_numero = novo_numero%26  
            if j%2 == 1:
                novo_numero = dic[cad_c[j]]+impar
                if novo_numero > 26:
                    novo_numero = novo_numero%26
            for (letra, numero) in dic.items():
                if numero == novo_numero:
                    nova_letra = letra
            res += nova_letra
            
    return res



''' decifrar_bdb: lista -> lista '''
''' a funcao decifrar_bdb recebe uma lista com pelo menos uma entrada da bdb e
devolve uma lista com o texto decifrado de cada uma das entradas, em cada\
entrada. se o argumento nao for uma lista com pelo menos uma entrada da bdb,\
geramos um erro. '''

def decifrar_bdb(lst):
    
    res = []
    if not isinstance(lst, list) or len(lst) < 1:
        raise ValueError('decifrar_bdb: argumento invalido')
    
    for el in lst:
        if not eh_entrada(el):
            raise ValueError('decifrar_bdb: argumento invalido')
        
        num_seg = obter_num_seguranca(el[2])
        cifra = el[0]
        res += decifrar_texto(cifra, num_seg),
        
    return res



''' eh_utilizador: universal -> booleano '''
''' a funcao eh_utilizador recebe um argumento universal e verifica se\
corresponde a um utilizador da BDB. para tal, e necessario ser um dicionario com\
nome, senha e regra individual. nomes e senhas devem ter tamanho minimo um e\
podem conter qualquer caracter. '''

def eh_utilizador(dic):
    
    ''' encontrar todos os casos falsos e se a entrada nao corresponder a nenhum\
    deles, entao e verdadeira. '''    
    if not isinstance(dic, dict) or len(dic) != 3:
        return False
    
    if not isinstance(dic['name'], str) or not isinstance(dic['pass'], str)\
       or not isinstance(dic['rule'], dict):
        return False
    
    if len(dic['rule']) != 2 or not isinstance(dic['rule']['vals'], tuple) or \
       len(dic['rule']['vals']) != 2 or not \
       isinstance(dic['rule']['char'], str) or len(dic['rule']['char']) != 1:
        return False
    
    if not isinstance(dic['rule']['vals'][0], int) or not\
       isinstance(dic['rule']['vals'][1], int):
        return False
    
    if dic['rule']['vals'][0] <= 0 or dic['rule']['vals'][1] <= 0 or \
       dic['rule']['vals'][0] > dic['rule']['vals'][1]:
        return False
    
    if len(dic['name']) < 1 or len(dic['pass']) < 1 or not \
       dic['rule']['char'].islower():
        return False
    
    return True



''' eh_senha_valida: cad. carateres x dicionario -> booleano '''
''' a funcao eh_senha_valida recebe uma senha e um dicionario com a regra\
individual para criar a senha. sera valida se cumprir a regra individual e as\
gerais.'''

def eh_senha_valida(cad_c, dic):
    
    minimo = dic['vals'][0]
    maximo = dic['vals'][1]
    letra = dic['char']
    i = 0
    j = 0
    
    ''' numeros de vogais minusculas contabilizadas. '''
    counter = cad_c.count('a')+cad_c.count('e')+cad_c.count('i')+\
        cad_c.count('o')+cad_c.count('u')
    
    ''' verificar se a letra em 'char' aparece um numero de vezes entre o minimo\
    e o maximo. '''
    for el in range(minimo, maximo+1):
        if cad_c.count(letra) == el:
            i = 1
            
    ''' verificar se aparece pelo menos uma vez dois caracteres iguais seguidos.
    '''        
    for el in range(32, 127):
        if chr(el)+chr(el) in cad_c:
            j += 1
            
    if i != 1 or counter < 3 or j < 1:
        return False
    return True



''' filtrar_senhas: lista -> lista '''
''' a funcao filtrar_senhas recebe uma lista pelo menos um dicionario\
correspondente as entrasas da BDB, e devolve a lista ordenada alfabeticamente\
dos nomes dos utilizadores que tem senhas erradas. se o argumento nao for uma\
lista contendo entradas da BDB, geramos um erro. '''

def filtrar_senhas(lst):
    
    res = []
    if not isinstance(lst, list) or len(lst) < 1:
        raise ValueError('filtrar_senhas: argumento invalido')
    
    for el in lst:
        if not isinstance(el, dict) or not eh_utilizador(el):
            raise ValueError('filtrar_senhas: argumento invalido')
        
        password = el['pass']
        regras = el['rule']
        
        if not eh_senha_valida(password, regras):
            res += el['name'],
            
    res.sort()
    return res