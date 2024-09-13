from money import Money
from filetxt import FileTxt

#テキストファイルで残高を管理するクラス
#Moneyクラスを継承する
class MoneyTxt(Money):
    def __init__(self, balance_path):
        self.balance = self.balance_init(balance_path)
        self.history = []
    
    def balance_init(self, balance_path):
        #FileTxtクラスをインスタンス化
        self.filetxt = FileTxt(balance_path)

        try: 
            #FileTxtクラスのget_txtメソッドを呼び出す
            balance = self.filetxt.get_txt()
            #残高が書き込まれていなかったら、残高を入力させbalanceに設定
            if balance == '':
                balance = int(input('残高を設定してください: '))
        except FileNotFoundError:
            #ファイルが存在しなかったら、残高を入力させbalanceに設定
            balance = int(input('残高を設定してください: '))
        
        #balanceを返却
        return balance
        

    def save(self):
        #残高をテキストファイルに書き込む処理
        self.filetxt.set_txt(str(self.balance))
