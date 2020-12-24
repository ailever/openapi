import sympy

def SARIMAEquation(trendparams:tuple=(0,0,0), seasonalparams:tuple=(0,0,0,1)):
    p, d, q = trendparams
    P, D, Q, m = seasonalparams

    Y_order = p + P*m + d + D*m
    e_order = q + Q*m

    # define Y, e
    Y, e = sympy.symbols('Y_t, e_t')
    Y_ = {}; e_ = {}
    Y_['t'] = Y; Y__ = [ [Y_['t']] ]
    e_['t'] = e; e__ = [ [e_['t']] ]
    for i in range(1, Y_order+1):
        Y_[f't-{i}'] = sympy.symbols(f'Y_t-{i}')
        Y__.append( [Y_[f't-{i}']] )    # Y__ = [ [Y_['t']], [Y_['t-1']], ..., [Y_['t-(p+P*m+q+Q*m)']] ]
    for i in range(1, e_order+1):   
        e_[f't-{i}'] = sympy.symbols(f'e_t-{i}')
        e__.append( [e_[f't-{i}']] )    # e__ = [ [e_['t']], [e_['t-1']], ..., [e_['t-(q+Q*m)']] ]

    # define L
    L = sympy.symbols('L')
    S_Lag = L**m
    T_Lag = L
    S_Lag_Diff = (1-L**m)**D
    T_Lag_Diff = (1-L)**d

    # define coefficients : phis(T), Phis(S), thetas(T), Thetas(S)
    T_phi = {}; T_phis = []; L_byT_phi = []
    S_phi = {}; S_phis = []; L_byS_phi = []
    T_theta = {}; T_thetas = []; L_byT_theta = []
    S_theta = {}; S_thetas = []; L_byS_theta = []

    for p_ in range(0, p+1):
        T_phi[p_] = sympy.symbols(f'phi_{p_}')
        T_phis.append(-T_phi[p_])       # T_phis      = [T_phi[0], T_phi[1], ..., T_phi[p]]
        L_byT_phi.append([T_Lag**p_])   # L_byT_phi   = [[L**0], [L**1], ..., [L**p]]
    for P_ in range(0, P+1):
        S_phi[P_] = sympy.symbols(f'Phi_{P_}')
        S_phis.append(-S_phi[P_])       # S_phis      = [S_phi[0], S_phi[1], ..., S_phi[P]]
        L_byS_phi.append([S_Lag**P_])   # L_byS_phi   = [[(L**m)**0], [(L**m)**1], ..., [(L**m)**P]]
    for q_ in range(0, q+1):
        T_theta[q_] = sympy.symbols(f'theta_{q_}')
        T_thetas.append(T_theta[q_])    # T_thetas    = [T_theta[0], T_theta[1], ..., T_theta[q]]
        L_byT_theta.append([T_Lag**q_]) # L_byT_theta = [[L**0], [L**1], ..., [L**q]]
    for Q_ in range(0, Q+1):
        S_theta[Q_] = sympy.symbols(f'Theta_{Q_}')
        S_thetas.append(S_theta[Q_])    # S_thetas    = [T_theta[0], T_theta[1], ..., T_theta[Q]]
        L_byS_theta.append([S_Lag**Q_]) # L_byS_theta = [[(L**m)**0], [(L**m)**1], ..., [(L**m)**Q]]

    T_phi_Lag = sympy.Matrix([T_phis]) * sympy.Matrix(L_byT_phi)
    S_phi_Lag = sympy.Matrix([S_phis]) * sympy.Matrix(L_byS_phi)
    T_theta_Lag = sympy.Matrix([T_thetas]) * sympy.Matrix(L_byT_theta)
    S_theta_Lag = sympy.Matrix([S_thetas]) * sympy.Matrix(L_byS_theta)

    Y_operator = (T_phi_Lag * S_phi_Lag * T_Lag_Diff * S_Lag_Diff).subs(T_phi[0], -1).subs(S_phi[0], -1)[0]
    e_operator = (T_theta_Lag * S_theta_Lag).subs(T_theta[0], 1).subs(S_theta[0], 1)[0]

    Y_operation = sympy.collect(Y_operator.expand(), L)
    e_operation = sympy.collect(e_operator.expand(), L)

    Y_coeff = sympy.Poly(Y_operation, L).all_coeffs()[::-1]
    e_coeff = sympy.Poly(e_operation, L).all_coeffs()[::-1]

    Y_term = sympy.Matrix([Y_coeff]) * sympy.Matrix(Y__) # left-side
    e_term = sympy.Matrix([e_coeff]) * sympy.Matrix(e__) # right-side
    
    Time_Series = Y - Y_term[0] + e_term[0]
    Time_Series = sympy.collect(Time_Series, Y).simplify()
    return Time_Series

SARIMAEquation((1,1,2), (2,0,1,4))
