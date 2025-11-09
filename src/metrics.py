import numpy as np
def reliability(d,s): return 1-s.sum()/d.sum()
def losses(g,p): return (g.sum()-p.sum())/g.sum()
def ebitda_margin(r,c): return (r-c)/r