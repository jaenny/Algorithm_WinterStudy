import heapq


def solution(genres, plays):
    music = dict()  # key = genre / value = [totalPlay, each genre's play]

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre not in music:
            music[genre] = [play, [[-play, i]]]
        else:
            music[genre][0] += play
            music[genre][1].append([-play, i])

    musicByTotalPlay = []
    for m in music:
        new = music[m][1]
        music[m][1] = sorted(new)
        heapq.heappush(musicByTotalPlay, [-music[m][0], m])

    answer = []
    while musicByTotalPlay:
        new = heapq.heappop(musicByTotalPlay)
        genre = new[1]
        play = music[genre][1]
        if len(play) == 1:
            answer.append(play[0][1])
        else:
            answer.append(play[0][1])
            answer.append(play[1][1])

    return answer
