def solution(food_times, k): 
    cur = []
    for idx in range(len(food_times)):
        if food_times[idx]: cur.append(idx)   
    if not cur: return -1
    else:
        if k >= len(cur):
            delta = min((min([food_times[c] for c in cur]), k//len(cur)))
            for c in cur:
                food_times[c] -= delta
            return solution(food_times, k - delta * len(cur))
        else:
            return cur[k]+1