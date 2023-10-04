def sum_of_intervals(intervals):
    count = 0
    intervals =  sorted(set(intervals))
    if len(intervals) >= 2:
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                match intervals[i+1][1] >= intervals[i][1]:
                    case True: intervals[i+1] = (intervals[i][0], intervals[i+1][1])
                    case _: intervals[i+1] = (intervals[i][0], intervals[i][1])
                intervals[i] = set()
        intervals = [i for i in intervals if i != set()]
        for interval in intervals:
            count += interval[1] - interval[0]
    else:
        return intervals[0][1] - intervals[0][0]
    return count