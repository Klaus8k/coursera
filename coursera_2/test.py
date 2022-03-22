class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.kind = kind

class EventSet:
    def __init__(self, kind):
        self.kind = kind

class NullHandler:
    def __init__(self, successor = None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            self.__successor.handle(obj, event)

class IntHandler(NullHandler):

    def handle(self, obj, event):

        try:
            if issubclass(event.kind, int):
                return obj.integer_field
        except:
            isinstance(event.kind, int)
            obj.integer_field = event.kind
            return obj.integer_field
        return super().handle(obj, event)


class FloatHandler(NullHandler):

    def handle(self, obj, event):

        if issubclass(event.kind, float):
            return obj.float_field
        elif isinstance(event.kind, float):
            obj.float_field = event.kind
        else:
            super().handle(obj, event)

class StrHandler(NullHandler):

    def handle(self, obj, event):

        if issubclass(event.kind, str):
            return obj.string_field
        elif isinstance(event.kind, str):
            obj.string_field = event.kind
        else:
            super().handle(obj, event)

if __name__ == '__main__':
    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))
    chain.handle(obj, EventSet(100))
    print(chain.handle(obj, EventGet(int)))
    chain.handle(obj, EventSet(0.5))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))
    # print(obj.float_field)