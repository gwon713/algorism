def solution(nums):
    max = len(nums)/2
    nset = set(nums)
    new_nums = list(nset)
    if len(new_nums)>max:
        return len(nums)/2
    else:
        return len(new_nums)