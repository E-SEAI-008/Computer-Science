# Default solution: Time O(n²), Space O(1)
def can_attend_meetings(intervals):
    def overlap(interval_1, interval_2):
        return (
            interval_1[0] > interval_2[0]
            and interval_1[0] < interval_2[1]
            or interval_2[0] > interval_1[0]
            and interval_2[0] < interval_1[1]
        )

    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if overlap(intervals[i], intervals[j]):
                return False
    return True


# --- Test: can_attend_meetings ---
print("--- can_attend_meetings ---")
print(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))  # False
# overlap([0,30], [5,10]): 5 > 0 and 5 < 30 → True → return False immediately

print(can_attend_meetings([[7, 10], [2, 4]]))  # True
# overlap([7,10], [2,4]): 7 > 2 and 7 < 4 → False. 2 > 7 → False → no overlap
# → return True


# Efficient: Sort then scan — Time O(n log n), Space O(1)
from itertools import pairwise


def can_attend_meetings_efficient(intervals):
    intervals.sort(key=lambda x: x[0])
    for prev, curr in pairwise(intervals):
        if prev[1] > curr[0]:
            return False
    return True


# --- Test: can_attend_meetings_efficient ---
print("\n--- can_attend_meetings_efficient ---")
print(can_attend_meetings_efficient([[0, 30], [5, 10], [15, 20]]))  # False
# After sort: [[0,30],[5,10],[15,20]]
# prev=[0,30], curr=[5,10]: 30 > 5 → True → return False immediately

print(can_attend_meetings_efficient([[7, 10], [2, 4]]))  # True
# After sort: [[2,4],[7,10]]
# prev=[2,4], curr=[7,10]: 4 > 7 → False → loop ends → return True
