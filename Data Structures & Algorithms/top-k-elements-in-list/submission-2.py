class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}  # Dictionary to count occurrences

        # Step 1: Count the occurrences of each number
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        # Step 2: Convert dictionary to a list of (number, frequency) tuples
        freq_list = []
        for key in num_dict:
            freq_list.append((key, num_dict[key]))  # Store tuples (num, frequency)

        # Step 3: Custom sort function (Sort by frequency in descending order)
        def custom_sort(pair):
            return pair[1]  # We return the frequency (2nd element of tuple)

        freq_list.sort(reverse=True, key=custom_sort)  # Sort descending by frequency

        # Step 4: Extract the top k elements
        result = []
        for i in range(k):
            result.append(freq_list[i][0])  # Only store the numbers, not their counts

        return result

