import pymysql


def get_database(host="34.146.240.199", user="iot", password="WilsonZ@", database='iot'):
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        charset="utf8"
    )


def exist_user(db, username):
    cursor = db.cursor()

    sql = "SELECT COUNT(*) FROM device WHERE username=%s"
    cursor.execute(sql, username)
    res = cursor.fetchone()

    cursor.close()
    return bool(res[0])


def verify_user(db, username, password):
    cursor = db.cursor()

    sql = "SELECT * FROM device WHERE username=%s AND password=%s"
    cursor.execute(sql, [username, password])
    res = cursor.fetchone()
    user = {
        "username": res[0],
        "uid": res[2],
        "age": res[3],
        "gender": res[4]
    }

    cursor.close()
    return user


def get_indicators_by_uid(db, uid):
    cursor = db.cursor()

    sql = "SELECT * FROM body_indicators WHERE uid=%s ORDER BY record_id DESC"
    cursor.execute(sql, uid)
    res = cursor.fetchall()

    indicators = []
    for item in res:
        indicators.append({
            "time": item[2],
            "heart_rate": item[3],
            "blood_oxygen_levels": item[4],
            "heart_status": item[5],
            "oxygen_status": item[6],
            "body_status": item[7]
        })

    cursor.close()
    return indicators
