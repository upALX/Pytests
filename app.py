def create_account(number_id, name_user, balance_value):
    account = {"id_user": number_id, "user_name": name_user, "balance": balance_value}
    return account


account = create_account(1, "Alexandre", "10.000")

print('Sua conta é a numero {}, você é o corretista {} e seu saldo em conta é {}'.format(account["id_user"],
                                                                                         account["user_name"],
                                                                                         account["balance"]))


def deposit_value_in_account(account, value_push):
    account["balance"] += value_push


def pull_money_to_the_account(account, pull_money):
    account["balance"] -= pull_money


def show_balance(account):
    print(account["balance"])
