// Team Phantom Tollbooth :: David, Aaron
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-03r
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

factorial = function(n){
    if(n == 1){
        return 1;
    }else{
        return(n * factorial(n-1));
    }
}

function fib(n){
    if(n <= 1){
        return n;
    }else{
        return (fib(n-1) + fib)
    }
}

gcd = function(a, b){
    smallest = a;
    if(a > b){
        smallest = b;
    }
    // console.log("smallest is " + smallest);
    for(let i = smallest; i >= 1; i--){
        // console.log("i is " + i);
        // console.log("a % i is " + a%i)
        // console.log("b % i is " + b%i)
        if(a % i == 0 && b % i == 0){
            return i;
        }
    }
}

console.log(gcd(1290, 186));
console.log(factorial(7));