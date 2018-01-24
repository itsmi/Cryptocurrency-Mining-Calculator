# Cryptocurrency-Mining-Calculator
Computes optimized reinvestment rates for maximum return on investment for providers, auch as Genesis and Hashflare mining.

The Python script optimizes the reinvest strategy for a maximum return on investment based on a given timeframe or end date. The optimizer used is the limited-memory Broyden–Fletcher–Goldfarb–Shanno algorithm (L-BFGS-B).

Inputs:
* init_invest: The initial investment in USD.
* init_hashpwr_price: THe initial hashpower price in USD / GH/s.
* invest_dur: The time period for the investment.
* hashpwr_dur: The duration of the hashpower in days.
* BTC_price: The current (bit)coin price in USD
* BTC_return: The return in (bit)coin per day and GH/s
* eff_red: The relative change in efficiency per year. 0: no change; 1: complete shutdown
* hashpwr_price_red: The relative change in cost of hashpower per year. 0: no change; 1: free

Conclusions:
* It is best to reinvest everything up to a certain point and then stop reinvesting.
* The time to stop is not necessarily one year before the optimized period. This means that hashpower may be left past the time period optimized for, further increasing the return on investment.

Feel free to contribute and let me know of any bugs or errors in the code. Thank you!


