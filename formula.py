def formulate(form):
    final = ""
    '''
    A = total population
    B = 85 years and older
    C = 80 - 84 years
    D = 75-79 years
    E = 65 years and older
    F = 60 years and older
    G = 55 - 59 years
    H = 21 and over
    I = 16 and over
    J = 10 - 14 years



    '''
    keys = {
        'A':'ACS_17_5YR_S0101_HC01_EST_VC01',
        'B':'ACS_17_5YR_S0101_HC01_EST_VC20',
        'C':'ACS_17_5YR_S0101_HC01_EST_VC19',
        'D':'ACS_17_5YR_S0101_HC01_EST_VC18',
        'E':'ACS_17_5YR_S0101_HC01_EST_VC33',
        'F':'ACS_17_5YR_S0101_HC01_EST_VC31',
        'G':'ACS_17_5YR_S0101_HC01_EST_VC14',
        'H':'ACS_17_5YR_S0101_HC01_EST_VC30',
        'I':'ACS_17_5YR_S0101_HC01_EST_VC28',
        'J':'ACS_17_5YR_S0101_HC01_EST_VC05',
    }
    for char in form:
        if(keys.has_key(char)):
            final = final + keys[char]
        else:
            final = final + char

    print(final)
formulate('((G+F)-(D+C+B))/(A-(A-I-J))')
