# Cryptocurrency-Mining-Calculator

The Python script optimizes the reinvest strategy for a maximum return on investment for a given duration or end date. The optimizer used is the limited-memory Broyden–Fletcher–Goldfarb–Shanno algorithm (L-BFGS-B).

Inputs:
* init_invest: The initial investment in USD.
* init_hashpwr_price: The initial hashpower price in USD / GH/s.
* invest_dur: The time period for the investment.
* hashpwr_dur: The duration of the hashpower in days.
* BTC_price: The current (bit)coin price in USD.
* BTC_return: The return in (bit)coin per day and GH/s.
* eff_red: The relative change in efficiency per year. 0: no change; 1: complete shutdown.
* hashpwr_price_red: The relative change in cost of hashpower per year. 0: no change; 1: free.

Conclusions:
* It is best to reinvest everything up to a certain point and then stop reinvesting completely.
* The time before stopping is not necessarily one year before the optimized period. This means that hashpower may be left past the time period optimized for, further increasing the return on investment.

Feel free to contribute and let me know of any bugs or errors in the code. Thank you!

Example:
* init_invest: 550 # USD
* init_hashpwr_price: 0.22 # USD / GH/s
* invest_dur: 2 * 365 # days
* hashpwr_dur: 365 # days
* BTC_price: 11000 # USD
* BTC_return: 0.00000012 # BTC per day and GH/s
* eff_red: 0.4
* hashpwr_price_red: 0.3

![alt text](https://github.com/itsmi/Cryptocurrency-Mining-Calculator/blob/master/example/1_reinvest_vs_day.png)

![alt text](https://github.com/itsmi/Cryptocurrency-Mining-Calculator/blob/master/example/2_hashpower_vs_day.png)

![alt text](https://github.com/itsmi/Cryptocurrency-Mining-Calculator/blob/master/example/3_USD_per_day_vs_day.png)

![alt text](https://github.com/itsmi/Cryptocurrency-Mining-Calculator/blob/master/example/4_USD_accumuated_vs_day.png)


