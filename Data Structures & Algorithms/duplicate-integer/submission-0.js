class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let dict1 = new Set(nums);
        return !(dict1.size === nums.length)
    }
}
