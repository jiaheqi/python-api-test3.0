#coding:utf-8

import sys
from config import setting

class Env_Module():

    def __init__(self):
        pass

    def get_grpc_target(self, module):
        """
        获取grpc调用地址
        :param module:环境对应业务名称，入：sms
        :return: 返回grpc调用地址
        """
        if sys.argv.__len__()<2:
            env = 'dohko'
        else:
            env = sys.argv[1]
        env_target = setting.ENVIRONMENT_GRPC_CONFIG[env]
        return env_target[module]
