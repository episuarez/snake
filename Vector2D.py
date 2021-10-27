class Vector2D:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __iter__(self):
        yield self.x;
        yield self.y;

    def __eq__(self, object) -> bool:
        return self.x == object.x and self.y == object.y;

    def __repr__(self):
        return str(self.__dict__);
