def increasingTriplet(nums):
    # Initialize first and second to very large values
    first = float('inf')
    second = float('inf')

    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            # Found n > first and n > second
            return True

    return False


# ---------------- MAIN / CALLABLE PART ----------------
if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    nums3 = [2, 1, 5, 0, 4, 6]

    print("Input:", nums1, "→", increasingTriplet(nums1))
    print("Input:", nums2, "→", increasingTriplet(nums2))
    print("Input:", nums3, "→", increasingTriplet(nums3))