import numpy as np
import matplotlib.pyplot as plt


def agent_modelling(p=0.2, q=3, n=1000, t_sym=1000):
    agent = np.ones(n)
    c_list = np.zeros(t_sym)
    m_list = np.zeros(t_sym)

    for t in range(t_sym):
        for i in range(n):
            a = np.random.uniform(0, 1)
            if non_conformism(p):
                if np.random.uniform(0, 1) > 0.5:
                    agent[a] = 1
                else:
                    agent[a] = -1
            else:
                influence_group = [agent[k] for k in np.random.randint(0, n, q)]
                if np.sum(influence_group) == q:
                    agent[a] = 1
                elif np.sum(influence_group) == -q:
                    agent[a] = -1
        c_list

def non_conformism(p):
    if np.random.uniform(0, 1) < p:
        return True
    return False


if __name__ == '__main__':
    x = agent_modelling()
    t = np.linspace(10, 1000, 1000 - 10)
    plt.plot(t, x[10:])
    plt.show()
