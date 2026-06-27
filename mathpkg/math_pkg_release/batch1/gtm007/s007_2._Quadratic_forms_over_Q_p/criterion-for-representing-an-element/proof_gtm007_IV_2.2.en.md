---
role: proof
locale: en
of_concept: criterion-for-representing-an-element
source_book: gtm007
source_chapter: "IV"
source_section: "§2.2.2"
---

Let $a \in k^*/k^{*2}$ and consider the augmented form $f_a = f \oplus a Z^2$, which has $n+1$ variables. Recall that $f_a$ represents $0$ nontrivially if and only if $f$ represents $a$.

The invariants of $f_a$ are:
$$d(f_a) = -a d, \qquad \varepsilon(f_a) = (-a, d) \varepsilon,$$
which follow directly from the definitions of discriminant and epsilon invariant.

Now apply Theorem 6 to $f_a$ with its invariants. The zero-representation condition gives:

- $n = 1$: $f_a$ has rank $2$, represents $0$ iff $d(f_a) = -1$, i.e., $-ad = -1$, which means $a = d$.
- $n = 2$: $f_a$ has rank $3$, represents $0$ iff $\varepsilon(f_a) = (-1, -d(f_a))$, i.e., $(-a, d)\varepsilon = (-1, ad)$, which simplifies to $(a, -d) = \varepsilon$.
- $n = 3$: $f_a$ has rank $4$, represents $0$ iff either $d(f_a) \neq 1$ or $(d(f_a) = 1$ and $\varepsilon(f_a) = (-1, -1))$. The condition $d(f_a) \neq 1$ means $-ad \neq 1$, i.e., $a \neq -d$. If $a = -d$ then $d(f_a) = 1$ and we need $\varepsilon(f_a) = (-1, -1)$, which is $(-a, d)\varepsilon = (-1, -1)$. Since $a = -d$, this becomes $(-1, -1)\varepsilon = (-1, -1)$, i.e., $\varepsilon = (-1, -d)$.
- $n \geq 4$: $f_a$ has rank $\geq 5$, so it always represents $0$ by Theorem 6(iv), hence $f$ always represents $a$.
