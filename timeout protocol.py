import random

def send_timeout():
    # タイムアウト時間を0から1の間でランダムに生成する
    timeout = random.uniform(0, 1)
    # タイムアウト時間を10進数の文字列に変換
    timeout_str = f"{timeout:.6f}"  # 6桁の精度で文字列に変換
    # ここでtimeout_strを送信する処理を模擬する
    return timeout_str

def receive_timeout(timeout_str):
    # 受信したtimeout_strを10進数の値に戻す
    timeout_received = float(timeout_str)
    return timeout_received

# 例として関数を呼び出してみる
sent_timeout_str = send_timeout()
received_timeout = receive_timeout(sent_timeout_str)

# 結果の表示
print(f"Sent timeout: {sent_timeout_str}")
print(f"Received timeout: {received_timeout}")