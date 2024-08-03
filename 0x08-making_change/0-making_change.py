#!/usr/bin/python3
"""Coin Change"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    nb_coins = 0
    for coin in coins:
        if coin > total:
            continue
        count = total // coin
        total -= count * coin
        nb_coins += count
        if total == 0:
            return nb_coins
    return -1
