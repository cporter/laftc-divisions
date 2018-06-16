import random

random.seed('Rover Ruckus 2018')

host = ['C2', 'F1', 'F2', 'I']
nonhost = ['A1', 'A2', 'B', 'C1', 'D', 'PE', 'O']

random.shuffle(host)
random.shuffle(nonhost)

extra = random.randint(0,  len(host))

ilt = [(nonhost.pop(), nonhost.pop())]
ilt.extend(zip(host, nonhost))

for i, x in enumerate(ilt):
    h, n = x
    if i == extra:
        print '%s\t%s\t%s' % (h, n, nonhost[-1])
    else:
        print '%s\t%s' % (h, n)
