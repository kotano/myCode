from math import gcd


def make_rational(numer, denom):
    normalization = (numer // gcd(numer, denom), denom // gcd(numer, denom))
    res = {
        'original_numer': numer,
        'original_denom': denom,
        'numer': normalization[0],
        'denom': normalization[1]
    }
    return res


def get_numer(rational):
    return rational['numer']


def get_denom(rational):
    return rational['denom']


def add(rat1, rat2):
    numer = get_numer(rat1)*get_denom(rat2) + get_numer(rat2)*get_denom(rat1)
    denom = get_denom(rat1) * get_denom(rat2)
    res = make_rational(numer, denom)
    return make_rational(get_numer(res), get_denom(res))


def sub(rat1, rat2):
    numer = get_numer(rat1)*get_denom(rat2) - get_numer(rat2)*get_denom(rat1)
    denom = get_denom(rat1) * get_denom(rat2)
    res = make_rational(numer, denom)
    return make_rational(get_numer(res), get_denom(res))


def rat_to_string(rational):
    return '{}/{}'.format(get_numer(rational), get_denom(rational))


# #
# BEGIN
def m_make_rational(numer, denom):
    gcd_ = gcd(numer, denom)
    return {
        "numer": int(numer / gcd_),
        "denom": int(denom / gcd_),
    }


def m_get_numer(rational):
    return rational["numer"]


def m_get_denom(rational):
    return rational["denom"]


def m_add(rational1, rational2):
    numer1 = get_numer(rational1)
    denom1 = get_denom(rational1)
    numer2 = get_numer(rational2)
    denom2 = get_denom(rational2)

    return make_rational(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2,
    )


def m_sub(rational1, rational2):
    numer1 = get_numer(rational1)
    denom1 = get_denom(rational1)
    numer2 = get_numer(rational2)
    denom2 = get_denom(rational2)

    return make_rational(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2,
    )
# END


def test_rational():
    rat1 = make_rational(3, 9)
    print(get_numer(rat1) == 1)
    print(get_denom(rat1) == 3)

    rat2 = make_rational(10, 3)
    print(add(rat1, rat2) == make_rational(11, 3))
    print(sub(rat1, rat2) == make_rational(-3, 1))

    rat3 = make_rational(-4, 16)
    print(get_numer(rat3) == -1)
    print(get_denom(rat3) == 4)

    rat4 = make_rational(12, 5)
    print(add(rat3, rat4) == make_rational(43, 20))
    print(sub(rat3, rat4) == make_rational(-53, 20))

    print(rat_to_string(rat1) == "1/3")
    print(rat_to_string(rat3) == "-1/4")


if __name__ == "__main__":
    test_rational()
