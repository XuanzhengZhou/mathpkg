---
role: exercise
locale: en
chapter: "22"
section: "SS 22"
exercise_number: "22.10"
---

Consider a generalization of (22.9). Let $\Gamma$ be arbitrary but infinite. For each $\gamma$, let $A_\gamma \in \mathcal{M}_\gamma$ and $f_\gamma(t) = \xi_{A_\gamma}(t_\gamma) - \mu_\gamma(A_\gamma)$. For $\Omega = \{\gamma_1,\ldots,\gamma_n\} \subset \Gamma$, let $w(\Omega) > 0$ and $h_\Omega = w(\Omega) \sum_{\gamma \in \Omega} f_\gamma$.

(a) Show that $\int_T |h_\Omega|^2 d\mu = w(\Omega)^2 \sum_{\gamma \in \Omega} [\mu_\gamma(A_\gamma) - (\mu_\gamma(A_\gamma))^2]$.

(b) Generalize convergence in measure: $h_\Omega \to 0$ in measure if for every $\delta,\varepsilon > 0$ there is $\Omega_0 \subset \Gamma$ such that $\mu(\{t: |h_\Omega(t)| \geq \delta\}) < \varepsilon$ for all $\Omega \supset \Omega_0$. Find reasonable conditions on $w(\Omega)$ for $h_\Omega$ to converge to $0$ in measure.
