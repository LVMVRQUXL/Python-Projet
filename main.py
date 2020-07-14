from account import Account
from accountManager import AccountManager


def main():
    acc = Account('test', 'ozef', 'No website')
    account_manager = AccountManager()
    account_manager.add_account(acc)
    accounts = account_manager.get_all_accounts()
    if len(accounts) == 0:
        print('No accounts to print!\n')
    else:
        [print(acc) for acc in accounts]
        print('\n')

    new_acc = Account('test', 'password_updated', 'No description')
    account_manager.update_account(acc, new_acc)
    accounts = account_manager.get_all_accounts()
    if len(accounts) == 0:
        print('No accounts to print!\n')
    else:
        [print(acc) for acc in accounts]
        print('\n')

    account_manager.remove_account(acc)
    accounts = account_manager.get_all_accounts()
    if len(accounts) == 0:
        print('No accounts to print!\n')
    else:
        [print(acc) for acc in accounts]
        print('\n')


if __name__ == '__main__':
    main()
