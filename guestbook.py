# coding: utf-8
import shelve

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """登校データを保存する"""
    # shelveモジュールでデータベースファイルを開く
    database = shelve.open(DATA_FILE)
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # データベースからデータを取得する
        greeting_list = database['greeting_list']

    #リストの先頭に投稿データを追加する
    greeting_list.insert(0,{
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })
    #データベースを更新する
    database['greeting_list'] = greeting_list
    #データベースファイルを閉じる
    database.close();

def load_data():
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list