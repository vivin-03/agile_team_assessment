basic = float(input("Enter basic salary: "))

hra = 0.20 * basic
da = 0.10 * basic
gross = basic + hra + da
tax = 0.05 * gross
net = gross - tax

print("Net Salary:", net)
