from collections import Counter


with open("list_actriz.txt", "r") as txt:
    t = txt.read()


all_actriz = t.split('\n')[:-1]

print(Counter(all_actriz))