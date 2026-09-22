import sys
import math
def usage():
    print('''Usage: glicko2tr.py <glicko> <rd> <wins>
Glicko and RD must be an int or float and is mandatory. RD must be between 0 and 350.
Wins must be a int. If not specified, 18 wins will be assumed.
It is not neccesary to specify your win count if you have 18 or more wins.''')
    sys.exit(1)

def trCalc(mmr, deviation, victories):
    f = min(1, (0.5 + 0.5 * (victories / 18)))
    d = 1 + (60 - rd) / 1500
    b = 1.56
    c = 0.86
    v = 0.87646605
    w = 0.25

    return (22000 / ((1 + (math.e ** (-d * b * ((mmr - 1500) / 500)))) ** (1/(v*f)))) + (3000 / ((1 + (math.e ** (-d * c * ((mmr - 2000) / 500)))) ** (1/(w*(f ** 2)))))
    
if len(sys.argv) < 3:
    usage()

elif len(sys.argv) == 3:
    print("Win count was not given, assuming at least 18 wins")

try:
    glicko = float(sys.argv[1])
    rd = float(sys.argv[2])
    wins = int(sys.argv[3])

except ValueError:
    usage()

except IndexError:
    wins = 18 # only way IndexError can be raised iirc is if no wins count is given

tr = trCalc(glicko, rd, wins)
print(round(tr), "TR")




