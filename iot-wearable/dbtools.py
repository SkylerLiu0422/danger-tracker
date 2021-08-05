import pymysql

from wearable_entity import WearableDevice


def get_database(host="34.146.240.199", user="iot", password="WilsonZ@", database='iot'):
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        charset="utf8"
    )


def get_device(db, uid):
    cursor = db.cursor()

    sql = "SELECT * FROM device WHERE uid=%s"
    cursor.execute(sql, uid)
    res = cursor.fetchone()
    device = WearableDevice(res[2], res[3], [4])

    cursor.close()
    return device


def write_indicator(db, device):
    cursor = db.cursor()
    status = True

    sql = """
    INSERT INTO body_indicators(uid, time, heart_rate, blood_oxygen_levels, heart_status, oxygen_status, body_status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(
            sql, [device.uid, device.time, device.heart_rate, device.blood_oxygen_levels,
                  device.heart_status, device.oxygen_status, device.body_status]
        )
        db.commit()
    except pymysql.Error as e:
        db.rollback()
        print(e)
        status = False

    cursor.close()
    return status
