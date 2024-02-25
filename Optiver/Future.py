# -*- coding = utf-8 -*-
# @Time : 10/20/2023 10:49 PM
# @Author : Lauren
# @File : Future.py
# @Software : PyCharm
from dataclasses import dataclass
import bisect


@dataclass
class Dividend:
    amount: int
    days: int


class FuturePricingEngine:
    def __init__(self, stock_price: int, dividends: list[Dividend]):

    def update_dividend(self, dividend_id: int, updated_dividend: Dividend):

    def calculate_future_price(self, days_to_future: int) -> int:
