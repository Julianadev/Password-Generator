import secrets
import string


print('============================ Gerador de Senhas ================================')

escolha_usuario = int(input('Digite qual o tamanho que você quer que sua senha seja: '))

caracteres = string.ascii_letters + string.punctuation + string.digits
senha = ''.join(secrets.choice(caracteres) for i in range(escolha_usuario))

print(senha)
