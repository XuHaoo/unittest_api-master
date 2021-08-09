import time
import unittest
import requests
from case.exam_case import host
from case.exam_case.smzd_case import Smzd


class MeetingCase(unittest.TestCase):

    def test_001ConferenceInfo(self):
        """保存会议-新增线下会议，并查询新增会议信息"""
        url = host + '/api/v1/Conference/SaveConferenceInfo'
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Token': Smzd.token,
                   'ClientType': '1',
                   'Accept': 'application/json, text/plain, */*',
                   'Connection': 'keep-alive',
                   'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/92.0.4515.107 Safari/537.36',
                   }
        paylad = {'Date': '2021-07-30',
                  'address': '哒哒哒哒哒',
                  'category': 3,
                  'conferenceName': '测试会议' + Smzd.token,
                  'conferenceType': 0,
                  'endTime': '2021-07-30 17:00',
                  'introduction': "11111",
                  'liveUrl': '',
                  'project': '豪森笔',
                  'projectID': 7,
                  'startTime': '2021-07-30 14:00'
                  }
        result = requests.post(url, headers=headers, json=paylad)
        result = result.json()
        print(result)
        ss = result['Data']
        print("新增会议ID", ss)
        # return ss

        """查询新增会议信息"""
        url = host + '/api/v1/Conference/ConferenceInfo'
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Token': Smzd.token,
            'ClientType': '1',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }

        paylad = {'id':ss}
        result = requests.post(url, headers=headers, json=paylad)
        result = result.json()
        print('查询新增会议信息', result)
       # return result
        # act = result_json["DetailedMessage"]

    # exp = "成功"
    # 注册成功，返回结果中message==成功
    # self.assertEqual(act, exp)

    def test_002ConferenceInfo(self):
        """修改会议信息"""
        url = host + '/api/v1/Conference/UpdateConferenceInfo'
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Token': Smzd.token,
            'ClientType': '1',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'ClientId': 'fe522376-313c-40c7-8f17-886a1bf33c62',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        # now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        # real_name = "修改会议名称" + now_time
        paylad = {
            'id': 1,
            'Date': '2021-07-30',
            'address': '哒哒哒哒哒',
            'category': 3,
            'conferenceName': '测试会议修改',
            'conferenceType': 0,
            'endTime': '2021-07-30 17:00',
            'introduction': "11111",
            'liveUrl': '',
            'project': '豪森笔',
            'projectID': 7,
            'startTime': '2021-07-30 14:00'
        }
        print(paylad)
        result = requests.post(url, headers=headers, json=paylad)
        result = result.json()
        print('修改会议后的参数', result)
        return result


if __name__ == '__main__':
    unittest.main()
