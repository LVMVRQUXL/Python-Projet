from account import Account


def main():
    acc = Account('test', 'ozef')
    print(acc)
    acc.username = ''


if __name__ == '__main__':
    main()
