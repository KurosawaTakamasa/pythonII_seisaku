from money import Money

#残高の初期値
balance = int(input('残高の初期値: '))

#Moneyクラスをインスタンス化
money = Money(balance)

while True:
    #以下に実行処理を記述する（記述するのは以下の4つ）
    select = input('1:残高と履歴の確認/2:入金の登録/3:出金の登録/9:終了 => ')
    if select == '1':
        #「残高と履歴の確認」
        print(f'現在の残高: {money.get_balance()}')
        print('履歴')
        print(f'{'入金/出金':^5}{'科目':^16}{'金額':^16}')
        print('-'*40)
        for h in money.get_history():
            print(f'{h[0]:^5}{h[1]:^16}{h[2]:^16}')
            print('-'*40)

    elif select == '2':
        #「入金の登録」
        subject = input('科目: ')
        money2 = int(input('金額: '))
        money.set_payment(subject, money2)
        print('入金処理が終了しました')
        
    elif select == '3':
        #「出金の登録」
        subject = input('科目: ')
        money2 = int(input('金額: '))
        if money.set_withdrawal(subject, money2):
            print('出金処理が終了しました')
        else:
            print('残高が足りません')

    elif select == '9':
        #「プログラムの終了」
        break
