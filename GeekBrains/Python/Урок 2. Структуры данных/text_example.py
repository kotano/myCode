f = open('text.txt', 'w')
f.write('Hello, cats\nhow are\nYOU?')

f = open('text.txt', 'r')
print(f.readline())
for s in f:
    print(s)
