---
role: proof
locale: en
of_concept: equational-presentation-of-algebraic-theories
source_book: gtm026
source_chapter: "5"
source_section: "5.40"
---

Define $(\Omega, E)$ as follows:

$$
\Omega_n = \{n\} \times nT \quad \text{if } n \in \mathrm{Law}(T)
$$
$$
\Omega_n = \varnothing \quad \text{if } n \notin \mathrm{Law}(T).
$$

Denoting the underlying set functor from $\Omega$-$\mathbf{alg}$ by $U$, each $\alpha \in nT$ becomes an $n$-ary operation $\hat{\alpha}: U^n \longrightarrow U$ of $\Omega$ by $(X, \delta)\hat{\alpha} = \delta_\alpha: X^n \longrightarrow X$ (where we write $\alpha \in \Omega_n$ for the more cumbersome $(n, \alpha)$). Define the equations $E$ by $E = E_1 \cup E_2 \cup E_3$ where:

$E_1$ is the class of all equations $\{U^p \xrightarrow{\hat{\alpha} \cdot (a_i)} U, \; U^p \xrightarrow{\hat{\beta} \cdot (b_j)} U\}$ corresponding to $(p, n, m, a, b, \alpha, \beta)$ such that $p, n, m \in \mathrm{Law}(T)$, $a: n \to pT$, $b: m \to pT$, $\alpha \in nT$, $\beta \in mT$, and the Kleisli composites $a \circ \alpha$ and $b \circ \beta$ are equal in $pT$.

$E_2$ encodes the unit: for each $n \in \mathrm{Law}(T)$ and each $i \in n$, the equation $U^n \xrightarrow{\pi_i} U = U^n \xrightarrow{\widehat{i\eta}} U$ where $\pi_i$ is the $i$-th projection and $i\eta \in \Omega_n$ is the operation corresponding to $i\eta \in nT$.

$E_3$ encodes the multiplication: for each $n, m \in \mathrm{Law}(T)$, $\alpha \in mT$, and $\beta_i \in nT$ for $i \in m$, the equation asserting that the composite operation $\hat{\alpha} \circ (\hat{\beta}_i)_{i \in m}$ equals the operation corresponding to the Kleisli composite of $\alpha$ with $(\beta_i)$ in $nT$.

The remainder of the proof establishes that the categories of $T$-algebras and $(\Omega, E)$-algebras are isomorphic via a functor that preserves the underlying sets.
