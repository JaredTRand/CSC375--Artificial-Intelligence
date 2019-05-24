class Square:

    def __init__(self, left, top, width, height, name='square'):
        self.name = name
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.type = 'blank'  # blank, empty, bomb?, one, two, three, four, five?
        self.likelihood = 0
        self.flagged = False


        self.surroundings = [[None, None, None, None, None, None, None, None]]
        self.added = []
                        # Topleft, Top, Topright, Left, Right, Bottomleft, Bottom, Bottomright
                        #    0      1       2       3     4        5          6         7
