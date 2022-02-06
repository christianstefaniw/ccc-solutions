def main():
    N = int(input())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    area = 0
    
    for i in range(N):
        if (i == len(widths)):
            break
        area += calc_area(int(heights[i]), int(heights[i + 1]), int(widths[i]))

    print(area)

    return area




def calc_area(a, b, h):
    return h * ((a+b)/2)


main()

# score: 15/15