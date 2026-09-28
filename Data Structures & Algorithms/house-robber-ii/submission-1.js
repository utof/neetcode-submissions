class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        let nums1 = nums.slice(0, -1)
        let nums2 = nums.slice(1)
        let rob1 = 0
        let rob2 = 0
        let first_max;
        let second_max;

        for (let i of nums1) {
            first_max = Math.max(i + rob1, rob2)
            rob1 = rob2
            rob2 = first_max
        }

        rob1 = 0
        rob2 = 0
        for (let i of nums2) {
            second_max = Math.max(i + rob1, rob2)
            rob1 = rob2
            rob2 = second_max
        }
        return Math.max(first_max, second_max) || nums[0]
        
    }
}
