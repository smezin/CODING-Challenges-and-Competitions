def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    dist_map = {}
    n = len(seats)
    distance = 0
    none_left = True
    for i in range(n):
        if seats[i] == 0:
            if none_left:
                distance = 10**5
            else:
                distance += 1
        else:
            distance = 0
            none_left = False

        dist_map[i] = [distance]
    
    distance = 0
    none_right = True
    for i in range(n-1, -1, -1):
        if seats[i] == 0:
            if none_right:
                distance = 10**5
            else:
                distance += 1
        else:
            distance = 0
            none_right = False
        dist_map[i].append(distance)
    print(dist_map)
    max_dist = 0
    best_seat = -1
    for i in range(len(dist_map)):
        dist = min(dist_map[i][0], dist_map[i][1])
        if dist > max_dist:
            max_dist = dist
            best_seat = i
    return max_dist

seats = [0,1]
print(maxDistToClosest(seats))
    