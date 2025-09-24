class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        frac = []
        if (numerator<0) != (denominator<0):
            frac.append("-")
        dvd = abs(numerator)
        dvs = abs(denominator)
        frac.append(str(dvd//dvs))
        rmnd = dvd%dvs
        if rmnd == 0:
            return "".join(frac)
        frac.append(".")
        lkp = {}
        while rmnd != 0:
            if rmnd in lkp:
                frac.insert(lkp[rmnd],"(")
                frac.append(")")
                break
            lkp[rmnd] = len(frac)
            rmnd *= 10
            frac.append(str(rmnd//dvs))
            rmnd %= dvs
        return "".join(frac)

