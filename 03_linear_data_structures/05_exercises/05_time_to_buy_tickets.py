# Queue solution: Time O(n x m), Space O(n)
from collections import deque


def time_to_buy_tickets(tickets, k):
    queue = deque((i, t) for i, t in enumerate(tickets))
    # queue: [(0,2),(1,3),(2,2)]

    time = 0

    while queue:
        person, remaining = queue.popleft()

        time += 1
        remaining -= 1

        if person == k and remaining == 0:
            return time

        if remaining > 0:
            queue.append((person, remaining))

    return time


# --- Test: time_to_buy_tickets ---
print(time_to_buy_tickets([2, 3, 2], 2))  # 6
# queue: [(0,2),(1,3),(2,2)]
# t=1: pop (0,2)→(0,1), not k=2, requeue → [(1,3),(2,2),(0,1)]
# t=2: pop (1,3)→(1,2), not k=2, requeue → [(2,2),(0,1),(1,2)]
# t=3: pop (2,2)→(2,1), not done yet, requeue → [(0,1),(1,2),(2,1)]
# t=4: pop (0,1)→(0,0), not k=2, done, leave → [(1,2),(2,1)]
# t=5: pop (1,2)→(1,1), not k=2, requeue → [(2,1),(1,1)]
# t=6: pop (2,1)→(2,0), person==k and remaining==0 → return 6 ✓

print(time_to_buy_tickets([5, 1, 1, 1], 0))  # 8


# No-Queue solution: Time O(n), Space O(1)
def time_to_buy_tickets_no_queue(tickets, k):
    time = 0

    for i in range(len(tickets)):
        # tickets = [2, 3, 2], k = 2, tickets[k] = 2
        if i <= k:
            # Person i is in front of or at k — they buy before k every round.
            #
            # i=0: person 0 needs 2 tickets, k needs 2 → min(2, 2) = 2
            #      person 0 buys in round 1 and round 2 → contributes 2 seconds ✓
            #
            # i=1: person 1 needs 3 tickets, k needs 2 → min(2, 3) = 2
            #      person 1 wants 3 rounds but queue only runs 2 → contributes 2 seconds ✓
            #
            # i=2: person 2 IS k, needs 2 tickets → min(2, 2) = 2
            #      k buys in round 1 and round 2 → contributes 2 seconds ✓
            time += min(tickets[k], tickets[i])
        else:
            # Person i is behind k — they buy after k each round.
            # On k's final round, k finishes and the queue stops before reaching i.
            # So person i only gets tickets[k] - 1 = 2 - 1 = 1 round.
            #
            # Example with tickets = [2, 3, 2, 5], k = 2:
            # i=3: person 3 needs 5 tickets, but only gets 1 round → min(1, 5) = 1
            time += min(tickets[k] - 1, tickets[i])
    return time


# --- Test: def time_to_buy_tickets_no_queue ---
print(time_to_buy_tickets_no_queue([2, 3, 2], 2))  # 6
# tickets[k]=2, so 2 rounds
# i=0 (<=k): min(2, 2) = 2
# i=1 (<=k): min(2, 3) = 2  ← person 1 wants 3 but queue stops after 2 rounds
# i=2 (==k): min(2, 2) = 2
# total = 2 + 2 + 2 = 6 ✓


print(time_to_buy_tickets_no_queue([5, 1, 1, 1], 0))  # 8
