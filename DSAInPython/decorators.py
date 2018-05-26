def bold(fn):
    def karbold(*args):
        return "<b>" + fn(*args) + "</b>"
    return karbold


def italic(fn):
    def karitalic(*args):
        return "<i>" + fn(*args) + "</i>"
    return karitalic


@bold
@italic
def html(string):
    return string


print(html("Jackpot,Lag gya"))
