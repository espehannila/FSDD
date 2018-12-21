
class DbObject:
    
    _id         = None
    conn        = None

    def __init__(self, conn=None):
        self.conn        = conn