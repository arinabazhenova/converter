import argparse
from app.converter import convert

def main():
    parser = argparse.ArgumentParser(prog="crypto-converter")
    parser.add_argument("--from", dest="from_coin", type=str, required=True)
    parser.add_argument("--to", dest="to_coin", type=str, required=True)
    parser.add_argument("--amount", type=float, default=1.0)
    args = parser.parse_args()

    result = convert(args.from_coin, args.to_coin, args.amount)
    print(f"{args.amount} {args.from_coin.upper()} = {result:.6f} {args.to_coin.upper()}")

if __name__ == "__main__":
    main()
