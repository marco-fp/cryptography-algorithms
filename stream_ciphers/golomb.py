def golomb(n)
    '''
        Checks if secuence meets Golomb's 3 postulates:
            1. Number of 0s and number of 1s is as near as possible to n/2, where n is secuence's length.
            2. The number of runs of given length should halve when the length is increased by one.
            3. The out-of-phase correlation should be constant, independent of the shift.
    '''
    secuence = str(n)
    n0 = secuence.count('0')
    n1 = secuence.count('1')

    if abs(n0 - n1) > 1:
        return False # Does not meet postulate 1.

    secuence_length = len(secuence)

    # Shift secuence until first and last element are different.
    while secuence[0] == secuence[secuence_length - 1]:
        if i > len(secuence):
            return False # Does not meet postulate 2.
        secuence = secuence[1:] + secuence[0]
        i += 1

    secuence += secuence[0] # Add 0 or 1 to the end, to count last run.

    runs = {}
    run_length = 1

    for i in xrange(0, secuence_length - 1):
        if(secuence[i] == secuence[i + 1]):
            run_length += 1
        else:
            if run_length in runs:
                runs[run_length].append(i)
            else:
                runs[run_length] = [i]

            run_length = 1

    if not runs:
        return False # Does not meet postulate 2.

    runs_keys = runs.keys()

    for i in xrange(0, len(runs_keys) - 1):
        if(abs(runs_keys[i] - runs_keys[i + 1]) != 1):
            return False # Does not meet postulate 2.

        current_run_count = len(runs[runs_keys[i]])
        next_run_count = len(runs[runs_keys[i+1]])
        if(current_run_count != 2*next_run_count):
            if(current_run_count != 1 and next_run_count != 1):
                return False # Does not meet postulate 2.

    autocorrelations = []
    autocorrelation = sum(int(a)*int(b) for a, b in zip(secuence, secuence[1:] + secuence[:1]))
    autocorrelations.append(autocorrelation)

    for i in xrange(2, secuence_length):
        shifted_secuence = secuence[i:] + secuence[:i]
        autocorrelation = sum(int(a)*int(b) for a, b in zip(secuence, shifted_secuence))
        autocorrelations.append(autocorrelation)

        if(autocorrelations[i - 1] != autocorrelations[i]):
            return False

    return True
