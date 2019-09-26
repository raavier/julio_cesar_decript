import requests
import json
import hashlib


response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=987a886ac0e3b99d1f382d50b9f2f2db7e07a70a') # (your url)
answer = response.json()
with open('answer.json', 'w') as f:
    json.dump(answer, f)

def alfabeto_int(letra):
    input = letra
    input = input.lower()
    numb_alf = ord(input) - 96
    return numb_alf
def int_alfabeto(letra):
    input = letra
    alf_numb = chr(input+96)
    return alf_numb


num_cas = answer['numero_casas']
#um_cas = 1
#cifrado = 'çá'
cifrado = answer['cifrado']
cifrado.lower()
dec = []
#dic = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
for x in cifrado:
    #print(x)
    #print(x.isdigit())or x == '.' or x == ' '
    if not x.isalpha() :
        #print('valor de x dentro do if1: {}'.format(x))
        dec.append(x)
    else:
        #print('valor de x dentro do if2: {}'.format(x))
        n_int = alfabeto_int(x)
        #print('n_int: {}'.format(n_int))
        n_dec = n_int%27-num_cas
        #print('n_dec: {}'.format(n_dec))
        #print(n_dec)
        #print(dic[n_dec])
        if n_dec<=0:
            n_dec = n_dec+26
        a_dec = int_alfabeto(n_dec)

        #print(a_dec)
        dec.append(a_dec)
        #print(dec)


s = [str(i) for i in dec]
decifrado = (''.join(s))


result = hashlib.sha1(decifrado.encode())
sha1 = result.hexdigest()

answer['decifrado'] = decifrado
answer['resumo_criptografico'] = sha1
with open('answer.json', 'w') as f:
    json.dump(answer, f)

files = { 'answer' : open('answer.json', 'r')  }

response = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=987a886ac0e3b99d1f382d50b9f2f2db7e07a70a',
                             files=files)
print(response.status_code, response.reason)













