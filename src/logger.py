class Logger:
    def __init__(self, stream, te):

        self.stream = stream
        self.te = te
    
    def flush(self):
        self.stream.flush()
        self.te.flush()

    def write(self, data):

        self.stream.write(data)
        self.stream.flush()
        self.te.write(data)

        
        
