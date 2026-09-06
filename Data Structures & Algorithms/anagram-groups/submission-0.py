class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dupe_dict = {}
        final_list = []

        for check_word in strs:
            sorted_word = ''.join(sorted(check_word))
            if sorted_word not in dupe_dict:
                dupe_dict[sorted_word] = [check_word]
            else:
                dupe_dict[sorted_word].append(check_word)
        print(dupe_dict)

        for sub_lists in dupe_dict.values():
            final_list.append(sub_lists)
        return final_list



