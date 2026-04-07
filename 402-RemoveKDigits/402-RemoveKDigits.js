// Last updated: 07/04/2026, 11:39:05
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {
    
     if (k === num.length) {
            return "0";
        }
        
        let stack = [];
        
        for (let digit of num) {
            while (stack.length > 0 && k > 0 && stack[stack.length - 1] > digit) {
                stack.pop();
                k--;
            }
            stack.push(digit);
        }
        
        while (k > 0) {
            stack.pop();
            k--;
        }
        
        let ans = stack.join('').replace(/^0+/, '');
        
        return ans.length ? ans : "0";
    
};