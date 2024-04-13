def find(cities, Path, start,end):
    unexplored = {cities : float('inf') for cities in cities}
    unexplored[start] = 0
    while len(unexplored)!=0:
        explore = min(unexplored, key=unexplored.get)
        # print(min(unexplored, key=unexplored.get))
        # print("ini explore " + explore)
        if explore == end:
            break
        else:
            for path in Path.items():
                if path[0][0] == explore:
                    if path[0][1] in unexplored.keys():
                        check_time = unexplored[path[0][0]] + path[1]
                        if check_time < unexplored[path[0][1]]:
                            unexplored[path[0][1]] = check_time
                elif path[0][1] == explore:
                    if path[0][0] in unexplored.keys():
                        check_time = unexplored[path[0][1]] + path[1]
                        if check_time < unexplored[path[0][0]]:
                            unexplored[path[0][0]] = check_time
                # print(path[0][0] + "    " + path[0][1])
        print(explore)        
        del unexplored[explore]
        # print(unexplored)
    return(unexplored[explore])
    # return(unexplored[explore])

        #break
        #print(explore)
        #if(explore==)
    # print(unexplored)

