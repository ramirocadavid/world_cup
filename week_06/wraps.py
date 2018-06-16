def sum_digits(num):
    '''A function to sum up the digits of an integer. Negative integers will be processed according to their absolute value'''
    #catch if input is not an integer
    if type(num) != int:
        print("Error: Only integers accepted")
    else:
        # change number to integer, and turn it positive
        num_int = int(num)
        if num_int < 0:
            num_int *= -1
        tot = 0
        # use integer division and modulo operator to get sum of digits
        while num_int > 0:
            tot_adder = num_int % 10
            tot = tot + tot_adder
            num_int = num_int // 10
        return(tot)
		
def diff_sum_digits(num):
    '''A function that takes the difference between an input integer and the sum of its digits'''
    sum_of_digits = sum_digits(num)
    ans = abs(num - sum_of_digits)
    return(ans)
	
def wraps_diff_sum_digits(num):
    '''A function that will take an input integer and subtract the sum of digits from the value of the number.\
    This will be repeated until the result is a single digit integer.'''
    while num > 10:
        num = diff_sum_digits(num)
    return(num)