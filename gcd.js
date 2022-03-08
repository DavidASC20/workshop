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