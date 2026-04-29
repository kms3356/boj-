def solution(wallpaper):
    x = []
    y = []
    for i, wall in enumerate(wallpaper):
        for a,char in enumerate(wall):
            if char == '#':
                x.append(i)
                y.append(a)

    res = [min(x), min(y), max(x)+1, max(y)+1]
    return res