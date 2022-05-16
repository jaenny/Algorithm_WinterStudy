from collections import deque


def solution(tickets):
    tickets.sort()
    queue = deque()
    queue.append([["ICN"], tickets])

    while queue:
        path, leftTickets = queue.popleft()
        if len(leftTickets) == 0:
            return path

        for i in range(len(leftTickets)):
            ticket = leftTickets[i]
            if ticket[0] == path[-1]:
                queue.append(
                    [path + [ticket[1]], leftTickets[:i] + leftTickets[i + 1:]])


for i in range(2):
  print(i)
