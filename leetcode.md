Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
We don't actually need to store the window in a separate array. All we need is some variable, let's call it curr, that keeps track of the current sum. When we add a new element from the right, we just do curr += nums[right].
When we remove an element from the left, we just do curr -= nums[left]. This way, all operations are done in 


Next, how do we move the pointers left and right? Remember, we want to keep expanding our window, and the window always slides to the right - it just might shrink a few times in between. Because right is always moving forward,
we can use a for loop to iterate right over the input. In each iteration of the for loop, we will be adding the element nums[right] to our window.
function fn(nums, k):
    left = 0
    curr = 0
    answer = 0
    for (int right = 0; right < nums.length; right++):
        curr += nums[right]
        while (curr > k):
            curr -= nums[left]
            left++

        answer = max(answer, right - left + 1)

    return answer
Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.

def find_length(nums,k):
    ans=curr=left=0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans,right-left+1)
    return ans

nums = [1, 2, 1, 3, 4, 5, 2, 1]
k = 7
result = find_length(nums, k)
print(result)

Example 2: You are given a binary substring s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
def find_length(s):
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


def generate_test_cases():
    test_cases = []

    # Test case 1: String with alternating '0's and '1's
    test_cases.append(("010101010", 3))

    # Test case 2: String with only '1's
    test_cases.append(("111", 3))

    # Test case 3: String with only '0's
    test_cases.append(("00000", 1))

    # Test case 4: String with multiple segments of '0's separated by '1's
    test_cases.append(("110011", 4))

    # Test case 5: String with multiple segments of '1's separated by '0's
    test_cases.append(("101010", 3))

    return test_cases


def run_test_cases():
    test_cases = generate_test_cases()
    for i, (s, expected_output) in enumerate(test_cases):
        result = find_length(s)
        print(f"Test Case {i + 1}:")
        print(f"Input: {s}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {result}")
        print("")


run_test_cases()
