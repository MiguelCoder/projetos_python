import string
from random import choice

valores= string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.digits + string.punctuation + 'ç'
tamanho = 24
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print("A senha gerada é: "+senha)