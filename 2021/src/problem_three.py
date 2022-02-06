num_people = int(input())
people = [list(map(int, input().split())) for _ in range(num_people)]


def main():
    max_speaker_pos = 10 ** 9
    min_speaker_pos = 0

    while max_speaker_pos > min_speaker_pos + 1:
        mid = (max_speaker_pos + min_speaker_pos) // 2

        time_one = calc_time_for_all_people_to_hear_music(mid)
        time_two = calc_time_for_all_people_to_hear_music(mid + 1)

        if (time_one > time_two): 
            min_speaker_pos = mid
        else:
            max_speaker_pos = mid

    print(min(calc_time_for_all_people_to_hear_music(min_speaker_pos), calc_time_for_all_people_to_hear_music(max_speaker_pos)))


def calc_time_for_all_people_to_hear_music(speaker_pos):
    time = 0

    for pos, speed, hear_distance in people:
        if (pos == speaker_pos): continue

        if (speaker_pos < pos and (pos - (speaker_pos + hear_distance)) > 0):
            time += (pos - (speaker_pos + hear_distance)) * speed
        elif (pos < speaker_pos and (speaker_pos - (pos + hear_distance)) > 0):
            time += (speaker_pos - (pos + hear_distance)) * speed

    return time

main()

# score: 15/15