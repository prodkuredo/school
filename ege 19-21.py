def moves(h): 
    a,b = h 
    return (a+1,b), (a*2,b), (a,b+1), (a,b*3) #MOVES
@lru_cache(None)
def game(h):
    a,b = h 
    if a+b >= 69: return 'W' #WIN COND
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'V1'
    if any(game(m) == 'V1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'V2'
for s in range(1,59):
    h = 10,s #FIRST AND SECOND HEAPS
    print(s,game(h))