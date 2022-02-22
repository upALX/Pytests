class Account:
    def __init__(self, user_value, user_name,user_balance, user_limit):
        self.__account = user_value
        self.__titular = user_name
        self.__balance = user_balance
        self.__limit = user_limit

    def deposita(self, value_dep):
        self.__balance += value_dep
        print('Seu saldo ficou em {}'.format(self.__balance))


    def saque(self, value_saq):
        self.__balance -= value_saq
        print('Seu saldo ficou em {}'.format(self.__balance))


    def transaction(self, value_transfer, account_destiny):
        self.saque(value_transfer)
        account_destiny.deposita(value_transfer)


    @property
    def account(self):
        return self.__account


    def get_balance(self):
        return self.__balance


    def get_titular(self):
        return self.__titular


    def get_limit(self):
        return self.__limit

    def set_limit(self, value_new_limit):
        self.__limit = value_new_limit



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