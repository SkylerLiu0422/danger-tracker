import time

from sender import get_connection, send_object
import dbtools


def main():
    db = dbtools.get_database()
    device = dbtools.get_device(db, "874a30cc-f4c5-11eb-9050-e0d4645ff956")

    key = "beta"
    channel = get_connection(key)
    while True:
        if device.body_status == "danger":
            send_object(channel, key, device, priority=8)
            time.sleep(10)
        else:
            send_object(channel, key, device)
            time.sleep(300)
        device.refresh()


if __name__ == "__main__":
    main()
