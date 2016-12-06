

with open('new1.txt','r') as f:
    for line in f:
        if (len(line.split('—')[0].split()) < 10):
            print(line.split('—')[0])
