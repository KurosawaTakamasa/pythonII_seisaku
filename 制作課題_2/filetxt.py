from file import File

#テキストファイルを管理するクラス
class FileTxt(File):
    #書き込みメソッド
    def set_txt(self, val):
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(val)

    #読み込みメソッド
    def get_txt(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            text = file.read()
            return int(text)
