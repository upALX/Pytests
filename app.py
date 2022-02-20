class Account:
    def __init__(self, user_value, user_name,user_balance, user_limit):
        self.__account = user_value
        self.__titular = user_name
        self.__balance = user_balance
        self.__limit = user_limit


    def extrato(self):
        print('Seu saldo é de {:.f3}.'.format(self.__balance))


    def deposita(self, value_dep):
        self.__balance += value_dep
        print('Seu saldo ficou em {:.f3}'.format(self.__balance))


    def saque(self, value_saq):
        self.__balance -= value_saq
        print('Seu saldo ficou em {:.f3}'.format(self.__balance))














# class Sistema():
#     def __init__(self):
#         self.text = ''
#
#
#     def le_entrada(self):
#         self.texto = input('Digite a entrada: ')
#
#
#     def exibe_saida(self):
#         print('O texto digitado é: {}'.format(self.texto))