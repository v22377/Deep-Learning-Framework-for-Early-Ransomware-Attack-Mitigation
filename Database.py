import datetime

def save_log(data, status):
    with open("logs.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} | {data} | {status}\n")
