

class KeepTrackOfAllMyThings:
    runnum = 0
    runs = 500
    dirt_count = [0]*runs
    cleaned_count = [0]*runs
    moved_forward_count = [0]*runs

    def dirtcountadd(self, amount):
        self.dirt_count[self.runnum-1] = amount

    def cleanedcountadd(self):
        self.cleaned_count[self.runnum-1] += 1

    def movedforwardcountadd(self):
        self.moved_forward_count[self.runnum-1] += 1

    def totals(self):
        length = len(self.dirt_count)
        dirts = 0
        cleans = 0
        moves = 0
        for x in range(0, length):
            dirts += self.dirt_count[x]
            cleans += self.cleaned_count[x]
            moves += self.moved_forward_count[x]
        return dirts, cleans, moves

    def show(self):
        print('\n\n'
              '////////////////////////////\n'
              '//// Agent Stats Round {} ///\n'
              '////////////////////////////\n'
              '/// Spaces Dirty:   {} ///\n'
              '/// Spaces Cleaned: {} ///\n'
              '/// Spaces Moved:   {} ///\n'
              '////////////////////////////\n\n'
              ''.format(self.runnum, self.dirt_count[self.runnum-1], self.cleaned_count[self.runnum-1], self.moved_forward_count[self.runnum-1]))



simple_stats = KeepTrackOfAllMyThings()
random_stats = KeepTrackOfAllMyThings()   ###To keep track of all the stats for each agent
table_stats = KeepTrackOfAllMyThings()


