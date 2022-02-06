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


console.log(factorial(7));