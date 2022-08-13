import importlib

class Reflect:
    def __init__(self, modulename:str = "", classname:str = ""):
        self.__classname = classname
        self.__modulename = modulename
        self.__cls = None

    def load_class(self):
        try:
            self.__cls = getattr(importlib.import_module(self.__modulename), self.__classname)
            return self.__cls
        except Exception as e:
            return None

    def load_object(self, *params):
        try:
            if not self.__cls:
                self.load_class()
            self.__obj = self.cls(*params)
            return self.__obj
        except Exception as e:
            print(e)
            return None

    def set_object(self, obj):
        self.__obj = obj

    @property
    def cls(self):
        return self.__cls

    @property
    def object(self):
        return self.__obj

    def list_attributes(self, filter_builtin = False):
        if filter_builtin:
            return [x for x in dir(self.__obj) if not x.startswith("__")]
        return dir(self.__obj)

    def has_attribute(self, attribute: str):
        if attribute in dir(self.__obj):
            return True
        if ("_" + self.__classname + attribute) in dir(self.__obj):
            return True
        return False

    def get_attribute(self, attribute: str):
        if attribute in dir(self.__obj):
            return getattr(self.__obj, attribute)
        elif ("_" + self.__classname + attribute) in dir(self.__obj):
            return getattr(self.__obj, "_" + self.__classname + attribute)
        return None 

    def list_public_members(self):
        return [x for x in dir(self.__obj) if not x.startswith("_")]
