from scipy.stats import norm
import time
import math

# global function for time in year
days_year = 356 # or can use 242 for trading days
time_year = days_year * 24 * 60 * 60
time_year = float(time_year)

# function returns time to expire in years
def get_TUE(time_close):
    time_until_expires = time_close - time.time()/time_year
    return time_until_expires

# function returns call and put option values
def option_value(P0, X, TUE, sigma, KRF, isCall):
    # P0: stock price == market price == underlying price
    # X: exercise price
    # KRF: risk free rate (0.0? or .03?)
    # sigma: annualized volatility
    # TUE: time until expiration
    # isCall: true returns call option, false returns put option

    e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353
    D1 = (math.log(P0/X, e) + (KRF + 0.5 * math.pow(sigma, 2.0)) * TUE) / (sigma * (math.pow(TUE,0.5)))
    D2 = D1 - (sigma * math.sqrt(TUE))
    ND1 = norm.cdf(D1)
    ND2 = norm.cdf(D2)

    VC = P0 * ND1 - (X * ND2) / (math.pow(e, KRF * TUE))

    if isCall:
        return VC
    else:
        VP = VC + X / (math.pow(e, KRF * TUE)) - P0
        return VP

if __name__ == "__main__":
    print(option_value(62.0, 60.0, 40.0/365, 0.32, 0.04, True))
    print(option_value(62.0, 60.0, 40.0 / 365, 0.32, 0.04, False))
    print(option_value(40.0, 45.0, 4.0/12, 0.4, 0.03, True))