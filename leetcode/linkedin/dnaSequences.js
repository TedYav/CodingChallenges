/**
 * STRATEGY:
 * 
 * NAIVE: count all 10 character strings as strings --> O(n) BUT constant factor of 10, can do better!
 * 
 * BETTER:
 *  Treat ACTG string as base 4 number. Thus any 10 character subsequence will have unique numeric value.
 *  Use math to calculate new number based on previous number in O(1) time rather than in 10 operations to generate new string.
 *  Keep track of current numbers in hashmap --> when number has been found twice set its key to true.
 *  First time we set number to true, copy current string to output array.
 * 
 *  Thus we only have constant factor of 10 m times, where m is # of duplicated sequences.
 * @param {string} s
 * @return {string[]}
 */
 
 
const sumInBase = (arr,mapping,base) => {
    return arr.reduce((sum,nextBase) => sum * base + mapping[nextBase],0);
};

// to make this TRULY functional, I need lazy array evaluation functions :)
// then I can keep a current window on the array

const repeatedSequences = (dnaSequence, targetLength, mapping, initialSum) => {
    const base = Object.keys(mapping).length;
    const firstDigit = base ** (targetLength - 1);
    return Array.from(Object.entries(Array.prototype.slice.call(dnaSequence,targetLength)
                .reduce((acc,nextBase) => {
                    acc.currentSum -= mapping[dnaSequence[acc.currentStart]] * firstDigit;
                    acc.currentSum *= base;
                    acc.currentSum += mapping[nextBase];
                    
                    acc.currentStart += 1;
                    
                    if (acc.baseMap.has(acc.currentSum)) {
                        acc.baseMap.get(acc.currentSum).push(acc.currentStart);
                    } else {
                        acc.baseMap.set(acc.currentSum,[acc.currentStart]);
                    }
                    
                    return acc;
                }, {
                    baseMap: new Map().set(initialSum, [0]),
                    currentSum: initialSum,
                    currentStart: 0,
                }))
                .filter(entry => entry[0] === 'baseMap')
                .map(arr => arr[1])
                .reduce((res,entry) => entry)   // roundabout way of getting map out of object :)
                .entries())
                .filter(entry => entry[1].length > 1)
                .map(entry => entry[1])
                .map(startPoints => Array.prototype.slice.call(dnaSequence,startPoints[0],startPoints[0] + targetLength))
                .map(arr => arr.join(''))
}
 

var findRepeatedDnaSequences = function(dnaSequence) {
    const targetLength = 10;
    const firstDigit = 4**9;
    const baseMapping = {A: 0, C: 1, G: 2, T: 3};
    const initialSum = sumInBase(Array.prototype.slice.call(dnaSequence,0,10),baseMapping,4);
    
    if(dnaSequence.length < targetLength) return [];
    
    /*
    design decision:
    * I can calculate initial sum using Array.slice and then use Array.slice to pass the next into reduce.
        DISADVANTAGE: copies array inefficiently
    * I can keep track of current position in array using a variable in the accumulator for reduce
        DISADVANTAGE: basically turns this into a disguised for loop
    * I can use RxJS or something to allow me to operate on a lazily evaluated iteration of the array
        DISADVANTAGE: requires external library
        
    I'm going with option 1 to write this functionally and sacrifice some speed.
    */
    
    return repeatedSequences(dnaSequence,
                             targetLength,
                             baseMapping,
                             initialSum,
                             firstDigit);
};
