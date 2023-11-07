def main():
    ##################################################
    # Comlete your code here
    ##################################################
    """
    Use following variables to save your result
    total 
    average
    """
    score1 = int(input('Enter the score 1: '))
    score2 = int(input('Enter the Score 2: '))
    score3 = int(input('Enter the score 3: '))
    total = score1 + score2+ score3
    average = total / 3
    print (f'Total is  {total:10d}' )
    print (f'Average is {average:.2f}')

    ########################################
    # Do not delete the return statement
    ########################################
    return total, average


if __name__ == '__main__':
    main()
