import pulp, numpy as np
def optimize_one_hour(gen_hat,dem_hat,price_hat):
    n=len(gen_hat); m=pulp.LpProblem('opt',pulp.LpMaximize)
    p=pulp.LpVariable.dicts('p',range(n),0); u=pulp.LpVariable.dicts('u',range(n),0)
    m+=price_hat*pulp.lpSum([p[i] for i in range(n)])-1000*pulp.lpSum([u[i] for i in range(n)])
    for i in range(n): m+=p[i]<=gen_hat[i]; m+=p[i]+u[i]>=dem_hat[i]
    m.solve(); return [p[i].value() for i in range(n)],[u[i].value() for i in range(n)]