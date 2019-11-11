

class RevealAccess(object):
    """Logs during access"""

    def __init__(self):
        print("In RevealAccess __init__: initializing but not setting the property")
        # self.__set_name__(temperature)

    def __set_name__(self, owner, name):
        print("In __set_name__: setting the property name the descriptor wil be assigned to, namely: " + str(name) + ". The owner will be the class that will get the property: " + str(owner))
        # Called when A.x = RevealAccess()
        # as self.__set_name__(A, 'x')
        self.name = name

    @property
    def attr(self):
        print("Returning the attribute")
        return f"_{self.name}"

    def __get__(self, obj, objtype):
        print("in __get__")
        if obj is None:
            print(f"Returning the instance {objtype}")
            return self
        print(f"Retrieving {self.name}")
        return getattr(obj, self.attr)

    def __set__(self, obj, val):
        print(f"Updating {self.name}")
        setattr(obj, self.attr, val)

    def __call__(self):
        print("__call_ The __call__ method of an object only comes into play when the object is invoked like a function:")
