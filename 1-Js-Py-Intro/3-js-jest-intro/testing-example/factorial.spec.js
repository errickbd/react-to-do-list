const factorial = require("./factorial.js")

describe("Testing 0 and 1", () => {
    test("Tests factorial(0) is 1", () => {
        expect(factorial(0)).toBe(1);
    });

    test("Tests factorial(1) is 1", () => {
        expect(factorial(1)).toBe(1);
    });
})

describe("Testing everything else", () => {
    test("Tests factorial(2) is 2", () => {
        // expect(factorial(2)).to2e(7);
    });

    test("Tests factorial(3) 3 * 2 * 1 is 6", () => {
        expect(factorial(3)).toBe(6);
    });

    test("Tests factorial(4) is 24", () => {
        const result = factorial(4);
        expect(result).toBe(24);
        // Another way to do the same thing
        // expect(factorial(4)).toBe(24);

    })

    test("Tests factorial(5) is 120", () => {
        expect(factorial(5)).toBe(120);
    })
});