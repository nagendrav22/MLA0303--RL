import numpy as np

portfolios={
'Conservative':np.array([0.2,0.6,0.2]),
'Balanced':np.array([0.5,0.3,0.2]),
'Aggressive':np.array([0.8,0.1,0.1])
}
expected=np.array([0.10,0.05,0.02]) # example asset returns

for name,w in portfolios.items():
    value=float(w@expected)
    print(name,"predicted return:",round(value*100,2),"%")

best=max(portfolios,key=lambda n:portfolios[n]@expected)
print("Best predicted portfolio:",best)

