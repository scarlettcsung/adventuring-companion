from enum import Enum, auto

class ResetType(Enum):
    NONE = auto()
    SHORT = auto()
    LONG = auto()
    DAILY = auto()


class Counter:
    def __init__(self, maximum:int,
                 reset_type:ResetType = ResetType.NONE, max_type:dict = None,
                 start_full:bool = True):
        self.maximum = maximum
        self.reset_type = reset_type
        self.max_type = max_type
        self.start_full = start_full
        self.current = maximum if start_full else 0

    def plus_current(self):
        self.current = min(self.maximum,self.current + 1)

    def minus_current(self):
        self.current = max(0, self.current - 1)

    def plus_maximum(self):
        self.maximum += 1

    def minus_maximum(self):
        self.maximum = max(0, self.maximum - 1)
        self.current = min(self.current, self.maximum)

    def reset(self):
        if self.start_full:
            self.current = self.maximum
        else:
            self.current = 0




