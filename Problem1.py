
def findmissing(nums):
        start=0
        end = len(nums)-1

        while (start<=end):
            mid = start + (end-start)//2
            if nums[mid]==mid+1:
                start=mid+1
            else:
                end=mid-1
        return start+1