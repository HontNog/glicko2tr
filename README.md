# glicko2tr
Python 3 script that converts Glicko-2 elo and RD to TETR.IO's TR.

## What it does
This is a Python 3 script that converts Glicko-2's elo and RD (and optionally your win count) into TETR.IO's TR used in Tetra League.

Similar to TETR.IO, this script will round your TR to the nearest whole number.

This script is useful for players trying to determine their true TR after experiencing an increase in RD.
## Usage
Run from the command line.
```
python glicko2tr.py <glicko> <rd> <wins>
```
If you are running macOS or Linux, you may have to run this instead:
```
python3 ./glicko2tr.py <glicko> <rd> <wins>
```
`<glicko>` refers to a players Glicko-2 elo.
`<rd>` refers to a players Glicko-2 RD.
`<wins>` refers to a players wincount. **Note:** This is optional, and in fact not necessary for most people as a player's win count does not affect your TR if you have at least 18 wins in Tetra League.
## Known issues
Inputting low values for glicko-2 does appear to give incorrect results. I don't know why this is the case, nor do I really care to fix it.
## Thanks
Thanks to osk for the TR formula ([shamelessly stolen here](https://discord.com/channels/673303546107658242/1260605501754839060/1356615088509026466)).

