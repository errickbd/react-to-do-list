/**
 * A factorial is ... 5! is 5 * 4 * 3 * 2 *1 
 * 4! is 4 * 3 * 2 * 1
 * 3! is 3 * 2 *1
 */
function factorial(num) {
    let product = 1;

    for(let i = num; i > 0; i--) {
        product = product * i;
    }

    return product;
}

// console.log(factorial(4))

module.exports = factorial;