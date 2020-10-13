    # CTI-110
    # P4HW1 - Expenses
    # Jillian Purgason
    # 10/12/2020

def main():
    amt_account = float(input('Enter starting amount in account: $'))
    print()
    expense1 = float(input('Enter expense1:'))                   
    exp_again = input('Do you want to enter another expense?(y/n)')
    print()
    total_exp_amt = expense1
    end_amount = (amt_account - expense1)
    total_exp = 1
    num_exp = 2               
    while exp_again == 'y':
        expense = float(input('Enter expense {}:'.format(num_exp)))
        exp_again = input('Do you want to enter another expense?(y/n)')
        num_exp += 1
        total_exp_amt += expense
        total_exp += 1
        end_amount -= expense
        print()
    
    print('Amount in account before expenses subtracted ${:.2f}'.format(amt_account))
    print('Number of expenses entered:', total_exp)
    print('Amount in account after expenses subtracted is ${:.2f}'.format(end_amount))

if __name__ == "__main__":
    main()



        
        
        
