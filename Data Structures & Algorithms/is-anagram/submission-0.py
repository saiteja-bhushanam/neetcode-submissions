class Solution:
    def return_dict(a:str) -> dict:
        dict_ = {}
        for i in a:
            if i in dict_.keys():
                dict_[i]+=1
            else:
                dict_[i] = 1
        return dict_

    def isAnagram(self, s: str, t: str) -> bool:
        if Solution.return_dict(s) == Solution.return_dict(t):
            return True
        else:
            return False


    

        