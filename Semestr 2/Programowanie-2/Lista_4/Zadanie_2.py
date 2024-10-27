import sys
import Zadanie_1


n = 1000
beta = 1.34
sigma = 0.19
gamma = 0.34
s0, e0, i0, r0 = n - 1, 1, 0, 0

for i in range(1, len(sys.argv) - 1):
    if sys.argv[i].lower() == '-beta':
        beta = float(sys.argv[i + 1])
    elif sys.argv[i].lower() == '-sigma':
        sigma = float(sys.argv[i + 1])
    elif sys.argv[i].lower() == '-gamma':
        gamma = float(sys.argv[i + 1])
    elif sys.argv[i].upper() == '-N':
        n = int(sys.argv[i + 1])
    elif sys.argv[i].upper() == '-S0':
        s0 = int(sys.argv[i + 1])
    elif sys.argv[i].upper() == '-E0':
        e0 = int(sys.argv[i + 1])
    elif sys.argv[i].upper() == '-I0':
        i0 = int(sys.argv[i + 1])
    elif sys.argv[i].upper() == '-R0':
        r0 = int(sys.argv[i + 1])

if n != s0 + e0 + i0 + r0:
    raise ValueError

if '-beta' in sys.argv:
    if '-sigma' in sys.argv:
        if '-gamma' in sys.argv:
            # Dane beta, sigma, gamma
            pass
        # Dane beta, sigma
        gamma = beta - 5*sigma
    elif '-gamma' in sys.argv:
        # Dane beta, gamma
        sigma = (beta - gamma)/5
    # Dana beta
    sigma = beta/7
    gamma = beta - 5*sigma
elif '-sigma' in sys.argv:
    if '-gamma' in sys.argv:
        # Dane sigma, gamma
        beta = gamma + 5*sigma
    # Dana sigma
    beta = 7 * sigma
    gamma = 2 * sigma
elif '-gamma' in sys.argv:
    # Dana gamma
    sigma = 0.5*gamma
    beta = 5*sigma + gamma

if '-N' in sys.argv:
    if '-s0' in sys.argv:
        if '-e0' in sys.argv:
            if '-i0' in sys.argv:
                if '-r0' in sys.argv:
                    # Dane N, s0, e0, i0, r0
                    pass
                # Dane N, s0, e0, i0
                r0 = n - s0 - e0 - i0
            elif '-r0' in sys.argv:
                # Dane N, s0, e0, r0
                i0 = n - s0 - e0 - r0
            # Dane N, s0, e0
            i0 = n - s0 - e0
        elif '-i0' in sys.argv:
            if '-r0' in sys.argv:
                # Dane N, s0, i0, r0
                e0 = n - s0 - i0 - r0
            # Dane N, s0, i0
            e0 = n - s0 - i0 - r0
            r0 = 0
        elif '-r0' in sys.argv:
            # Dane N, s0, r0
            e0 = n - s0 - r0
            i0 = 0
        # Dane N, s0
        e0 = n - s0
        i0 = 0
        r0 = 0
    elif '-e0' in sys.argv:
        if '-i0' in sys.argv:
            if '-r0' in sys.argv:
                # Dane N, e0, i0, r0
                s0 = n - e0 - i0 - r0
            # Dane N, e0, i0
            s0 = n - e0 - i0
            r0 = 0
        elif '-r0' in sys.argv:
            # Dane N, e0, r0
            s0 = n - e0 - r0
            i0 = 0
        # Dane N, e0
        s0 = n - e0
        i0 = 0
        r0 = 0
    elif '-i0' in sys.argv:
        if '-r0' in sys.argv:
            # Dane N, i0, r0
            e0 = i0 + r0 + 1
            s0 = n - e0 - i0 - r0
        # Dane N, i0
        r0 = i0
        e0 = i0 + r0 + 1
        s0 = n - e0 - i0 - r0
    elif '-r0' in sys.argv:
        # Dane N, r0
        i0 = r0
        e0 = i0 + r0 + 1
        s0 = n - e0 - i0 - r0
    # Dane N
    e0 = 1
    i0 = 0
    r0 = 0
    s0 = n - e0
elif '-s0' in sys.argv:
    if '-e0' in sys.argv:
        if '-i0' in sys.argv:
            if '-r0' in sys.argv:
                # Dane s0, e0, i0, r0
                n = s0 + e0 + i0 + r0
            # Dane s0, e0, i0
            r0 = 0
            n = s0 + e0 + i0
        elif '-r0' in sys.argv:
            # Dane s0, e0, r0
            i0 = 0
            n = s0 + e0 + r0
        # Dane s0, e0
        i0 = 0
        r0 = 0
        n = s0 + e0
    elif '-i0' in sys.argv:
        if '-r0' in sys.argv:
            # Dane s0, i0, r0
            e0 = i0 + r0 + 1
            n = s0 + e0 + i0 + r0
        # Dane s0, i0
        r0 = i0
        e0 = i0 + r0 + 1
        n = s0 + e0 + i0 + r0
    elif '-r0' in sys.argv:
        # Dane s0, r0
        i0 = r0
        e0 = i0 + r0 + 1
        n = s0 + e0 + i0 + r0
    # Dane s0
    n = s0 + 1
    e0 = 1
    i0 = 0
    r0 = 0
elif '-e0' in sys.argv:
    if '-i0' in sys.argv:
        if '-r0' in sys.argv:
            # Dane e0, i0, r0
            n = 1000 * (e0 + i0 + r0)
            s0 = n - e0 - i0 - r0
        # Dane e0, i0
        r0 = i0
        n = 1000 * (e0 + i0 + r0)
        s0 = n - e0 - i0 - r0
    elif '-r0' in sys.argv:
        # Dane e0, r0
        i0 = r0
        n = 1000 * (e0 + i0 + r0)
        s0 = n - e0 - i0 - r0
    # Dane e0
    i0 = 0
    r0 = 0
    n = 1000*e0
    s0 = n - e0
elif '-r0' in sys.argv:
    if '-i0' in sys.argv:
        # Dane i0, r0
        e0 = i0 + r0 + 1
        n = 1000 * (e0 + i0 + r0)
        s0 = n - e0 - i0 - r0
    # Dane r0
    i0 = r0
    e0 = i0 + r0 + 1
    n = 1000 * (e0 + i0 + r0)
    s0 = n - e0 - i0 - r0
elif '-i0' in sys.argv:
    # Dane i0
    r0 = i0
    e0 = i0 + r0 + 1
    n = 1000 * (e0 + i0 + r0)
    s0 = n - e0 - i0 - r0


x_poczatkowe = s0, e0, i0, r0
args = beta, sigma, gamma

Zadanie_1.SEIR_plot(0, 365, 366, x_poczatkowe, args)
