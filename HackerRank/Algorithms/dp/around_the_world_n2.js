/*

AROUND THE WORLD:
Naive Strategy: calculate all possible circuits. O(n^2)
Dynamic Programming Strategy:
    * Start at city 0, calculate how much fuel we have in the tank at each stop, assuming we move to the next stop.
    * Save the minimum value as min_fuel[0]
    * Let starting_fuel = amount of fuel I have at a given city, if I start on that city == a[i] - b[i]
    * Calculate min_fuel for values in 0...n using following formula:
        min_fuel[i] = min_fuel[i-1] - starting_fuel[i-1]
    * Count number of times min_fuel is >= 0 and return it
    O(n)
    
NOOOO: forgot about C --> capacity of tank. Only works if tank has unlimited capacity :(

NEW STRATEGY:
Let 
F(i) = number of cities I can start at and reach city i
= 0         i == 0
= 

LET'S BRUTE FORCE IT WITH SOME OPTIMIZATIONS AND SEE IF IT WORKS :) :)
It didn't!

*/

const BigNumber = require('bignumber.js');

function possibleCities (numCities,capacity,available,required) {
    //debug(numCities,capacity,available,required);
    let validStarts = findValidStarts(available,required);
    let possibleStarts = 0;
    validStarts.forEach(startCity => {
       if (completeTour(numCities,startCity,capacity,available,required)) {
           possibleStarts++;
       }
    });
    console.log(possibleStarts);
}

function findValidStarts (available,required) {
    let validStarts = [];
    for (let i=0;i<available.length;i++) {
        if (! available[i].minus(required[i]).isNegative() ) {
            validStarts.push(i);
        }
    }
    return validStarts;
}

function completeTour (numCities,startCity,capacity,available,required) {
    let currentFuel = new BigNumber(0);
    for (let i=0; i < numCities; i++) {
        let currentCity = (startCity + i) % numCities;
        currentFuel = currentFuel.plus(available[currentCity]);
        if (currentFuel.greaterThan(capacity)) {
            currentFuel = capacity;
        }
        currentFuel = currentFuel.minus(required[currentCity]);
        if (currentFuel.isNegative()) {
            return false;
        }
    }
    return true;
}

function debug (numCities,capacity,available,required) {
    console.log(numCities.toString());
    console.log(capacity.toString());
    console.log(available.map(num => num.toString()));
    console.log(required.map(num => num.toString()));
}

function solve() {
    getData(data => processData(data,possibleCities))
}

function processData(input,cb) {
    let fields = input.split('\n');
    const convert = arr => arr.split(' ').map(chars => new BigNumber(chars));
    let [numCities,capacity] = convert(fields[0]);
    let available = convert(fields[1]);
    let required = convert(fields[2]);
    cb(numCities,capacity,available,required);
} 

function getData (cb) {
    process.stdin.resume();
    process.stdin.setEncoding("ascii");
    _input = "";
    
    process.stdin.on("data", function (input) {
        _input += input;
    });

    process.stdin.on("end", function () {
        cb(_input);
    });
}

solve();
