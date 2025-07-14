class solution3:
    def removeDuplicate(self,nums):
        my_set=set(nums)
        my_set=list(my_set)
        return my_set
obj=solution3()
array=list(map(int,input("enter a number:").split()))
result=obj.removeDuplicate(array)
print(result)