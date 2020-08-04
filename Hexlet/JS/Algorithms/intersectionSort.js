// BEGIN (write your solution here)
const getIntersectionOfSortedArrays = (arr1, arr2) => {
    const res = [];

    let i1 = 0;
    let i2 = 0;

    while (i1 < arr1.length && i2 < arr2.length) {
        const first = arr1[i1];
        const second = arr2[i2];

        if (first === second) {
            res.push(first);
            i1 += 1;
            i2 += 1;
        } else if (first < second) {
            i1 += 1;
        } else if (first > second) {
            i2 += 1;
        }
    }

    return res;
};
// END



describe('getIntersectionOfSortedArrays', () => {
    it('test 1', () => {
        const actual = getIntersectionOfSortedArrays([], []);
        expect(actual).toEqual([]);
    });

    it('test 2', () => {
        const actual = getIntersectionOfSortedArrays([1], []);
        expect(actual).toEqual([]);
    });

    it('test 3', () => {
        const actual = getIntersectionOfSortedArrays([], [2]);
        expect(actual).toEqual([]);
    });

    it('test 4', () => {
        const actual = getIntersectionOfSortedArrays([10, 11, 24], [-2, 3, 4]);
        expect(actual).toEqual([]);
    });

    it('test 5', () => {
        const actual = getIntersectionOfSortedArrays([10, 11, 24], [10, 13, 14, 18, 24, 30]);
        expect(actual).toEqual([10, 24]);
    });

    it('test 6', () => {
        const actual = getIntersectionOfSortedArrays([3, 5, 10], [10, 12, 19, 21]);
        expect(actual).toEqual([10]);
    });

    it('test 7', () => {
        const actual = getIntersectionOfSortedArrays([10, 12, 19, 21], [3, 5, 10]);
        expect(actual).toEqual([10]);
    });
});
