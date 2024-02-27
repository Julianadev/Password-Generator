import secrets
import string
import PySimpleGUI as sg


def generate_password(length):
    caracteres = string.ascii_letters + string.punctuation + string.digits
    senha = ''.join(secrets.choice(caracteres) for i in range(length))
    return senha

layout = [
    [sg.Text('Digite o tamanho da senha que você deseja:')],
    [sg.Input(key='-LENGTH-', size=(20,1))],
    [sg.Button('Gerar Senha'), sg.Button('Sair')],
    [sg.Text(size=(40, 1), key='-OUTPUT-')]
]

window = sg.Window('Gerador de Senha', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Gerar Senha':
        try:
            length = int(values['-LENGTH-'])
            password = generate_password(length)
            window['-OUTPUT-'].update(password)
        except ValueError:
            window['-OUTPUT-'].update('Por favor, insira um número inteiro válido.')

window.close()
