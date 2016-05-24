""""Summarize ranges
http://www.codewars.com/kata/55fb6537544ae06ccc0000dc

Write

    summary_ranges(nums)

that given a sorted array of numbers, returns the summary of its ranges.
"""


def summary_ranges(nums):
    """Compute ranges in the given array

    Args:
        nums (list): List of ints

    Returns:
        list: List of ranges (ex. ['1->5', '7->9', ...]

    Examples:
        >>> summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10])
        ['0->7', '9->10']
    """
    ranges = []
    try:
        prev, current = nums[0], str(nums[0])
        single = True
        for num in nums[1:]:
            if num - prev > 1:  # New range
                if single:  # Single digit range ends
                    ranges.append(current)
                else:  # Multi digit range ends
                    ranges.append(current + '->' + str(prev))
                current = str(num)
                single = True
            elif num - prev == 1:  # Range continues
                single = False
            prev = num

        # Last character check
        if single:  # Last character is range by itself
            ranges.append(current)
        else:  # Last character ends opened range
            ranges.append(current + '->' + str(nums[-1]))
    except IndexError:
        pass
    return ranges
