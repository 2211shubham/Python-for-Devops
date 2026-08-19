import shutil
import argparse
from pathlib import Path
from datetime import datetime

def archive_logs(source_dir, dest_dir):
    source = Path(source_dir)
    dest = Path(dest_dir)

    if not source.exists():
        print(f"Source {source_dir} does not exists." )
        return  

    dest.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = dest / f"logs_{timestamp}"

    shutil.make_archive(str(archive_name),'zip',str(source))

    print(f"Logs archived at path {archive_name}.zip")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Archive log files')
    parser.add_argument("--source", required= True, help="Source log directory")
    parser.add_argument("--destination", required=True, help="Add destination")
    args = parser.parse_args()

    archive_logs(args.source,args.destination)