import argparse

def check_disk(args):
    print(f"Checking disk usage for path: {args.path}")

def check_memory(args):
    print("Checking memory usage")


def main():
    parser = argparse.ArgumentParser(
        prog="syscheck",
        description="Check system status and report.",
    )

    subs = parser.add_subparsers(
        required=True,
        dest="command",
        title="commands",
    )

    disk = subs.add_parser("disk", help="Check disk usage")
    disk.add_argument("--path", default="/", help="Path to check disk usage (default: /)")
    disk.set_defaults(func=check_disk)

    mem = subs.add_parser("memory", help="Check memory usage")
    mem.set_defaults(func=check_memory)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()