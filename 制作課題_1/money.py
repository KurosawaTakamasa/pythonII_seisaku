#残高、入出金を管理するクラス
class Money:
    def __init__(self, balance):
        #残高
        self.balance = balance
         #履歴
        self.history = [] 

    #出金メソッド
    def set_withdrawal(self, subject, money):
        #残高がマイナスになる場合
        if self.balance < money: 
            return False
        #残高がプラス or ゼロとなる場合
        else:
            self.balance =  self.balance - money
            self.history.append(['出金', subject, money])
            return True
    
    #入金メソッド
    def set_payment(self, subject, money):
        self.balance = self.balance + money
        self.history.append(['入金', subject, money])

    
    #履歴を返すメソッド
    def get_history(self):
        #参照渡しとならないようにコピーする
        history_copy = self.history.copy()
        return history_copy
    
    #残高を返すメソッド
    def get_balance(self):
        return self.balance