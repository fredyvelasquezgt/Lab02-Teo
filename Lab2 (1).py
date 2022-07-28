import numpy as np
import pandas as pd


def main():
    print(":: LABORATORIO 2 ::\n")
    data = pd.DataFrame(np.array([
    ["q0", ["+","-"], "q0,q1"], ["q0", [str(i) for i in range(0, 9)], "q1,q4"], 
    ["q0,q1", [str(i) for i in range(0, 9)], "q1,q4"], 
    ["q0,q1", ["+","-"], "q0,q1"], ["q1,q4", [str(i) for i in range(0, 9)], "q1,q4"], 
    ["q1,q4", ["."], "q2,q3,q5"], ["q2,q3,q5",[str(i) for i in range(0, 9)] ,"q3,q5" ],
    ["q3,q5", [str(i) for i in range(0, 9)], "q3,q5"]],),
    columns=['state', 'symbol', 'δ(q, s)'])

    print("[!] Estado de aceptacion: " + str(accepted(getFinalState("q0","2022.3.3.3",data), ["q2,q3,q5","q3,q5"])) )
    print("[Nuevo] δ(s, sy)")
    for i in estados:
        print(i)



def transition(q, w, s):
    try:
        n1 = s['state'] == q 
        n2 = s['symbol'].map(lambda x:w in  x)
        el = s[ n1 & n2 ]
        return el['δ(q, s)'].values[0]
    except:
        print("[ERR] ")


estados = []
items = {}
def getFinalState(q, w,s ):
    try:
        if len(w) != 0:
            items['state'], items['symbol'] = q, w[0]
            estados.append("[!] δ(" + str(q) + "," + str(w[0]) + ") -> " + str( transition(q, w[0], s) ))
            res_transition = transition(q, w[0], s)
            return getFinalState( res_transition, w[1:], s)

        return q
    except:
        print("[ERR] ")

def accepted(q, s):
    try:
        res = q in s
        return bool(res)
    except:
        print("[ERR] ")


if _name_ == '_main_':
    main()
