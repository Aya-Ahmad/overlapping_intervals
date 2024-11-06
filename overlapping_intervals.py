"""
This function merges overlapping intervals ( each interval of size 2 )
and returns a list of the merged intervals
"""
def MergeIntervals ( intervals ):
#list to store the merged intervals
    merged_interval = []
    for i in range ( len (intervals) ):
#to store the current interval
        interval = intervals [i]
#if the merged interval is empty, add the first array in the intervals to it
        if len ( merged_interval ) == 0:
            merged_interval.append ( interval )
#store it as last interval to make a comparison
            last_array = interval
        else:
#if is needed here to check if the current array overlap the last array,
#if yes, we update last array to the end of current array
#if no, we add the current array to merged
            if last_array [1] < interval[0]:
                merged_interval.append ( interval )
#update last array to current interval
                last_array = interval
            else: #  interval[1] > last_array[1]
                if last_array[1] < interval [1]:
                    last_array[1] = interval[1]
    return merged_interval

interval = [[-1,5],[2,5],[6,8],[8,16]]
result = MergeIntervals ( interval )
print ( result )
