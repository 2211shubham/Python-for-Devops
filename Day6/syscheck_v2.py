# syscheck_v2.py
import argparse
import psutil


def check_disk(args):
    """Check disk usage for a given path."""
    usage = psutil.disk_usage(args.path)

    total_gb = usage.total / (1024 ** 3)
    used_gb  = usage.used  / (1024 ** 3)
    free_gb  = usage.free  / (1024 ** 3)

    print(f"\n💾 DISK CHECK: {args.path}")
    print(f"  Total : {total_gb:.2f} GB")
    print(f"  Used  : {used_gb:.2f} GB ({usage.percent}%)")
    print(f"  Free  : {free_gb:.2f} GB")

    if usage.percent > 80:
        print(f"  🚨 ALERT: Disk usage is HIGH! ({usage.percent}%)")


def check_mem(args):
    """Check memory usage."""
    mem = psutil.virtual_memory()

    total_gb = mem.total     / (1024 ** 3)
    used_gb  = mem.used      / (1024 ** 3)
    avail_gb = mem.available / (1024 ** 3)

    print(f"\n🧠 MEMORY CHECK")
    print(f"  Total    : {total_gb:.2f} GB")
    print(f"  Used     : {used_gb:.2f} GB ({mem.percent}%)")
    print(f"  Available: {avail_gb:.2f} GB")

    if mem.percent > 90:
        print(f"  🚨 ALERT: Memory usage is HIGH! ({mem.percent}%)")


def check_proc(args):
    """Check top N processes by CPU or memory."""
    print(f"\n⚙️  TOP {args.count} PROCESSES (sorted by {args.sort})")
    print(f"  {'PID':>6}  {'NAME':<20}  {'CPU%':>6}  {'MEM%':>6}")
    print(f"  {'-'*6}  {'-'*20}  {'-'*6}  {'-'*6}")

    # Collect all running processes
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass   # skip processes that ended or we can't read

    # Sort by cpu or memory
    sort_key = 'cpu_percent' if args.sort == 'cpu' else 'memory_percent'
    processes.sort(key=lambda p: p[sort_key] or 0, reverse=True)

    # Print top N
    for proc in processes[:args.count]:
        print(
            f"  {proc['pid']:>6}  "
            f"{proc['name']:<20}  "
            f"{proc['cpu_percent'] or 0:>6.1f}  "
            f"{proc['memory_percent'] or 0:>6.1f}"
        )


def main():
    # ─── Main Parser ───
    parser = argparse.ArgumentParser(
        prog='syscheck',
        description='🛠️  System Health Check CLI'
    )

    subs = parser.add_subparsers(
        required=True,
        dest='command',
        title='Available Commands'
    )

    # ─── disk ───
    disk = subs.add_parser("disk", help="Check disk usage")
    disk.add_argument("--path", default="/", help="Path to check (default: /)")
    disk.set_defaults(func=check_disk)

    # ─── mem ───
    mem = subs.add_parser("mem", help="Check memory usage")
    mem.set_defaults(func=check_mem)

    # ─── proc ───
    proc = subs.add_parser("proc", help="Check running processes")
    proc.add_argument("--count", type=int, default=5,       help="Number of processes to show")
    proc.add_argument("--sort",  choices=['cpu', 'mem'],    help="Sort by cpu or mem",
                      default='cpu')
    proc.set_defaults(func=check_proc)

    # ─── Dispatch ───
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()