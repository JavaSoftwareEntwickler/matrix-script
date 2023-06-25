import time
import random
import os
import msvcrt

class message(str):
    def __new__(cls, text, speed):
        self = super(message, cls).__new__(cls, text)
        self.speed = speed
        self.y = -1 * len(text)
        self.x = random.randint(0, display().width)
        self.skip = 0
        return self

    def move(self):
        if self.speed > self.skip:
            self.skip += 1
        else:
            self.skip = 0
            self.y += 1

class display(list):
    def __init__(self):
        _, self.width = os.get_terminal_size()
        self.height = os.get_terminal_size().lines
        self[:] = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def set_vertical(self, x, y, string):
        string = string[::-1]
        if x < 0:
            x = self.width + x
        if x >= self.width:
            x = self.width - 1
        if y < 0:
            string = string[abs(y):]
            y = 0
        if y + len(string) > self.height:
            string = string[0:self.height - y]
        if y >= self.height:
            return
        for i, char in enumerate(string):
            self[y + i][x] = char

    def __str__(self):
        return '\n'.join(''.join(row) for row in self)

def matrix(iterations, sleep_time=.08):
    messages = []
    d = display()
    for _ in range(iterations):
        messages.append(message('10' * 16, random.randint(1, 5)))
        for text in messages:
            d.set_vertical(text.x, text.y, text)
            text.move()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[1m\033[32m%s\033[0m' % d, end='\r')
        time.sleep(sleep_time)

if __name__ == '__main__':
    while True:
        try:
            matrix(150)
        except KeyboardInterrupt:
            print('\n\033[1m\033[32m=== Matrix Stopped ====\033[0m\n')
            break
