import requests
import self as self

from case.exam_case import host


def __init__(self, requests):
    self.requests = requests  # 设置全局参数


class Smzd:

    print(".......................................Login  start..................................................>")

    def Smzdlogin(self, token):
        """登录获取token等信息"""
        self.smzd_token = token
        # 调用登录接口
    url_login = host+"/api/v1/Login/SingleSignOnByLoginId"
    # 传入用户名和密码
    payload = {'loginId': '13671679931', 'clientType': 1, 'systemId': 56, 'loginPwd': '679931',
               'isExclusiveLogin': True, 'clientId': 'fe522376-313c-40c7-8f17-886a1bf33c62'}
    # 返回结果赋值给result
    result = requests.post(url_login, json=payload)
    # 将返回结果转为json格式
    result = result.json()
    print('登录返回参数',result)
    token = result["Data"]["Token"]
    # try:
    #     act = result["Data"]["Name"]
    # except KeyError:  # 避免取不到key报错
    #     act = '徐浩'
    #     print('登录成功')
    #       # 设置断言，返回结果中包含用户名
    #     self.assertEqual(act, '徐浩')
    # print('这个是登录成功的token'+token)


    # def meetingMessage(self):
    #     """新增会议"""
    #     url = host + '/api/v1/Conference/SaveConferenceInfo'
    #     headers = {'Content-Type': 'application/json;charset=UTF-8',
    #                'Token': Smzd.token,
    #                'ClientType': '1',
    #                'Accept': 'application/json, text/plain, */*',
    #                'Connection': 'keep-alive',
    #                'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
    #                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                              'Chrome/92.0.4515.107 Safari/537.36',
    #                }
    #     paylad = {'Date': '2021-07-30',
    #               'address': '哒哒哒哒哒',
    #               'category': 3,
    #               'conferenceName': '测试会议' + Smzd.token,
    #               'conferenceType': 0,
    #               'endTime': '2021-07-30 17:00',
    #               'introduction': "11111",
    #               'liveUrl': '',
    #               'project': '豪森笔',
    #               'projectID': 7,
    #               'startTime': '2021-07-30 14:00'
    #               }
    #     result = requests.post(url, headers=headers, json=paylad)
    #     result = result.json()
    #     print(result)
    #





