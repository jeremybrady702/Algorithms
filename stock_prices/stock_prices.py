#!/usr/bin/python
import argparse


def find_max_profit(prices):
    min_idx = 0
    max_idx = len(prices)-1
    for i in range(len(prices)-1):
        if prices[min_idx] > prices[i]:
            min_idx = i
    for i in range(min_idx+1, len(prices)-1):
        if prices[max_idx] < prices[i]:
            max_idx = i
    return prices[max_idx] - prices[min_idx]


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
