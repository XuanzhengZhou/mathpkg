---
role: proof
locale: en
of_concept: factoring-through-monomorphism
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof of (2).** For each $m \in M$, $f(m) \in \text{Im}\, f \subseteq \text{Im}\, g$. So since $g$ is monic, there is a unique $n' \in N'$ such that $g(n') = f(m)$. Therefore, there is a well-defined function $h: M \to N'$ (viz., $m \mapsto n'$) such that $f = gh$.

To verify $R$-linearity of $h$, let $x, y \in M$ and $a, b \in R$. Then
$$g(h(ax + by)) = f(ax + by) = af(x) + bf(y) = a g(h(x)) + b g(h(y)) = g(ah(x) + bh(y)).$$
Since $g$ is monic, we deduce $h(ax + by) = ah(x) + bh(y)$.

Uniqueness of $h$ follows from $g$ being monic: if $gh = gh'$, then $h = h'$. The statements about $\text{Ker}\, h$ and $\text{Im}\, h$ follow directly from the factorization $f = gh$ and the properties of $g$. $\square$
