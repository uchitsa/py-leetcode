class Spreadsheet:
    def __init__(self, rows):
        self.dat = {}

    def setCell(self, cell, val):
        self.dat[cell] = val

    def resetCell(self, cell):
        if cell in self.dat:
            del self.dat[cell]

    def getValue(self, formula):
        parts = formula[1:].split("+")
        total = 0
        for p in parts:
            if p[0].isdigit():
                total += int(p)
            else:
                total += self.dat.get(p,0)

        return total

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
