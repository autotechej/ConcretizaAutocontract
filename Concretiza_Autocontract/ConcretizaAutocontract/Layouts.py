#Esta é a biblioteca usada para fazer a interface


import pysimplegui as sg
#Aqui são definidos os parâmetros do tema da interface, nesse caso foram utilizadas as cores da EJ

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#87ceeb', 
                                        'TEXT': '#3C3C3B', 
                                        'INPUT': '#87ceeb', 
                                        'TEXT_INPUT': '#3C3C3B', 
                                        'SCROLL': '#EB7F00', 
                                        'BUTTON': ('#3C3C3B', '#87ceeb'), 
                                        'PROGRESS': ('# D1826B', '# CC8019'), 
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, }
font = ("Times New Roman", 12)
FontTitle = ("Times New Roman", 40)
FontSubtitle = ("Times New Roman", 20)
font2 = ("Times New Roman", 6)
font3 = ("Times New Roman", 24)

#Essa função aplica o tema à janela

sg.theme('MyCreatedTheme') 

#Aqui se definem os layouts das janelas de interface

#Layout do menu principal
MenuPrincipalLayout = [
    [sg.Image('ConcretizaAutocontract/Logo.png', size=(200,140), key= 1)],
    [sg.Text('Menu Principal', font = FontSubtitle)],
    [sg.Button('Preencher Novo Contrato', font=font)],
    [sg.Button('Preferências',  font=font)],
    [sg.Button('Sair', font=font)]
]

#Layout do Menu de Contratos
MenuContratosLayout = [
    [sg.Text('Menu de Seleção', font = font3)],
    [sg.Text('')],
    [sg.Button('Contrato de Prestação de Serviços')],
    [sg.Button('Sair')]
]

#Layout do Formulário
FormularioLayout1 = [
    [sg.Text('Informações do Cliente', font=font3)],
    [sg.Text('Indique o Nome da Empresa Cliente:'), sg.InputText(), sg.Text('Indique o CNPJ do Cliente:'), sg.InputText(),],
    [sg.Text('Indique o Endereço do Cliente:'), sg.InputText(), sg.Text('Indique o EMAIL do Cliente:'), sg.InputText()],
    [sg.Text('Indique o CEP do Cliente:'), sg.InputText(), sg.Text('Indique a Cidade e o Estado do Cliente:'), sg.InputText()],
    [sg.Text('Indique o Nome do Representante do Cliente:'), sg.InputText(), sg.Text('Indique o CPF do Presidente Cliente:'), sg.InputText()],
    [sg.Text('Indique o RG do Presidente Cliente:'), sg.InputText(), sg.Text('Indique o órgão expedidor: '), sg.InputText()],
    [sg.Text('Indique o Cargo do Representante: '), sg.InputText(), sg.Text('Indique o Estado Civil do Cliente: '), sg.InputText()],
    [sg.Text('Indique o CPF do Cliente: '), sg.InputText(), sg.Text('Indique o telefone de contato do Cliente: '), sg.InputText()], 
    [sg.Button('Continuar'), sg.Button('Sair')]
    ]

FormularioLayout2 =[
    [sg.Text('Dados Financeiros', font = font3)],
    [sg.Text('Indique o Valor Final do Serviço: '), sg.InputText()],
    [sg.Text('Faça uma breve descrição de como será a forma de pagamento:'), sg.InputText('Digite aqui da forma que digitaria no contrato...')],
    [sg.Text('Indique o Titular da Conta que o pagamento será efetuado:'), sg.InputText()],
    [sg.Text('Indique o CNPJ da Conta do Pagamento: '), sg.InputText()],
    [sg.Text('Inidique o Banco em que será efetuado o pagamento:'), sg.InputText()],
    [sg.Text('Indique a Agência do Banco(Com dígito):'), sg.InputText()], 
    [sg.Text("Indique a Conta(Com dígito): "), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
]

FormularioLayout3 =[
    [sg.Text('Dos Serviços e Prazos', font=font3)],
    [sg.Text('Prazo para Execução do Projeto: '), sg.InputText("Escreva por extenso")],
    [sg.Text('Prazo para Contato após finalizar: '), sg.InputText("Escreva por extenso")],
    [sg.Text('Descrição do Serviço: '), sg.InputText('Descreva como deve estar no contrato')],
    [sg.Text('Descrição passo-a-passo do Serviço: '), sg.InputText]
    [sg.Text('Vigência do Contrato: '), sg.InputText()],
    [sg.Button('Finalizar'), sg.Button('Sair')]
]


FormularioLayout4 = [
    [sg.Text('Dados Finais', font=font3)],
    [sg.Text('Faça uma descrição do sistema: '), sg.InputText()],
    [sg.Text('Indique o Número de Controle: '), sg.InputText()], 
    [sg.Text('Data no formato xx/xx/xxxx:'), sg.InputText('xx/xx/xxxx')],
    [sg.Text('Indique o Nome do Representante da Empresa Cliente:'), sg.InputText()], 
    [sg.Text('Indique o CPF do Representante:'), sg.InputText()],
    [sg.Text('Indique o Nome da Testemunha 1'), sg.InputText()], 
    [sg.Text('Indique o CPF da Testemunha 1:'), sg.InputText()],
    [sg.Text('Indique o Nome da Testemunha 2'), sg.InputText()], 
    [sg.Text('Indique o CPF da Testemunha 2:'), sg.InputText()],
    [sg.Text('Faça uma descrição do sistema: '), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
]

FormularioLayout5 = [
    [sg.Text('Dos Prazos', font=font3)],
    [sg.Text('Prazo para Elaboração inicial e planejamento do projeto: '), sg.InputText()],
    [sg.Text('Prazo para a compra e obtenção dos materiais necessários para o projeto: '), sg.InputText()],
    [sg.Text('Prazo para desenvolvimento prático do projeto: '), sg.InputText()],
    [sg.Text('Prazo para compra e obtenção dos materiais necessários para o projeto: '), sg.InputText()],
    [sg.Text('Prazo para instalação do projeto no local solicitado pelo contratante: '), sg.InputText()],
    [sg.Button('Finalizar'), sg.Button('Sair')]
    ]