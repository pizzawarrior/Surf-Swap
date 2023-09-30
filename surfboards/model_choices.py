
# Board types:
Shortboard = 'Shortboard'
Mid_length = 'Mid-length'
Longboard = 'Longboard'

# Board style:
Fish = 'Fish'
Twin = 'Twin'
Round = 'Round'
Asym = 'Asym'
Swallow_tail = 'Swallow-tail'
Pin_tail = 'Pin tail'
Squash = 'Squash'
Mini_simmons = 'Mini-simmons'
Other = 'Other'

# Fin Style:
Single = 'Single fin'
# twin = 'twin'
Two_plus_one = '2+1'
Thruster = 'Thruster'
Quad = 'Quad'
Five = 'Five-fin'
Finless = 'Finless'
# other = 'other

# Fin System:
Fcs1 = 'Fcs1'
Fcs2 = 'Fcs2'
Futures = 'Futures'
# Other = 'other'

# Format variables as tuples to be accessed in the model attributes
BOARD_TYPES = [

    (Shortboard, 'Shortboard'),
    (Mid_length, 'Mid-length'),
    (Longboard, 'Longboard'),
    (Other, 'Other')
]

TAIL_STYLE = [
    (Fish, 'Fish'),
    (Round, 'Round'),
    (Asym, 'Asym'),
    (Swallow_tail, 'Swallow-tail'),
    (Pin_tail, 'Pin tail'),
    (Squash, 'Squash'),
    (Other, 'Other')
]

FIN_STYLE = [
    (Single, 'Single'),
    (Twin, 'Twin'),
    (Two_plus_one, '2+1'),
    (Thruster, 'Thruster'),
    (Quad, 'Quad'),
    (Five, 'Five-fin'),
    (Finless, 'Finless'),
    (Other, 'Other')
]

FIN_SYSTEM = [
    (Fcs1, 'FCS 1'),
    (Fcs2, 'FCS 2'),
    (Futures, 'Futures'),
    (Other, 'Other')
]
