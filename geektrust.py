# PROBLEM STATEMENT

# Context
#  Geekdemy provides a wide variety of online education programmes. Students can purchase them and enroll in these programmes. Geekdemy offers attractive discounts through their coupons so that students can spend less while purchasing these programmes

# Programmes
#  There are 3 different categories of online programmes, and the cost is different for each category. A student can purchase any number of programmes at a time.
 
#  CERTIFICATION - Rs.3000 
#  DEGREE - Rs. 5000 
#  DIPLOMA - Rs 2500 
# Coupons
#  The discount coupons offered by Geekdemy are based on different criteria. Only one discount coupon can be applied at a time.
 
#  B4G1 - This coupon is applied automatically if 4 or more programmes are being purchased. The student gets one programme for free. The lowest priced programme is given for FREE.
 
#  DEAL_G20 - This coupon can be applied if the purchased programmes value is Rs.10,000/- or above. It provides a 20% discount on the total programme cost. The coupon needs to be applied explicitly to get a discount.
 
#  DEAL_G5 - This coupon can only be applied if there are a minimum of 2 programmes being purchased. It provides a 5% discount on the total programme cost. The coupon needs to be applied explicitly to get a discount.
 
# Enrollment Fee
#  If the total programme cost is below Rs. 6666/, an extra enrollment fee Rs.500/- is added to the cart. The enrollment fee is applied after the discount. If the total programme cost is or above Rs.6666/- the enrollment fee is waived off.
 
# Pro Membership Fee
#  A student can choose to purchase a Pro Membership for a small amount of Rs.200/- . The pro membership provides an additional membership discount on each of the individual programmes on top of the other discounts.
 
#  DIPLOMA - 1% discount 
#  CERTIFICATION - 2% discount 
#  DEGREE - 3% discount
 
# Assumptions
#  A student can add any number of programmes to the cart. 
#  A student can add the same category of programme multiple times. 
#  A student can choose to buy pro membership or not.  
#  If a student has  purchased a pro membership and has applied for a coupon, The coupon discount is applied after applying the pro membership discounts. 
#  The B4G1 coupon gets auto applied when there are more than 4 programmes in the cart. 
#  All the other coupons (DEAL_G20, DEAL_G5) need to be applied on the cart, if not no discount is provided. 
#  If there are 4 or more programmes in the cart and the student has applied for a coupon other than B4G1, B4G1 coupon will be used, and the other coupon needs to be ignored. 
#  If 2 or more coupons are applied, the higher value coupon needs to be considered (except in the case of 4 or more programmes; in that case B4G1 is auto applied).
# 	eg: if a student applies the coupon DEAL_G20 and DEAL_G5 and the purchase value is greater than 10,000, then DEAL_G20 needs to be considered.
# 	eg: if a student applies the coupon DEAL_G20 and DEAL_G5 and the purchase value is greater than 10,000, then DEAL_G20 needs to be considered. 


# Input Commands & Format
#  Your program should take the purchase details as input.
 
# ADD_PROGRAMME <CATEGORY_1> <QUANTITY> 
#  Adds the specified category and quantity of programme to the purchases 
# APPLY_COUPON <COUPON_NAME> 
#  Applies the discount coupon to the total value of the purchases 
# ADD_PRO_MEMBERSHIP 
#  Adds a pro membership along with other purchases. It applies a membership discount on each programme. 
# PRINT_BILL 
#  Prints the programme purchase details. 

# Output Commands & Format
#  Your program should print the bill details.
 
# SUB_TOTAL <AMOUNT> 
#  This includes all the items purchased (programmes and pro membership) 
#  Print the cost of all the programmes purchased, after applying a pro membership discount (if applicable). 
# COUPON_DISCOUNT <COUPON_NAME> <AMOUNT> 
#  Print the applied coupon and the discounted amount 
#  If the coupon is not applicable, Print “DISCOUNT NONE 0 
# TOTAL_PRO_DISCOUNT <AMOUNT> 
#  Print the total amount discounted through pro membership. 
# PRO_MEMBERSHIP_FEE <AMOUNT> 
#  Print the pro membership fee. 
# ENROLLMENT_FEE <AMOUNT> 
#  Print the enrollment fee. 
# TOTAL <AMOUNT> 
#  Print the total value of the shopping cart after discount is applied. 


from sys import argv

def main():

# Declaring the initial variables
    PURCHASE = {}
    course = []
    quantity = []
    COUPON = []
    ENROLLMENT_FEE = 0
    PRO_MEM_FEE = 0
    cost1, cost2, cost3 = 0, 0, 0
    discount1, discount2, discount3 = 0, 0, 0
    
# Take the input of file name from the user
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    
    
# Sort the inputs from the user into ADD_PROGRAMME, APPLY_COUPON AND PRO_MEMBERSHIP_FEE categories
    for i,j in enumerate(Lines):
        if j.split()[0] == "ADD_PROGRAMME":
            course.append(j.split()[1])
            quantity.append(int(j.split()[2]))
        elif j.split()[0] == "APPLY_COUPON":
            COUPON.append(j.split()[1])
# Insert the input coupon name into a COUPON list because multiple coupons can be given as input but we have to choose the one which is applicable.
        elif j.split()[0] == "ADD_PRO_MEMBERSHIP":
            PRO_MEM_FEE = 200

# Created a dictionary which contains course name as 'keys' and quantity as their respective 'values' as integer
    PURCHASE = dict(zip(course, quantity))

# Calculation of Purchase cost after the deduction of TOTAL_PRO_DISCOUNT if PRO_MEMBERSHIP_FEE is paid by the user
    for i in range(len(PURCHASE.values())):
# For 'CERTIFICATION' course fee is 3000 and PRO_MEMBERSHIP_DISCOUNT is 2%
        if list(PURCHASE.keys())[i] == 'CERTIFICATION':
            cost1 = PURCHASE['CERTIFICATION']*3000
            if PRO_MEM_FEE == 200:
                discount1 = cost1 * 0.02
                cost1 = cost1 - discount1
# For 'DEGREE' course fee is 5000 and PRO_MEMBERSHIP_DISCOUNT is 3%
        elif list(PURCHASE.keys())[i] == 'DEGREE':
            cost2 = PURCHASE['DEGREE']*5000
            if PRO_MEM_FEE == 200:
                discount2 = cost2 * 0.03
                cost2 = cost2 - discount2
# For 'DIPLOMA' course fee is 2500 and PRO_MEMBERSHIP_DISCOUNT is 1%
        else:
            cost3 = PURCHASE['DIPLOMA']*2500
            if PRO_MEM_FEE == 200:
                discount3 = cost3 * 0.01
                cost3 = cost3 - discount3

    TPRO_DIS = discount1 + discount2 + discount3
    TPURCHASE = cost1 + cost2 + cost3 + PRO_MEM_FEE   # Effective cost after deduction of discounts and PRO_MEMBERSHIP_FEE addition

    print(f"SUB_TOTAL {TPURCHASE:.2f}")    # Printing Effective cost after TOTAL_PRO_DISCOUNT deduction

# Calculation for COUPON_DISCOUNT, where B4G1 is applied automatically and DEAL_G20 and DEAL_G5 needs to be applied by the user explicitly
    if sum(quantity) >= 4:      # If the total programme purchased is equal or greater than 4
        if "DIPLOMA" in course:      # If "DIPLOMA" is selected by the user, then the discount will be 2500 (cost of "DIPLOMA" course)
            COUP_DIS = 2500
            TPURCHASE = TPURCHASE - COUP_DIS
            print(f"COUPON_DISCOUNT B4G1 {COUP_DIS:.2f}")
# If "DIPLOMA" is not selected and "DEGREE" and "CERTIFICATION" are selected by the user, then the discount will be 3000 (cost of "CERTIFICATION" course)
        elif "DIPLOMA" not in course and "CERTIFICATION" in course:
            COUP_DIS = 3000
            TPURCHASE = TPURCHASE - COUP_DIS
            print(f"COUPON_DISCOUNT B4G1 {COUP_DIS:.2f}")
# If "DIPLOMA" and "CERTIFICATION" are not selected and "DEGREE" is selected by the user, then the discount will be 5000 (cost of "DEGREE" course)
        elif "DIPLOMA" not in course and "CERTIFICATION" not in course and "DEGREE" in course:
            COUP_DIS = 5000
            TPURCHASE = TPURCHASE - COUP_DIS
            print(f"COUPON_DISCOUNT B4G1 {COUP_DIS:.2f}")
            
# If the coupon provided by the user is DEAL_G20 and Programme values is equal to greater than 10000, the a discount of 20% will be applied
    elif 'DEAL_G20' in COUPON and TPURCHASE >= 10000:
        COUP_DIS = TPURCHASE * 0.2
        TPURCHASE = TPURCHASE - COUP_DIS
        print(f"COUPON_DISCOUNT DEAL_G20 {COUP_DIS:.2f}")
# If the coupon provided by the user is DEAL_G5 and number of programmes is equal to greater than 2, then a discount of 5% will be applied
    elif 'DEAL_G5' in COUPON and sum(quantity) >= 2:
        COUP_DIS = TPURCHASE * 0.05
        TPURCHASE = TPURCHASE - COUP_DIS
        print(f"COUPON_DISCOUNT DEAL_G5 {COUP_DIS:.2f}")
    else:
        print(f"COUPON_DISCOUNT NONE 0.00")

# Printing TOTAL_PRO_DISCOUNT AND PRO_MEMBERSHIP_FEE
    print(f"TOTAL_PRO_DISCOUNT {TPRO_DIS:.2f}")
    print(f"PRO_MEMBERSHIP_FEE {PRO_MEM_FEE:.2f}")

# Calculation of Total cost after ENROLLMENT_FEE    
    if TPURCHASE < 6666:
        ENROLLMENT_FEE = 500
        TPURCHASE = TPURCHASE + ENROLLMENT_FEE
        print(f"ENROLLMENT_FEE {ENROLLMENT_FEE:.2f}")
    else:
        print(f"ENROLLMENT_FEE {ENROLLMENT_FEE:.2f}")

# Total Cost of the programme to be paid by the user
    print(f"TOTAL {TPURCHASE:.2f}")

    
if __name__ == "__main__":
    main()
    