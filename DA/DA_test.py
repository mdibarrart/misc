# -*- coding: utf-8 -*-

import sys
if "C:\\Users\\Pipo Dirrabart\\scripts\\python" not in sys.path :
    sys.path.append("C:\\Users\\Pipo Dirrabart\\scripts\\python\\DA")

import random
import matplotlib.pyplot as plot

import DA

a = [[2,1,3,0],[1,2,3,0],[1,2,3,0]]

b = [[1,2,3,0],[3,1,2,0],[1,2,3,0]]

c = DA.DA(a,b)

steps = []
n = 20
for t in range(1000) :
    m_pref = []
    w_pref = []
    for i in range(n) :
        m_pref.append(random.sample(range(0, n+1), n+1))
        w_pref.append(random.sample(range(0, n+1), n+1))
    steps.append(DA.DA(m_pref,w_pref)["steps"])
    
plot.hist(steps,bins=[sum(x) for x in zip([0.5]*(n+3), list(range(-1,n+1)))])