χ = -2
i = 0
for k in range(3,abs(2*χ)+5):
    for n in range(k,abs(100*χ)):
        d = (2*k+2*n-k*n)
        if χ*d > 0 and χ*k*n % d == 0 and 2*χ*k % d == 0 and 2*χ*n % d == 0:
            E = χ*k*n//d
            V = 2*χ*n//d
            R = 2*χ*k//d
            i += 1
            # print("{}) k={}; n={}; V={}; E={}; R={}".format(
                # i,k,n,V,E,R))
            # print("{:2} & {:2} & {:2} & {:2} & {:2}\\\\".format(
                # i,k,n,V,E,R))
            print(R,"& ",end="")
