// Last updated: 07/04/2026, 11:34:46
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    for (let i = 0 ; i < nums.length;i++){
        init=(fn(init,nums[i]));
    }
    return init ;
};