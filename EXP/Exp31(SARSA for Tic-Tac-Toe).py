import random

Q={}
actions=list(range(9))
alpha,gamma,eps=0.2,0.9,0.1

def key(board): return ''.join(board)

for _ in range(5000):
    board=[' ']*9
    while ' ' in board:
        s=key(board)
        avail=[i for i in actions if board[i]==' ']
        a=random.choice(avail) if random.random()<eps else max(avail,key=lambda x:Q.get((s,x),0))
        board[a]='X'
        ns=key(board)
        reward=1 if ' ' not in board else 0
        na=random.choice([i for i in actions if board[i]==' '],default=None)
        old=Q.get((s,a),0)
        target=reward if na is None else reward+gamma*Q.get((ns,na),0)
        Q[(s,a)]=old+alpha*(target-old)
        if na is None: break
        board[na]='O'

print("SARSA training completed. Learned state-action pairs:",len(Q))

