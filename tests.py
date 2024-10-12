from characters import *


def copycat():
    cc = Copycat()
    decisions = []
    assert cc.make_decision(decisions)
    decisions.append(False)
    assert not cc.make_decision(decisions)
    decisions.append(True)
    assert cc.make_decision(decisions)


def grudger():
    gd = Grudger()
    decisions = []
    assert gd.make_decision(decisions)
    decisions.append(False)
    assert not gd.make_decision(decisions)
    decisions.append(True)
    assert not gd.make_decision(decisions)


def detective():
    dt = Detective()
    decisions = []
    assert dt.make_decision(decisions)
    decisions.append(True)
    assert not dt.make_decision(decisions)
    decisions.append(True)
    assert dt.make_decision(decisions)
    decisions.append(True)
    assert dt.make_decision(decisions)
    decisions.append(True)
    assert not dt.make_decision(decisions)


def detective_2():
    dt = Detective()
    decisions = []
    assert dt.make_decision(decisions)
    decisions.append(True)
    assert not dt.make_decision(decisions)
    decisions.append(True)
    assert dt.make_decision(decisions)
    decisions.append(False)
    assert not dt.make_decision(decisions)
    decisions.append(True)
    assert dt.make_decision(decisions)


def upside_down():
    ud = UpsideDown()
    decisions = []
    assert ud.make_decision(decisions)
    decisions.append(True)
    assert ud.make_decision(decisions) == (not decisions)
    decisions.append(False)
    assert ud.make_decision(decisions) == (not decisions)
    decisions.append(True)
    assert ud.make_decision(decisions) == (not decisions)


def careful():
    cr = Careful()
    decisions = []
    assert cr.make_decision(decisions)
    decisions.append(True)
    assert cr.make_decision(decisions)
    decisions.append(True)
    assert cr.make_decision(decisions)
    decisions.append(True)
    assert cr.make_decision(decisions)
    decisions.append(False)
    assert not cr.make_decision(decisions)


if __name__ == "__main__":
    copycat()
    grudger()
    detective()
    detective_2()
    upside_down()
    careful()
    print("Everything passed")

    
