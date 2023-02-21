
prim = 0
seg = 1
i = 3
while i < 15:
    sig = prim + seg
    prim = seg
    seg = sig
    print(sig)
    i = 1 + i
    