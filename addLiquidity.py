# fork and modify from https://github.com/Jeiwan/uniswapv3-code/blob/main/unimath.py
import math

min_tick = -887272
max_tick = 887272

q96 = 2**96
eth = 10**18


def price_to_tick(p):
    return math.floor(math.log(p, 1.0001))


def price_to_sqrtp(p):
    return int(math.sqrt(p) * q96)


def sqrtp_to_price(sqrtp):
    return (sqrtp / q96) ** 2


def tick_to_sqrtp(t):
    return int((1.0001 ** (t / 2)) * q96)


def liquidity0(amount, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return (amount * (pa * pb) / q96) / (pb - pa)


def liquidity1(amount, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return amount * q96 / (pb - pa)


def calc_amount0(liq, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return int(liq * q96 * (pb - pa) / pb / pa)


def calc_amount1(liq, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return int(liq * (pb - pa) / q96)


# Liquidity provision
price_low = 1000.302
price_cur = 2645.75
price_upp = 2998.9045

print(f"Price range: {price_low} - {price_upp}; current price: {price_cur} \n")

sqrtp_low = price_to_sqrtp(price_low)
sqrtp_cur = price_to_sqrtp(price_cur)
sqrtp_upp = price_to_sqrtp(price_upp)

amount_eth = 1 * eth
amount_usdt = 5000 * eth

liq0 = liquidity0(amount_eth, sqrtp_cur, sqrtp_upp)
liq1 = liquidity1(amount_usdt, sqrtp_cur, sqrtp_low)
print(f"Liquidity \n L1: {liq0}, L2: {liq1} \n")
liq = int(min(liq0, liq1))

print(f"Deposit: {amount_eth/eth} ETH, {amount_usdt/eth} USDT; liquidity: {liq} \n")
amount0 = calc_amount0(liq, sqrtp_upp, sqrtp_cur)
amount1 = calc_amount1(liq, sqrtp_low, sqrtp_cur)
print(f"Real deposit amount: \n ETH amount: {amount0/eth}, USDT amount: {amount1/eth} \n")


badLiq = int(max(liq0, liq1))
badAmount0 = calc_amount0(badLiq, sqrtp_upp, sqrtp_cur)
badAmount1 = calc_amount1(badLiq, sqrtp_low, sqrtp_cur)
print(f"Using bigger L requirement: \n ETH amount: {badAmount0/eth}, USDT amount: {badAmount1/eth}")
