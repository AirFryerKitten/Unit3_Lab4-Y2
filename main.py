#Jonas York
#U3 L4
#Binary Search

def binary_search (target, nums, pointer = 0):
  if len(nums) == 1:
    #print("BASE CASE REACHED")
    if nums[0] == target:
      #print(f"Returning {nums}")
      return pointer
    else:
      #print(f"Returning None")
      return None

  splitLocation = int(len(nums)/2)
  number = nums[splitLocation]
  if number == target:
    #print("Number and target are equal\n")
    pointer += splitLocation
    return pointer
  elif number < target:
    #print("Target is greater\n")
    new_nums = nums[splitLocation:]
    pointer += splitLocation 
    #print(f"New list: {new_nums}")
    ind = binary_search(target,new_nums,pointer)
  elif number > target:
    #print("Number is greater\n")
    new_nums = nums[:splitLocation]
    #print(f"New list: {new_nums}")
    ind = binary_search(target,new_nums)
  
  return ind

    
  
  

def subMain():
  binary_search(2, [1])
  


def main():
    nums = [1,2,3,4,5,6,7,8,9]

    test1 = binary_search(2, nums)
    print("\n\nTest 1 - search for 2")
    print(f"Your returned index: {test1}")
    print(f"Test passed? {test1 == 1}\n\n")

    test2 = binary_search(7, nums)
    print("Test 2 - search for 7")
    print(f"Your returned index: {test2}")
    print(f"Test passed? {test2 == 6}\n\n")

    test3 = binary_search(9, nums)
    print("Test 3 - search for 9")
    print(f"Your returned index: {test3}")
    print(f"Test passed? {test3 == 8}\n\n")
    
    test4 = binary_search(99, nums)
    print("Test 4 - number doesn't exist")
    print(f"Your returned index: {test4}")
    print(f"Test passed? {test4 == None}\n\n")

if __name__ == "__main__":
  main()
