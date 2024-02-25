# -*- coding = utf-8 -*-
# @Time : 10/20/2023 7:49 PM
# @Author : Lauren
# @File : Worst Trade Reporter.py
# @Software : PyCharm

class PnLCalculator:
    def __init__(self):
        self.buy_search = {} # store buy decisions
        self.sell_search = {} # store sell decisions
        self.price_search = {} # store prices
        self.timeStamp = 0

    def process_trade(self, trade_id, instrument_id, buy_sell, price,
                      volume):
        self.timeStamp += 1
        if buy_sell == 'BUY':
            if instrument_id not in self.buy_search:
                self.buy_search[instrument_id] = (price, trade_id, self.timeStamp)
            else:
                # if the current buy price is larger, add it in
                if self.buy_search[instrument_id][0] <= price:
                    self.buy_search[instrument_id] = (price, trade_id, self.timeStamp)
        else:
            if instrument_id not in self.sell_search:
                self.sell_search[instrument_id] = (price, trade_id, self.timeStamp)
            else:
                # if the current sell price is lower, add it in
                if self.sell_search[instrument_id][0] >= price:
                    self.sell_search[instrument_id] = (price, trade_id, self.timeStamp)

    def process_price_update(self, instrument_id, price):
        self.price_search[instrument_id] = price

    def output_worst_trade(self, instrument_id):
        buy_loss = self.price_search[instrument_id] - self.buy_search[
                instrument_id][0] if instrument_id in self.buy_search else \
            float('inf')


        sell_loss = self.sell_search[instrument_id][0] - self.price_search[
            instrument_id] if instrument_id in self.sell_search else float(
            'inf')
        if buy_loss < 0 and sell_loss < 0:
            if buy_loss < sell_loss:
                return self.buy_search[instrument_id][1]
            elif buy_loss > sell_loss:
                return self.sell_search[instrument_id][1]
            else:
                if self.buy_search[instrument_id][2] > self.sell_search[
                    instrument_id][2]:
                    return self.sell_search[instrument_id][1]
                else:
                    return self.buy_search[instrument_id][1]
        elif buy_loss < 0:
            return self.buy_search[instrument_id][1]
        elif sell_loss < 0:
            return self.sell_search[instrument_id][1]
        else:
            return 'NO BAD TRADES'

