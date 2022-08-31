# coding=utf-8
import configparser
import os


class HandleInit:
    # 加载ini文件
    def load_ini(self):
        base_path = os.path.dirname(os.getcwd())
        ini_path = base_path + "/Config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(ini_path, encoding="utf-8-sig")
        return cf

    # 获取ini里面的value
    def get_value(self, section, key):
        cf = self.load_ini()
        try:
            data = cf.get(section=section, option=key)
        except Exception:
            print("没有获取到值")
            data = None
        return data


if __name__ == "__main__":
    a = HandleInit().get_value(section="server", key="host")
    print(a)
