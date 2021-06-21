// Time Complexity O(2^n)
// Space Complexity O(n)

const fibV1 = (n) => {
    if (n <= 2) return 1;
    return fibV1(n - 1) + fibV1(n - 2);
}

// console.log(fibV1(8)) // 21
// console.log(fibV1(13)) // 233
// console.log(fibV1(50)) // 12586269025


// Memoized Version of Fibonacci Sequence
// Time Complexity O(n)
// Space Complexity O(n)

const fibV2 = (n, memo = {}) => {
    if (n in memo) return memo[n];
    if(n <= 2) return 1;
    memo[n] = fibV2(n - 1, memo) + fibV2(n - 2, memo);
    return memo[n];
}

console.log(fibV2(8)) // 21
console.log(fibV2(13)) // 233
console.log(fibV2(50)) // 12586269025