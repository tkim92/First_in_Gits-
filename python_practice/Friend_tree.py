def print_all_friend(g,start):
    qu = []
    done = set()
    qu.append((start,0))
    done.add(start)

    while qu:
        (p,d) = qu.pop(0)
        print(p,d)

        for x in g[p]:
            if x not in done:
                qu.append((x,d+1))
                done.add(x)
