def solution(cacheSize, cities):
    answer = 0
    t = 0
    cache = []
    for city in cities:
        # cache hit
        for q in cache:
            if city.lower() == q[1]:
                t += 1
                q[0] = t
                break
        # cache miss
        else:
            t += 5
            cache.append([t, city.lower()])
            if len(cache) > cacheSize:
                lt = (len(cities)+1)*5
                # pick least recently used key
                for i in range(len(cache)):
                    if cache[i][0] <= lt:
                        idx = i
                        lt = cache[i][0]
                del cache[idx]
    answer = t
    return answer