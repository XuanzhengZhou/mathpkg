---
role: proof
locale: en
of_concept: factoring-through-epimorphism
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof of (1).** Since $g: M \to M'$ is epic, for each $m' \in M'$ there is at least one $m \in M$ with $g(m) = m'$. If also $\ell \in M$ with $g(\ell) = m'$, then clearly $m - \ell \in \text{Ker}\, g$. But since $\text{Ker}\, g \subseteq \text{Ker}\, f$, we have $f(m) = f(\ell)$. Thus, there is a well-defined function $h: M' \to N$ such that $f = hg$.

To see that $h$ is actually an $R$-homomorphism, let $x', y' \in M'$ and let $x, y \in M$ with $g(x) = x'$, $g(y) = y'$. Then for each $a, b \in R$, $g(ax + by) = ax' + by'$, so that
$$h(ax' + by') = f(ax + by) = af(x) + bf(y) = ah(x') + bh(y').$$

The uniqueness of $h$ with these properties is assured by (3.3.c) since $g$ is an epimorphism. The final assertions about $\text{Ker}\, h$ and $\text{Im}\, h$ are straightforward to verify. $\square$
