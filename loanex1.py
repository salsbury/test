#Program to print out payment schedule
#for a loan with amount, interest, and years as inputted by the user
#prints out the month, the monthly payment, and the remaining amount
#
#Sally Li, ECS 10, Spring 2014


def loan():
	#will attempt to see if the inputs are actually numbers
    try:
        ar = float(input("What is the annual interest rate (enter it without the % sign)?"))
        PV = float(input("How much is being borrowed (no commas)?"))
        yr = int(input("How many years is the loan for?"))
    except:
        print("You must enter numbers for all inputs!")
        return

    #converting inputs into units we want
    #interest rate now as decimals and for monthly rate
    r = (((ar)/100)/12.0)
    #calculating number of months
    mon = yr*12

    #setting a counter for total interest, remaining
    total=0
    RP = 5000.00

    print("Payment schedule for a loan of $%0.2f at %3.1f%% interest, repaid over %d years:" %(PV,ar,yr))
    print("month payment principle interest total int remaining")

    #looping over every month
    for m in range(1,mon+1):
        #finding the monthly payment
        P = ((r)*PV)/(1-((1+r)**(-mon)))
	#finding the interest payment
        interest = RP * r
	#adding up the total by counting up interest with each loop
        total = total + round(interest,2)
	#finding the remaining payment
        RP = (PV*(1-((1+(r))**(m-mon))))/(1 - (1+r)**(-mon))
        #finding the principal
        prin = P - interest
        print(" %3d %7.2f %7.2f %7.2f %7.2f %9.2f" % (m,P, prin ,interest, total, RP))


loan()
