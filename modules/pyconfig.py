import pyjson_withcommit


# 新增参数类，读取本地全局参数
class Config:
    def __init__(self, configPath: str) -> None:
        CONFIG = pyjson_withcommit.LoadJson(configPath)
        self.__appid = CONFIG['appid']
        self.__keys = CONFIG['keys']
        self.__http = CONFIG['http']
        

    @property
    def getAppid(self) -> str:
        return self.__appid

    @property
    def getKeys(self) -> str:
        return self.__keys

    @property
    def getHttp(self) -> str:
        return self.__http
