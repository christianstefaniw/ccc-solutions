N = int(input())
obs = [list(map(int, input().split())) for _ in range(N)]

def main():
    obs.sort()

    top_speed = 0

    for i in range(N):
        if i == 0: 
            continue
        
        delta_t = obs[i][0] - obs[i-1][0]
        delta_d = abs(obs[i][1] - obs[i-1][1])
        speed = calc_speed(delta_d, delta_t)

        if speed > top_speed:
            top_speed = speed

    print(top_speed)       

def calc_speed(delta_d, delta_t):
    return delta_d/delta_t

main()