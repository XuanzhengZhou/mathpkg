---
role: exercise
locale: en
chapter: "24"
section: "24"
exercise_number: 9
---

The purpose of this exercise is to obtain another decomposition of a tensor product, based on explicit knowledge of the weights of one module involved.

Begin, as in (24.4), with the equation
$$
\operatorname{ch}_{\lambda'} * \omega(\lambda'' + \delta) = \sum_{\lambda \in \Lambda^+} n(\lambda) \, \omega(\lambda + \delta). \tag{2}
$$

Replace $\operatorname{ch}_{\lambda'}$ on the left side by $\sum_{\lambda \in \Lambda} m_{\lambda'}(\lambda) \varepsilon_{\lambda}$, and combine to get:
$$
\sum_{\sigma \in \mathcal{W}} \operatorname{sn}(\sigma) \sum_{\lambda} m_{\lambda'}(\lambda) \varepsilon_{\sigma(\lambda + \lambda'' + \delta)},
$$
using the fact that $\mathcal{W}$ permutes weight spaces of $V(\lambda')$.

Next show that the right side of (2) can be expressed as
$$
\sum_{\sigma \in \mathcal{W}} \operatorname{sn}(\sigma) \sum_{\lambda \in \Lambda^+} n(\lambda) \varepsilon_{\sigma(\lambda + \delta)}.
$$

Define $t(\mu)$ to be $0$ if some element $\sigma \neq 1$ of $\mathcal{W}$ fixes $\mu$, and to be $\operatorname{sn}(\sigma)$ if nothing but $1$ fixes $\mu$ and if $\sigma(\mu)$ is dominant. Then deduce from Exercise 8 that:
$$
\operatorname{ch}_{\lambda'} * \operatorname{ch}_{\lambda''} = \sum_{\lambda \in \Pi(\lambda')} m_{\lambda'}(\lambda) \, t(\lambda + \lambda'' + \delta) \, \operatorname{ch}_{\{\lambda + \lambda'' + \delta\} - \delta},
$$
where the braces denote the unique dominant weight to which the indicated weight is conjugate.
