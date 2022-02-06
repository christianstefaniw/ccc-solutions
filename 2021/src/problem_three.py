num_people = int(input())
people = [list(map(int, input().split())) for _ in range(num_people)]

# people = [[6,8,3], [1,4,1], [14, 5, 2]]

def main():
    max_speaker_pos = 10 ** 9
    min_speaker_pos = 0
    speaker_pos = 0

    while True:
        speaker_pos = (max_speaker_pos + min_speaker_pos) // 2

        curr_time = calc_time_for_all_people_to_hear_music(speaker_pos)

        if (curr_time > calc_time_for_all_people_to_hear_music(speaker_pos + 1)): 
            min_speaker_pos = speaker_pos
        elif (curr_time > calc_time_for_all_people_to_hear_music(speaker_pos - 1)):
            max_speaker_pos = speaker_pos
        else:
            break

    print(calc_time_for_all_people_to_hear_music(speaker_pos))


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