class Polynomial:
    def __init__(self, coeffs):
        i = 0
        while i < len(coeffs) - 1 and coeffs[i] == 0:
            i += 1
        self.coeffs = coeffs[i:]

    def __call__(self, x):
        result = 0
        deg = len(self.coeffs) - 1
        for c in self.coeffs:
            result += c * (x ** deg)
            deg -= 1
        return result

    def __add__(self, other):
        a = self.coeffs[:]
        b = other.coeffs[:]
        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        else:
            b = [0] * (len(a) - len(b)) + b
        return Polynomial([a[i] + b[i] for i in range(len(a))])

    def __str__(self):
        terms = []
        n = len(self.coeffs)
        for i, c in enumerate(self.coeffs):
            if c == 0:
                continue
            deg = n - 1 - i
            sign = "-" if c < 0 else "+"
            c_abs = abs(c)
            if deg == 0:
                term = str(c_abs)
            elif deg == 1:
                term = "x" if c_abs == 1 else f"{c_abs}x"
            else:
                term = f"x^{deg}" if c_abs == 1 else f"{c_abs}x^{deg}"
            terms.append((sign, term))
        if not terms:
            return "0"
        sign, term = terms[0]
        result = ("-" if sign == "-" else "") + term
        for sign, term in terms[1:]:
            result += f" {'+' if sign == '+' else '-'} {term}"
        return result