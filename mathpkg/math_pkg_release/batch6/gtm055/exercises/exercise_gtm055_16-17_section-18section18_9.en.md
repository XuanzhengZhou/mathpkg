---
role: exercise
locale: en
chapter: "16-17"
section: "Section 18_Section_18"
exercise_number: 9
---

I. Thus $\Omega$ is invariant under all rotations $R_{\gamma}$, $\gamma \in Z$, whence it follows that $\Omega$ is constant a.e. $[\theta]$. That is, there exists a complex number $\omega$ such that $\Omega = \omega$ a.e. $[\theta]$. (This may be seen in various ways. Suppose, for example, that the real function $g = \text{Re}(\Omega)$ is not essentially constant on $Z$. Then there exist real numbers $m$ and $m'$ where $m < m'$ such that $E = \{\zeta \in Z : g(\zeta) \leq m\}$ and $E' = \{\zeta \in Z : g(\zeta) \geq m'\}$ both have positive arc-length measure. Thus there exist real numbers $t$ and $t'$ and a positive number $h$ such that the intersection of $E$ with the arc $\{e^{iu} : t \leq u \leq t + h\}$ has arc-length measure greater than $h/2$, while the intersection of $E'$ with the congruent arc $\{e^{iu} : t' \leq u \leq t' + h\}$ likewise has arc-length measure greater than $h/2$ (see Problem 8F). But then it is impossible for $\Omega$ and $R_{\gamma}\Omega$ to be equal a.e. if we take for $\gamma$ the number $e^{i(t' - t)}$. Finally, to determine the value of $\omega$, we employ Example J to write

$$\int_Z \Omega d\theta = 2\pi \omega = \int_Z \left[ \int_Z f_{(\gamma)} d\theta \right] d\theta(\gamma) = 2\pi \int_Z f d\theta.$$

Thus $\omega = \int_Z f d\theta$, and, putting everything together, we see that

$$\int_Z f_{(\gamma)} d\theta(\gamma) = \int_Z f d\theta$$

for almost every $\gamma$ in $Z$ and for every $f$ in $\mathcal{L}_p(Z)$.

If $\gamma \rightarrow 
...
