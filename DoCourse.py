import json
import random
import time
from datetime import datetime
import WanXue.WXAPI as WXAPI
import WanXue.WXUtil as WXUtil

COURSE_ID = 1012  # 课程ID

if __name__ == '__main__':
    now = datetime.now()
    time_stamp = int(datetime.timestamp(now) * 1000) - 3000  # 时间戳从系统获取
    f = open('.\\answer.json', 'r')  # 打开文件
    answer_json_text = f.read()  # 读文件
    f.close()  # 关闭文件
    print(answer_json_text)  # 显示读取的文件内容

    cookie = WXAPI.fileGetCookie()  # 读cookie

    answer_json = json.loads(answer_json_text)  # 解析答案json

    """按页遍历答案"""
    for em in answer_json:
        print(em)
        req_ctx = WXUtil.gen_req_ctx(em, COURSE_ID, time_stamp + random.randint(1, 10) * 1000,
                                     '2_' + str(em['em_id']))  # 生成请求参数data，且加入时间波动
        print(req_ctx)  # 显示参数内容
        rsp_ctx = WXAPI.doCourse(req_ctx, time_stamp, COURSE_ID, '2_' + str(em['em_id']), cookie)  # 发送请求
        print(rsp_ctx)
        time.sleep(0.5)  # 休息0.5秒
    print('Finished!')
