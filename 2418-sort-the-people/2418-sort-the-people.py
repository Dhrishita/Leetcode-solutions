class Solution(object):
    def sortPeople(self, names, heights):
        people=list(zip(names,heights))
        people.sort(reverse=True, key=lambda x:x[1])
        sorted_names=[name for name,height in people]
        return sorted_names
        