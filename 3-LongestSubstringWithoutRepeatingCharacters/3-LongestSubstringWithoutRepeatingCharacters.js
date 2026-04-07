// Last updated: 07/04/2026, 11:44:01
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    let list = new Map();
    let output = 0 ;
    let pos = -1 ; 

        for (let i = 0 ; i<s.length;i++){
            if (list.has(s[i]) && list.get(s[i]) > pos){
                pos= list.get(s[i]);

            }
            list.set(s[i],i);
            output = Math.max(output,i-pos);
        }
        return output;

};