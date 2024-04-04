import aiohttp
import asyncio
import argparse

from datetime import datetime, timedelta
import json

from logger import logger
from async_util import async_timeit
from ssl_util import get_ssl


class ExchangeRateDriver:

    URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='
    BASE_CURRENCIES = ['USD', 'EUR']
    ALL_CURRENCIES = ['USD', 'EUR', 'CHF', 'GBP', 'PLZ', 'SEK', 'XAU', 'CAD']

    def __init__(self, num_days, additional_currencies):
        self.num_days = num_days
        self.currencies = self.BASE_CURRENCIES + additional_currencies

    @async_timeit
    async def _task(self, date):
        logger.debug("Fetching exchange rates for %s", date)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"{self.URL}{date}", ssl=get_ssl()) as resp:
                    if resp.ok:
                        return await resp.json()
                    else:
                        logger.error("Error for %s: %s", date, resp.status)
                        return None
            except aiohttp.ClientConnectorError as err:
                logger.error("Connection error for %s: %s", date, err)
                return None

    async def get_exchange_rates(self) -> list:
        dates = []
        for i in range(self.num_days):
            date = (datetime.now() - timedelta(days=i)).strftime("%d.%m.%Y")
            dates.append(date)

        tasks = [self._task(date) for date in dates]
        results = await asyncio.gather(*tasks)
        return [self.parse(r) for r in results]

    def parse(self, result) -> dict:
        rates = result.get("exchangeRate")
        parsed_rates = {}
        for currency in self.currencies:
            rate = next((el for el in rates if el["currency"] == currency), None)
            if rate:
                sale = rate.get('saleRate') or rate.get('saleRateNB')
                purchase = rate.get('purchaseRate') or rate.get('purchaseRateNB')
                parsed_rates[currency] = {
                    "sale": sale,
                    "purchase": purchase,
                }
        return {result['date']: parsed_rates}


class ArgumentParser:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(
            description='Fetch exchange rates (USD and EUR) for the past n days.')
        parser.add_argument('num_days', type=int, nargs='?', default=2,
                            help='Number of past days to fetch exchange rates for')
        parser.add_argument('--currencies', nargs='+', default=[],
                            help='Additional currencies to include in response')
        return parser.parse_args()


class ExchangeRateFetcher:
    def __init__(self, num_days=2, currencies=[], driver=ExchangeRateDriver):
        self.num_days = num_days
        self.currencies = currencies
        self.rates = []
        try:
            self.validate_args()
        except ValueError as err:
            logger.error(err)
            return
        self.driver = driver(self.num_days, self.currencies)

    def validate_args(self):
        if self.num_days < 1:
            raise ValueError("Number of days must be greater than 0")
        if self.num_days > 10:
            raise ValueError("Number of days must be less than 10")
        for currency in self.currencies:
            if currency in self.driver.BASE_CURRENCIES:
                self.currencies.remove(currency)
            if currency not in self.driver.ALL_CURRENCIES:
                raise ValueError(f"Invalid currency: {currency}")

    def to_strings(self):
        result = []
        for rate in self.rates:
            for date, currencies in rate.items():
                rate_str = f"Date: {date}:"
                for currency, values in currencies.items():
                    rate_str += f" {currency}: {values['sale']} / {values['purchase']}"
                result.append(rate_str)
        return result

    def to_json(self):
        return json.dumps(self.rates, indent=4)

    async def fetch(self):
        self.rates = await self.driver.get_exchange_rates()
        return self.rates


async def main():
    args = ArgumentParser.parse_args()
    fetcher = ExchangeRateFetcher(args.num_days, args.currencies)
    await fetcher.fetch()
    return fetcher.to_json()


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)
