#the following algorithm is an existing algorithm from a published literature
#which provided the code
#https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf

def make_pi(limit):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    cnt=0
    while cnt<limit:
        if 4 * q + r - t < n * t:
            if(n%3==0):
                yield n
                cnt+=1
            q, r, t, k, n, l = (10 * q, 10 * (r - n * t), t, k,
                                (10 * (3 * q + r)) // t - 10 * n, l)
        else:
            q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1,
                                (q * (7 * k + 2) + r * l) // (t * l), l + 2)

# generator code
if __name__=='__main__':
    print([a for a in make_pi(900)])
