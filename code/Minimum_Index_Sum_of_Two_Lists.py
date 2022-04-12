"""
599.Minimum Index Sum of Two Lists [Easy]
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map={}
        list2_map={}
        for i in range(len(list1)):
            list1_map[list1[i]] = i
        for i in range(len(list2)):
            list2_map[list2[i]] = i
        
        minimum = float('inf')
        res=[]
        for item in list1_map:
            if item in list2_map:
                if list1_map[item]+list2_map[item] < minimum:
                    res=[item]
                    minimum = list1_map[item]+list2_map[item]
                elif list1_map[item]+list2_map[item] == minimum:
                    res.append(item)
                
        return res