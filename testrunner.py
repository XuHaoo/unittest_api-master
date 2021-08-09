from reports import HTMLTestRunner
from case.exam_case.teacher_case import TeacherCase
from case.vblog_case.index import VBlogCase
from case.exam_case.meeting_case import Smzd,MeetingCase
from case.exam_case.smzd_case import Smzd,SmdCase
import unittest
import os
import time

# 创建测试套件
suite = unittest.TestSuite()

# 添加测试用例，根据添加顺序执行
# 添加单个测试用例
# suite.addTest(TeacherCase("test_001_admin_login"))

# 添加多个测试用例

suite.addTests([SmdCase("test_001_taskSystem"),
                SmdCase("test_002_taskSystem"),
                SmdCase("test_003_taskSystem"),
                SmdCase("test_004_taskSystem"),
                SmdCase("test_005_taskSystem"),
                SmdCase("test_006_taskSystem"),
                SmdCase("test_007_taskSystem"),
                SmdCase("test_008_taskSystem")
                ])

# suite.addTests([MeetingCase("test_001ConferenceInfo"),
#                 MeetingCase("test_002ConferenceInfo")])


# suite.addTests([SzmdCase("test_001_taskSystem"),
#                 TeacherCase("test_002_insert_paper"),
#                 TeacherCase("test_003_select_paper"),
#                 TeacherCase("test_004_edit_paper"),
#                 TeacherCase("test_005_delete_paper"),
#                 TeacherCase("test_006_insert_questions"),
#                 TeacherCase("test_007_select_questions"),
#                 TeacherCase("test_008_update_questions"),
#                 TeacherCase("test_009_delete_questions"),
#                 ])
# suite.addTests([StudentCase("test_001_register"),
#                 StudentCase("test_002_login"),
#                 StudentCase("test_003_user_info"),
#                 StudentCase("test_004_user_info_update"),
#                 StudentCase("test_005_log"),
#                 ])
# suite.addTests([VBlogCase("test_001_login"),
#                 VBlogCase("test_002_insert_article"),
#                 VBlogCase("test_003_select_article"),
#                 VBlogCase("test_004_update_article"),
#                 VBlogCase("test_005_detail_article"),
#                 VBlogCase("test_006_delete_article"),
#                 VBlogCase("test_007_insert_category"),
#                 VBlogCase("test_008_select_category"),
#                 VBlogCase("test_009_update_category"),
#                 VBlogCase("test_010_delete_category"),
#                 VBlogCase("test_011_batch_delete_category"),
#                 ])

# 定义测试报告的存放的路径
path = r"D:\Desktop\Testman_Study\unittest_exam_system\reports"
# 判断路径是否存在
if not os.path.exists(path):
    # 如果不存在，则创建一个
    os.makedirs(path)
else:
    pass
# 定义一个时间戳用于测试报告命名
now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
reports_path = path + "\\" + now_time + "(exam_report).html"
reports_title = u"森美周到-测试报告"
desc = u"SMZD-接口自动化测试报告"
# 二进制写
fp = open(reports_path, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=reports_title, description=desc)
# 运行
runner.run(suite)
