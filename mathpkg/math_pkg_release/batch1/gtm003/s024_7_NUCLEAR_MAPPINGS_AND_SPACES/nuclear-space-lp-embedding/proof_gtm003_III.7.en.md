---
role: proof
locale: en
of_concept: nuclear-space-lp-embedding
source_book: gtm003
source_chapter: "III"
source_section: "7. Nuclear Mappings and Spaces"
---

Let $U$ be an arbitrary convex, circled $0$-neighborhood in $E$. By Theorem 7.2 and the definition of nuclear space, the canonical map $\phi_U: E \to \tilde{E}_U$ is nuclear. Hence by (7.1), $\phi_U$ admits a representation
$$\phi_U(x) = \sum_{n=1}^{\infty} \lambda_n f_n(x) y_n,$$
where we can assume $\lambda_n > 0$ for all $n \in \mathbb{N}$, $\sum_{n=1}^{\infty} \lambda_n = 1$, $\|y_n\| = 1$ in $\tilde{E}_U$, and the sequence $\{f_n\}$ is equicontinuous.

For a fixed $p$ with $1 \leq p \leq \infty$, define a map $v: E \to \ell^p$ by
$$v(x) = \left( \sqrt[p]{\lambda_1} f_1(x),\, \sqrt[p]{\lambda_2} f_2(x),\, \ldots \right)$$
for all $x \in E$ (set $\sqrt[p]{\lambda_n} = 1$ for all $n$ if $p = \infty$). By the equicontinuity of $\{f_n\}$, we have $v(x) \in \ell^p$ and $v \in \mathcal{L}(E, \ell^p)$.

Let $p^{-1} + q^{-1} = 1$ (with $q = 1$ if $p = \infty$ and $q = \infty$ if $p = 1$). Applying Hölder's inequality to $\sum \alpha_n \beta_n$ with $\alpha_n = \sqrt[p]{\lambda_n} f_n(x)$ and $\beta_n = \sqrt[q]{\lambda_n}$, we obtain
$$\|\phi_U(x)\| = \left\|\sum_{n=1}^{\infty} \lambda_n f_n(x) y_n\right\| \leq \sum_{n=1}^{\infty} \lambda_n |f_n(x)| \leq \|v(x)\|_p,$$
where $\|\cdot\|$ denotes the norm in $\tilde{E}_U$. Hence $v^{-1}(B) \subset U$, where $B$ is the unit ball of $\ell^p$. Setting $V = v^{-1}(B)$, the definition of $v$ implies that $E_V$ is norm isomorphic to $v(E)$, so $\tilde{E}_V$ is norm isomorphic to the closed subspace $\overline{v(E)}$ of $\ell^p$.
