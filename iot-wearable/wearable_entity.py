import uuid
import time
import numpy as np
import random

from wearable_tools import check_indicator

heart_rate_range = [i for i in range(88, 95)] + [i for i in np.arange(95, 100.1, 0.1)]


class WearableDevice:
    def __init__(self, uid=uuid.uuid1(), age=random.randint(18, 80), gender=random.choice(["male", "female"])):
        self.uid = uid
        self.age = age
        self.gender = gender
        self.time = None
        self.heart_rate = None
        self.blood_oxygen_levels = None
        self.heart_status = None
        self.oxygen_status = None
        self.body_status = None
        self.refresh()

    def refresh(self, stable=True):
        self.time = time.localtime()
        if stable:
            self.heart_rate = random.randint(54, 82)
            self.blood_oxygen_levels = random.uniform(98, 100)
        else:
            self.heart_rate = random.randint(48, 85)
            self.blood_oxygen_levels = random.choice(heart_rate_range)
        self.check()

    def check(self):
        self.heart_status, self.oxygen_status = check_indicator(
            self.age,
            self.gender,
            self.heart_rate,
            self.blood_oxygen_levels
        )
        if self.heart_status in ["poor", "danger"] or self.oxygen_status == "danger":
            self.body_status = "danger"
        elif self.heart_status == "below average" or self.oxygen_status == "concerning":
            self.body_status = "attention"
        else:
            self.body_status = "normal"
