class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> d = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;

            if(d.containsKey(diff)) {
                return new int[] { d.get(diff), i} ;
            }

            d.put(num, i);
        }
        return new int[] {};
    }
}
