# ChatGPTに作ってもらった、タイピングゲームです。

import random
import time

# 単語リスト
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def typing_game():
    print("タイピングゲームへようこそ！")
    print("表示された単語をできるだけ早く入力してください。")
    print("準備ができたらEnterを押してください。")
    input()
    
    score = 0
    total_time = 0

    for i in range(5):  # 5回の単語を出題
        word = random.choice(words)  # ランダムに単語を選択
        print(f"単語: {word}")
        
        start_time = time.time()  # タイピング開始時刻
        typed_word = input("あなたの入力: ")
        end_time = time.time()  # タイピング終了時刻
        
        elapsed_time = end_time - start_time  # 経過時間
        total_time += elapsed_time

        if typed_word == word:
            print("正解！")
            score += 1
        else:
            print(f"不正解。正しい単語は '{word}' です。")

    # 結果表示
    print(f"\nゲーム終了！あなたのスコア: {score}/5")
    print(f"平均タイピング時間: {total_time / 5:.2f}秒")

# ゲームを実行
if __name__ == "__main__":
    typing_game()
