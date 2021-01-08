import random
import sys


def decision(probability):
    return random.random() < probability

#gia tin ektelesi perni ta pio kato orismata me tin seira: phi graph corrupted_users users broken_paths fix_strategy
def main():
    phi = float(sys.argv[1])
    graphf = sys.argv[2]
    corrupted = sys.argv[3]
    users = sys.argv[4]
    broken = int(sys.argv[5])
    fix = sys.argv[6]
    graph = {}
    i = 0
    corrupted_users = []
    with open(corrupted) as infile:
        for line in infile:
            corrupted_users.append(int(line[:-1]))
    senders = []
    with open(users) as infile:
        for line in infile:
            senders.append(int(line[:-1]))
    with open(graphf) as infile:
        for line in infile:
            line = line[:-1]
            line_words = line.split(' ')
            neighbors = []
            j = 0
            for neighbor in line_words:
                if neighbor == "1":
                    neighbors.append(j)
                j += 1
            graph[i] = neighbors
            i += 1
    st_brok = broken
    for sender in senders:
        to_print = ""
        broken = st_brok
        choices = []
        choices.extend(graph.get(sender))
        choices.append(sender)
        chosen = random.choice(choices)
        flag = False
        while chosen in corrupted_users:
            to_print += str(sender) + ","
            broken -= 1
            if broken < 0:
                flag = True
                break
            else:
                chosen = random.choice(choices)
        if flag:
            print str(sender) + ',' + to_print[:-1]
            continue
        flag = False
        while True:
            if decision(phi):  # forward
                tchoices = []
                tchoices.extend(graph.get(chosen))
                tchoices.append(chosen)
                tnext = random.choice(tchoices)
                while tnext in corrupted_users:
                    to_print += str(chosen) + ","
                    broken -= 1
                    if broken < 0:
                        flag = True
                        break
                    else:
                        if fix == 'last_honest':
                            tnext = random.choice(tchoices)
                        else:
                            tnext = random.choice(choices)
                if flag:
                    break
                chosen = tnext
            else:  # deliver
                to_print += str(chosen) + ","
                while broken > 0:
                    to_print += "-1,"
                    broken -= 1
                break
        print str(sender)+','+to_print[:-1]

if __name__ == "__main__":
    main()
