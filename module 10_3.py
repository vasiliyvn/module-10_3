import threading
from time import sleep
import  random



class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(100):
            input = random.randint(50, 100)
            self.balance += input
            if self.balance >=500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {input}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            insert = random.randint(50, 100)
            print(f'Запрос на {insert}\n')
            if insert <= self.balance:
                self.balance -= insert
                print(f'Снятие: {insert}. Баланс: {self.balance}')
            if insert > self.balance:
                self.lock.acquire()
                print(f'запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')