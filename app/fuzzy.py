import gauss_var

def calcfuzzy(threat, min, max):
    
    sig = 1
    
    mu = (min + max) / 6
   
    mu_m_b = mu
    mu_b = mu_m_b + mu
    mu_med = mu_b + mu
    mu_med_m = mu_med + mu
    mu_a = mu_med_m + mu
    m_m_a = mu_a + mu

    muito_baixo = gauss_var.gauss_var(sig, mu_m_b, threat)
    baixo = gauss_var.gauss_var(sig, mu_b, threat)
    medio = gauss_var.gauss_var(sig, mu_med, threat)
    medio_m  = gauss_var.gauss_var(sig,mu_med_m,threat);
    alto = gauss_var.gauss_var(sig, mu_a, threat)
    muito_alto = gauss_var.gauss_var(sig, m_m_a, threat)
    
    fuzzyficacao = [muito_baixo, baixo, medio,medio_m, alto, muito_alto]

    return fuzzyficacao

#print(calcfuzzy(13,1,36))


### OK ###