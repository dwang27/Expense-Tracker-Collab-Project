import time
from datetime import datetime
from zoneinfo import ZoneInfo
while True:
    print(time.time())
    time.sleep(1)
    print(time.localtime())
    print(time.gmtime())
    print(datetime.now(ZoneInfo("Australia/Sydney")))
    print(time.perf_counter())
    print(time.process_time())
    print(time.monotonic())