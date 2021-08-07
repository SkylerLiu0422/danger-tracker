import base64

import json
import time

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models

upload_folder = "./uploads/"


def convert_file(filename):
    file_path = upload_folder + filename
    with open(file_path, 'rb') as f:
        base64_str = base64.b64encode(f.read())
        src = base64_str.decode('utf-8')

    return src


def start_recognition(data):
    try:
        cred = credential.Credential("AKIDtb2C5i4AzXpqa3HFl0yf5E5fy0kDPKxJ", "80bvyjDQM1PWMwFH2YnlRqzsTothDSQ7")
        http_profile = HttpProfile()
        http_profile.endpoint = "asr.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        client = asr_client.AsrClient(cred, "", client_profile)

        req = models.CreateRecTaskRequest()
        params = {
            "EngineModelType": "16k_zh_medical",
            "ChannelNum": 1,
            "ResTextFormat": 0,
            "SourceType": 1,
            "Data": data,
            "ConvertNumMode": 1
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreateRecTask(req)
        loading = True
        success = False
        while loading:
            time.sleep(1)
            req = models.DescribeTaskStatusRequest()
            params = {
                "TaskId": resp.Data.TaskId,
            }
            req.from_json_string(json.dumps(params))

            resp = client.DescribeTaskStatus(req)
            if resp.Data.Status == 2:
                loading = False
                success = True
            elif resp.Data.Status == 3:
                loading = False
        if success:
            return {
                "status": 1,
                "data": resp.Data.Result
            }
        else:
            return {
                "status": 0,
                "data": "Recognition Error!"
            }
    except TencentCloudSDKException as err:
        print(err)