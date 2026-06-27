---
role: exercise
locale: en
chapter: "3"
section: "3.8"
exercise_number: 9
---

Only in one special case can the concept of particle energy be extended to include what might be named gravitational and electromagnetic potential energy. This special case provides an instructive exercise that will be used in Section 3.11 to examine difficulties with the concept of total energy in general relativity.

Let $\alpha$ be a 1-form, and $X$ be a future-pointing timelike Killing vector field such that $\mathcal{L}_X \alpha = 0$.

\begin{enumerate}
  \item[(a)] Show that $d\alpha$ is an electromagnetic field $F$ on $M$ that satisfies $\mathcal{L}_X F = 0$.
  \item[(b)] Let $(\gamma, m, e)$ be a particle that obeys the Lorentz world-force law with respect to $F$. Show that
    $$-g(\gamma_*, X) - \frac{e}{2}(\alpha X) \circ \gamma: \mathcal{E} \rightarrow \mathbb{R}$$
    is a constant.
  \item[(c)] Let $\mathcal{P}$ be a consistent particle set, each of whose particles obeys the Lorentz world-force law relative to $F$, and let $x$ be a collision event. For each $(\gamma, m, e) \in \mathcal{P}$, let $C_\gamma$ be the constant from part (b). Show
    $$\sum_{\operatorname{in}(x)} C_\gamma = \sum_{\operatorname{out}(x)} C_\gamma.$$
\end{enumerate}

If $|X| \rightarrow 1$ at spatial infinity, $C_\gamma$ is sometimes called the "total energy" of $(\gamma, m, e)$, which includes its rest-mass energy, its kinetic energy, its gravitational potential energy, and its electromagnetic potential energy. One then has in mind a $(z, Z)$ such that $z \in \gamma$ and $Z \in \operatorname{span}(Xz)$, so that $-g(\gamma_*, Xz)/|Xz| = -g(\gamma_*, Z)$ is the particle energy observed by $(z, Z)$, and $-(e/2)(\alpha Xz)/|Xz| = -(e/2)\alpha Z$ is by definition the electric energy for $\gamma$ observed by $(z, Z)$.
