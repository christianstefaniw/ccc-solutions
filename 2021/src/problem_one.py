from reprlib import aRepr


def main():
    N = int(input())
    h_raw = input()
    w_raw = input()
    area = 0

    heights = h_raw.split()
    widths = w_raw.split()

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