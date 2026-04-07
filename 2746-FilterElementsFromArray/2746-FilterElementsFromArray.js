// Last updated: 07/04/2026, 11:34:49
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let ar = []
    for (let i = 0 ; i <arr.length;i++){
        if (fn(arr[i],i)){
         ar.push(arr[i]);
        }
    }
    return ar;
};