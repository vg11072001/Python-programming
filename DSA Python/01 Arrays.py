# %%
import typing
import collections
import heapq
from typing import List
from collections import defaultdict, Counter


# %%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Store the product of nums except that same index int to new array.

        >> created 2 arrays to solve
        #!  three loops that iterate over the nums list, each taking O(n) Time complexity
        -----------------------------------------------------------------
        Calculate the prefix_product array and postfix_product array,
        then calculate the ith index of out array using these array with
        i-1 index and i+1 index respectively
        -----------------------------------------------------------------

        """
        prefix_prod = [0] * len(nums)
        prefix_prod[0] = nums[0]
        postfix_prod = [0] * len(nums)
        postfix_prod[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_prod[i] = nums[i] * prefix_prod[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix_prod[i] = nums[i] * postfix_prod[i + 1]

        # print(prefix_prod)
        # print(postfix_prod)

        nums[0] = postfix_prod[1]
        nums[-1] = prefix_prod[-2]
        for i in range(1, len(nums) - 1):
            nums[i] = prefix_prod[i - 1] * postfix_prod[i + 1]

        # print(nums)
        return nums

    # %%
    # class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Store the product of nums except that same index int to new array.

        >> used variables to store the intermidiate values
        #! time complexity of this code is O(n)
        -----------------------------------------------------------------
        Given an array nums of n integers where n > 1, return an array output such that
        output[i] is the product of all the elements of nums except nums[i].
        -----------------------------------------------------------------

        """
        n = len(nums)
        output = [0] * n
        prefix = 1
        for i in range(n):
            output = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

    # %%
    # class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check if the given Sudoku board is valid.

        >> #? defaultdict(set) to store the values for each row, column and square
        >> check the condition if already in set return False
        >> else add() on set
        #! Time complexity O(n^2)
        -----------------------------------------------------------------
        Using Hashset and grouping of rows and columns to identify each 3*3 grid within 9*9 by diving index of 9 by 3.
        Steps: first initiate the hashsets 3, for each value check if already in hashset else add the value to hashset.
        -----------------------------------------------------------------

        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(
            set
        )  # in this key = rowi//3 , coli//3

        for rowi in range(9):
            for coli in range(9):
                if board[rowi][coli] == ".":
                    continue
                if (
                    board[rowi][coli] in rows[rowi]
                    or board[rowi][coli] in cols[coli]
                    or board[rowi][coli] in square[(rowi // 3, coli // 3)]
                ):
                    return False
                rows[rowi].add(board[rowi][coli])
                cols[coli].add(board[rowi][coli])
                square[(rowi // 3, coli // 3)].add(board[rowi][coli])

        return True

    # %%
    # class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given a non-empty array of integers nums and an integer k, return the k most frequent elements.

        >> using Bucket Sort
        # ! O(n)
        -----------------------------------------------------------------
        index = count and value = number
        then fill that hashmap and check from last if value is present then append that numbers on hashmap.val
        Count frequency > Store in buckets > Iterate in reverse > Add to result
        -----------------------------------------------------------------

        """
        count = {}
        m = len(nums)
        bucket = [[] for _ in range(m + 1)]

        for i in range(m):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for n, c in count.items():
            bucket[c].append(n)
        result = []
        for i in range(len(bucket) - 1, 0, -1):

            # * first
            # for j in bucket[i]:
            #     result.append(j)
            #     if len(result) == k:
            #         return result

            # * second
            result.extend(bucket[i])
            if len(result) == k:
                return result

    # %%
    # class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given a non-empty array of integers nums and an integer k, return the k most frequent elements.

        >> used collections.Counter.most_common() to count the frequency of each number in array
        >> used list comprehension to get the keys of the hashmap
        # ! O(n logk) Time Complexity
        -----------------------------------------------------------------
        use most_common function
        -----------------------------------------------------------------
        """

        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]

    # %%
    # class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given a non-empty array of integers nums and an integer k, return the k most frequent elements.

        >> used sorted() for hashmap on basis of values
        >> lambda item: item[1]
        #!  the time complexity is O(n log n) due to the sorting step.
        -----------------------------------------------------------------
        lambda function used that extracts the second element (frequency) from each tuple in the list,
        allowing sorted() to sort by frequency.
        -----------------------------------------------------------------

        """
        abc = {}
        out = []
        for i in nums:
            if i not in abc:
                abc[i] = 0
            abc[i] = abc[i] + 1

        abc = sorted(abc.items(), key=lambda item: item[1], reverse=True)
        # print(abc)
        for i in range(k):
            out.append(abc[i][0])
        return out

    # %%
    # class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given a non-empty array of integers nums and an integer k, return the k most frequent elements.

        >> used collections.Counter to count the frequency of each number in array
        >> used heapify to get the top k frequent elements : heapq - heapify, heapop
        #! O(n log k) Time Complexity
        -----------------------------------------------------------------
        Using heapify, found top value
        -----------------------------------------------------------------

        """
        has = Counter(nums)
        ans = []
        heap = [(-p, d) for d, p in zip(has.keys(), has.values())]
        heapq.heapify(heap)
        for i in range(k):
            x, y = heapq.heappop(heap)
            ans.append(y)
        return ans

        # * more shortcut
        # freq_map = {}
        # for num in nums:
        #     freq_map[num] = freq_map.get(num, 0) + 1
        # return heapq.nlargest(k, freq_map, key=freq_map.get) #* heapq.nlargest

    # %%
    # class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group anagrams together.

        >> #? the usecase of hashmap (collections.defaultdict) in string as key and value
        >> sorted check the array with hashmap key
        >> then append it to the hashmap, then return the values of hashmap
        #! O(n log n) Time Complexity
        -----------------------------------------------------------------
        for each string sort it and store in dict
        -----------------------------------------------------------------
        """
        ##* first
        # has = defaultdict(list)
        # for s in strs:
        #     has[''.join(sorted(s))].append(s)
        # return list(has.values())

        ##* second
        has = {}
        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x not in has.keys():
                has[x] = [strs[i]]
            else:
                has[x].append(strs[i])
        return list(has.values())

    # %%
    # class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group anagrams together.

        >> #? res = defaultdict(list) , res[tuple(count)].append(word)
        >> #? count[ord(char) - ord('a')]
        #! O(m*n) Time Complexity
        -----------------------------------------------------------------
        a-z (26 charac) so count[a-z] = 1e, 1a, 1t. Counting each charac of each string in a array 26 len
        store that array as key and store values using simply appending on earlier hashmap
        -----------------------------------------------------------------
        """
        res = defaultdict(list)  # to map charac count to list of Anagrams
        for word in strs:
            count = [0] * 26  # count each charac in the word from a...z
            for char in word:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(word)
        return res.values()

    # %%
    # class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return _indices of two numbers such that they add up to target_.

        >> used 'in' operator to check if target - nums[i] exists in array
        #! O(n) Time Complexity
        -----------------------------------------------------------------
        count frequency of each number in array, if any number has frequency more than 1, return True
        -----------------------------------------------------------------
        """
        # * first
        for i in range(len(nums)):
            if (target - nums[i] in nums) and (
                i != nums.index(target - nums[i])
            ):
                return [i, nums.index(target - nums[i])]
        return []

    # %%
    # class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Check if two numbers in an array add up to a specific target.

        >> used 'hash' dictionary to store each number and its index
        >> used 'target - nums[i]' to find the complement of current number
        #! O(n) Time Complexity
        -----------------------------------------------------------------
        store each number and its index in a dictionary, if target - current number exists in dictionary, return their indices
        -----------------------------------------------------------------
        """
        hash = {}
        for i, n in enumerate(nums):
            if target - n in hash:
                return [hash[target - n], i]
            hash[n] = i
        return

    # %%
    # class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams.

        >> used ' '.join(sorted(s)) to make all string same
        >> used '==', to compare the sorted strings
        #! O(n log n) Time Complexity
        O(n log n) + O(n) + O(n) = O(n log n)
        -----------------------------------------------------------------
        sort the strings, join and then compare them.
        -----------------------------------------------------------------
        """
        s = " ".join(sorted(s))
        t = " ".join(sorted(t))
        return s == t

    # %%
    # class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if an array contains duplicate elements.

        >> used 'collections.Counter' to count the frequency of each number in array
        >> used '!= 0' to check if any number has frequency more than 1
        #! O(n) Time Complexity
        -----------------------------------------------------------------
        count frequency of each number in array, if any number has frequency more than 1, return True
        -----------------------------------------------------------------
        """
        # * first
        return len(nums) != len(Counter(nums))
        # * second
        # return len(nums) - len(set(nums)) != 0
        # * thrid
        # return any(Counter(nums)[num] > 1 for num in nums)

    # %%
    # class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if an array contains duplicate elements.

        >> #? Hashset() defined then add value,
        >> if value already in set then return True
        #! O(n) Time Complexity
        -----------------------------------------------------------------
        add each number to the set, if it already exists in the set, return True
        -----------------------------------------------------------------
        """
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False
