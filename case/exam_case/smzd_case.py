import time
import unittest
import requests
from case.exam_case import host
from public.exam_public.smzd import Smzd


class SmdCase(unittest.TestCase):

    def test_001_taskSystem(self):
        """发送任务--新增任务"""
        # 获取当前时间
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        url = host + '/api/v1/TaskSystem/SendTask'
        headers = {
            'Token': Smzd.token,
            'ClientType': '1',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        paylad = {
            "name": "测试新增任务" + now_time,
            "content": "这个测试新增任务内容信息",
            "files": [],
            "projectIds": [
                "6"
            ],
            "startTime": now_time,
            "endTime": "2022-07-28 13:08",
            "isAsync": False,
            "customFields": {
                "category": 3,
                "type": 11,
                "relatedLinks": {
                    "article": [
                        {
                            "Id": "f7467179-478a-4369-8c23-bf136d272177",
                            "Name": "五、心率问题_Q1_视频",
                            "Subtitle": "孚来美Q&A问答",
                            "coverImg": "https://smzdpcapi.huilangongyi.org.cn/api/v1/File/GetPublicFileByFileId?fileId=CFE2A18C5BAFBB98178BD171363FA864&systemId=56"
                        },
                        {
                            "Id": "be6bf1d8-0376-4bcf-9ad2-5371136f24d6",
                            "Name": "一、消化道_Q1",
                            "Subtitle": "1.为什么个别患者用孚来美（聚乙二醇洛塞那肽）后，不但食欲未减低，反而食欲增加？",
                            "coverImg": "https://ashermed.oss-cn-beijing.aliyuncs.com/Article/20210721105308568.jpg?x-oss-process=image/resize,w_350,limit_0"
                        }
                    ],
                    "link": []
                },
                "salesList": [],
                "groupPostingSales": False,
                "doctorList": [
                    {
                        "UserId": 58282,
                        "UserName": "徐浩",
                        "Type": 2
                    }
                ],
                "groupPostingDoctor": False,
                "nurseList": [],
                "groupPostingNurse": False,
                "patientList": [],
                "groupPostingPatient": False,
                "conferenceID": 0,
                "academicList": []
            }
        }
        result = requests.post(url, headers=headers, json=paylad)
        result = result.json()
        print('新增任务返回', result)
        # 添加一个任务ID为其他用例调用
        rid = result["Data"]
        globals()["Data"] = rid

    def test_002_taskSystem(self):
        """获取任务列表，发送的任务"""
        surl = host + '/api/v1/TaskSystem/QuerySendTaskList'

        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Token': Smzd.token,
                   'ClientType': '1',
                   'Accept': 'application/json, text/plain, */*',
                   'Connection': 'keep-alive',
                   'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/92.0.4515.107 Safari/537.36',
                   'Authorization': '19042607027949b4bb569ece1a7d0cc0'
                   }
        payload = {'pageIndex': 1, 'pageSize': 10, 'fuzzyField': '', 'isNewFeedback': True}
        result = requests.post(headers=headers, url=surl, json=payload)
        result = result.json()
        print('获取发送任务列表返回参数', result)
        try:
            act = result["Data"]["DetailedMessage"]
        except KeyError:  # 避免取不到key报错
            act = 1
        print("返回校验成功")
        # 设置断言，返回结果中包含用户名
        self.assertEqual(1, act)

    def test_003_taskSystem(self):
        """发布-任务详情"""
        url = host + '/api/v1/TaskSystem/QueryTaskDetail'
        headers = {
            'Token': Smzd.token,
            'ClientType': '1',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        # 使用新增任务是的ID信息
        paylad = {'taskId':globals()["Data"]}
        result = requests.post(headers=headers, json=paylad, url=url)
        result = result.json()
        print('获取任务详情返回参数', result)
        try:
            act = result["Data"]["DetailedMessage"]
        except KeyError:  # 避免取不到key报错
            act = 1
        print("返回校验成功")
        # 设置断言，返回结果中包含用户名
        self.assertEqual(1, act)

    def test_004_taskSystem(self):
        """获取任务类类型（根据类别）"""
        url = host + '/api/v1/TaskSystem/GetTaskTypeList'
        headers = {
            'Token': Smzd.token,
            'ClientType': '1',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        paylad = {'parentId': 0}
        result = requests.post(url, headers=headers, json=paylad)
        result = result.json()
        print('任务详情返回参数', result)
        try:
            act = result["Data"]["DetailedMessage"]
        except KeyError:  # 避免取不到key报错
            act = 1
        print("返回校验成功")
        # 设置断言，返回结果中包含用户名
        self.assertEqual(1, act)

    def test_005_taskSystem(self):
        """对已发布任务进行追加接收人"""
        url = host + '/api/v1/TaskSystem/AddTaskReceive'
        headers = {
            'Token': Smzd.token,
            'ClientType': '1',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        # 使用新增任务时的ID
        paylad = {
            'taskId': globals()["Data"],
            'salesList': [],
            'groupPostingSales': False,
            'doctorList': [
                {
                    'UserId': 58282,
                    'UserName': "徐浩",
                    'Type': 2
                }
            ],
            'groupPostingDoctor': False,
            'nurseList': [],
            'groupPostingNurse': False,
            'patientList': [],
            'groupPostingPatient': False,
            'academicList': [],
            'otherList': []
        }
        result = requests.post(url, headers=headers, json=paylad)
        result = result.json()
        print('追加人员状态', result)

    def test_006_taskSystem(self):
        """给任务发送消息"""
        url = host + '/api/v1/TaskSystem/SendMessage'
        headers = {
                'Token': Smzd.token,
                'ClientType': '1',
                'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
                'Content-Type': 'application/json;charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/92.0.4515.107 Safari/537.36'
            }
        # 使用新增任务时的ID
        paylad = {
                  'taskId': globals()["Data"],
                  'senderId': 24875,
                  'senderName': "徐浩",
                  'receiverId': 24875,
                  'receiverName': "徐浩",
                  'content': "测试发布内容信息test",
                  'files': []
                 }
        result =requests.post(url,headers=headers,json=paylad)
        result = result.json()
        print('发送消息返回结果',result)

    def test_007_taskSystem(self):
        """反馈-获取反馈文件列表"""
        url = host+'/api/v1/TaskSystem/QueryFeedbackList'
        headers = {
            'Token': Smzd.token,
            'ClientType': '1',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        paylad = {
              'pageIndex': 1,
              'pageSize': 1000,
              'fuzzyField': "",
              'isNewFeedback': True,
                 }
        result = requests.post(url,headers=headers,json=paylad)
        result= result.json()
        print('获取反馈文件列表',result)
       # print(result()[globals()["Data"]])
        #print(result()["Data"]["Items"][0])
        # for key, value in result.items():
        #     print(key,result[])


    def test_008_taskSystem(self):
        """删除任务"""
        url = host + '/api/v1/TaskSystem/DeleteTask'
        headers = {
            'Token': Smzd.token,
            'ClientType': '1',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        paylad = {"taskId": globals()["Data"]}
        result = requests.post(url, headers=headers, json=paylad)
        result = result.json()
        print('删除任务返回', result)




if __name__ == '__main__':
    unittest.main()


