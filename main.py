from account import Account
from csvManager import CSVManager


def main():
    acc = Account('test', 'ozef', 'No website')
    print(acc)
    csv_manager = CSVManager()
    print(csv_manager)
    csv_manager.add_account(acc)
    accounts = csv_manager.get_all_accounts()
    [print(acc) for acc in accounts]


if __name__ == '__main__':
    main()
