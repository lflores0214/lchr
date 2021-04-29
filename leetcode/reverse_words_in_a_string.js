/**
 * @param {string} s
 * @return {string}
 */

// understand 
// inputs 
var reverseWords = function(s) {
    let arr = s.split(" ")
    
    arr.reverse()
    string = arr.join(" ")
    string = string.replace(/\s+/g, ' ')
    return string.trim()
};