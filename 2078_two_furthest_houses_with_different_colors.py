def maxDistance(colors):
    pmax = 0
    n = len(colors)
    # logic is to check distance from either end
    # forward pass to find max distance
    for idx,color in enumerate(colors):
        if color != colors[0]:
            pmax = max(pmax,idx)
    # reverse pass to find max distance
    for idx,color in enumerate(reversed(colors)):
        if color != colors[0]:
            pmax = max(pmax,idx)

    return pmax

# time complexity is O(n) as we go over the list twice            