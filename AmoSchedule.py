import pandas as pd
from tabulate import tabulate
upb = float(input("What is the Unpaid Principle Balance of your Property?: "))
term = int(input("How long is the term of your mortgage (years)?: "))
rte = float(input("What is the fixed interest rate on this property? ex (3.5% = 3.5%): "))
class property:
    def __init__(self, upb,term,rte):
        self.upb = upb
        self.term = term
        self.rte = rte
def amo(self):
    upb = self.upb
    term = self.term
    realterm = term * 12
    rte = self.rte/100/12
    monthly_payments = []
    intpay = []
    agelist = []
    month_princlist = []
    rbl = []
    rem_balance = upb
    month_princ = 0
    for i in range(0,realterm):
        mp = (upb * rte) / ((1 - 1 / (1 + rte) ** realterm))
        ip = rem_balance * rte
        month_princ = mp - ip
        rem_balance = rem_balance - month_princ
        ac = realterm - i
        agelist.append(ac)
        rbl.append(rbl)
        monthly_payments.append(mp)
        intpay.append(ip)
        month_princlist.append(month_princ)
        columns = ["Age", "Remaining_Balance", "Monthly_Payments", "Interest_Payment", "Monthly_Principal"]
        df = pd.DataFrame(list(zip(agelist, rbl, monthly_payments, intpay, month_princlist)), columns=columns)
        print(df)

propertyofinterest = property(upb,term,rte)

amo(propertyofinterest)



