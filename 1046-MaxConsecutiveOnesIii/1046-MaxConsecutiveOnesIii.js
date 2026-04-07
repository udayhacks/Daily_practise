// Last updated: 07/04/2026, 11:37:23
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let i= 0 ;
    let zero = [];
    let ans = 0 
    let pos = -1 
    let countK = 0

    for (let j = 0 ;j<nums.length;j++){
        if (nums[j] === 0 ){
            countK++;
            zero.push(j);
        }
        if (nums[j] === 0  && countK> k ){
            pos = zero[i];
            i++;

        }
        ans = Math.max(ans,j-pos);
    }
    return ans 
};