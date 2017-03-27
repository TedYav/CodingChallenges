/**
 * 
 * NAIVE SOLUTION:
 *  O(n^2) --> look at first, compare to all the others, etc etc.
 * BETTER SOLUTION:
 *  O(nlogn) + O(n) ==> sort by start number, then reduce adjacent intervals as needed. Return result.
 * 
 * 
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
 
var merge = function(intervals) {
  return intervals
    .sort((interval1, interval2) => interval1.start - interval2.start)
    .reduce((result, nextInterval) => {
        if(result.length > 0 && (result[result.length - 1].end >= nextInterval.start)) {
            result[result.length - 1].end = Math.max(result[result.length - 1].end, nextInterval.end);
        } else {
            result.push(nextInterval);
        }
        return result;
    },[])
};
