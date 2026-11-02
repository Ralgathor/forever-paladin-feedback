#!/bin/sh
# builds/: the rest of the searches after runall.sh hit its time limit. 1-point moves only (SEARCH_2PT=0).
# ret-raid starts again from the two best builds of its 2-point rounds.
cd "$(dirname "$0")"
export SEARCH_2PT=0
python3 search.py ret-raid 050150001-503-15233011101301351 050251001-501-15231301101301351
python3 search.py ret-raid-prop 050150001-503-15233011101301351 050250002-501-05233011201301351
python3 search.py ret-fresh 050150001-503-15233011101301351 050250002-501-05233011201301351
python3 search.py ret-fresh-prop 050150001-503-15233011101301351
python3 search.py prot 050050002-05302102213301531-502
python3 search.py prot-prop -3530110213501531-45233
