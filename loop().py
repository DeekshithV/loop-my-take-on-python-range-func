# Code : Deekshith

class loop:
    def __init__(self, *args):
        if len(args)>3:
            raise Exception("Not more than three arguments")
        elif False in [ str(abs(ar)).isnumeric() for ar in args]:
            raise Exception("expected int not anything else")
        
        self.start = self.end = 0
        self.step = 1
        if len(args) == 1:
            self.end = args[0]
        elif len(args) == 2:
            if args[0]>args[1]:
                return
            else:
                self.start = args[0]
                self.end = args[1]
        else:
            if args[2] == 0:
                raise Exception("Must not be Zero")
            if args[0] > args[1]:
                if args[2]>1:
                    return
            if args[0] < args[1]:
                if args[2]<1:
                    return
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]
    
    def __iter__(self):
        print("__iter__")
        return self
    
    def __next__(self):
        if(self.step<0):
            if self.start <= self.end:
                raise StopIteration
        elif self.start >= self.end:
            raise StopIteration
        ret = self.start
        self.start = self.start + self.step
        return ret
