# Program demonstrating custom iterator

class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

obj = MyNumbers()

for number in obj:
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5