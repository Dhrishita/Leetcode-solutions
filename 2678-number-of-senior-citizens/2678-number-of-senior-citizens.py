class Solution(object):
    def countSeniors(self, details):
        cnt=0
        for i in details:
            age_str=i[11:13]
            age=int(age_str)
            if age>60:
                cnt+=1
        return cnt