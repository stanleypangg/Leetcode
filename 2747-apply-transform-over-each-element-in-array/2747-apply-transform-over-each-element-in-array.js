/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    ret = [];
    for (let i = 0; i < arr.length; i++) {
        ret[i] = fn(arr[i], i);
    }
    return ret;
};