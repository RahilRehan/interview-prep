def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # get sign
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1

    # remove sign from integers
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # result cannot exceed len(num1) + len(num2) , https://www.quora.com/Is-there-a-formula-to-calculate-the-total-number-of-digits-in-the-product-of-two-numbers
    result = [0] * (len(num1) + len(num2) + 1)

    # grade school multiplication
    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            result[i + j + 1] += num2[i]*num1[j]
            result[i + j] += result[i + j + 1]//10
            result[i + j + 1] %= 10

    # remove leading zeros in result
    for i in range(len(result)):
        if result[i]!=0:
            result = result[i:len(result)]
            break
        if i == len(result)-1 and result[i] == 0:
            return [0]

    return [sign * result[0]] + result[1:]