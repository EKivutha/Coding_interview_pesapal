

function testSomeNumbers(limit, n) {
    if (n < 3)
        return;

    for (let a = 1; a <= limit; a++)
        for (let b = a; b <= limit; b++) {
            // Check if there exists a triplet
            // such that a^n + b^n = c^n
            let pow_sum = (Math.pow(a, n)
                + Math.pow(b, n));
            let c = Math.pow(pow_sum, 1.0 / n);
            let c_pow = Math.pow(Math.round(c), n);
            if (c_pow == pow_sum) {
                document.write("Count example found");
                return;
            }
        }

    document.write("No counter example within given" +
        " range and data");
}


// Driver Code

testSomeNumbers(12, 5);


