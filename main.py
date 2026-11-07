import config
import subprocess
import sys

print(subprocess.run([sys.executable, 'config.py']))


def main():
    settings = f"SITE_LAT={config.SITE_LAT}, SITE_LON={config.SITE_LON}, HEAT_THRESHOLD={config.HEAT_THRESHOLD}, LOG_LEVEL={config.LOG_LEVEL}"
    return print(settings)


if __name__ == "__main__":
    main()