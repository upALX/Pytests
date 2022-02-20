# class Account:
#     def __init__(self, user_value, user_name,user_balance, user_limit):
#         self.account = user_value
#         self.titular = user_name
#         self.balance = user_balance
#         self.limit = user_limit

class Sistema():
    def __init__(self, text_user):
        self.text = text_user


    def le_entrada(self):
        self.texto = input('Digite a entrada: ')


    def exibe_saida(self):
        print('O texto digitado é: {}'.format(self.texto))