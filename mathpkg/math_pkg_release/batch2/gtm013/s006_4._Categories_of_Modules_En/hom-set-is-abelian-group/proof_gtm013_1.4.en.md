---
role: proof
locale: en
of_concept: hom-set-is-abelian-group
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

Let $M$ and $N$ be left $R$-modules. For $f, g \in \operatorname{Hom}_R(M, N)$, define $f + g$ and $-f$ pointwise by

$$(f + g)(x) = f(x) + g(x), \quad (-f)(x) = -f(x) \quad (x \in M).$$

We verify that $f + g$ is an $R$-homomorphism. For $x, y \in M$ and $r \in R$:

$$(f + g)(x + y) = f(x + y) + g(x + y) = f(x) + f(y) + g(x) + g(y)$$
$$= (f(x) + g(x)) + (f(y) + g(y)) = (f + g)(x) + (f + g)(y).$$

$$(f + g)(rx) = f(rx) + g(rx) = rf(x) + rg(x) = r(f(x) + g(x)) = r(f + g)(x).$$

Thus $f + g \in \operatorname{Hom}_R(M, N)$. Similarly, $-f \in \operatorname{Hom}_R(M, N)$.

The abelian group axioms are inherited from the abelian group structure of $N$:

- **Associativity**: $((f + g) + h)(x) = f(x) + g(x) + h(x) = (f + (g + h))(x)$.
- **Identity**: The zero homomorphism $0(x) = 0_N$ satisfies $(f + 0)(x) = f(x) + 0 = f(x)$.
- **Inverse**: $(f + (-f))(x) = f(x) - f(x) = 0$, so $-f$ is the additive inverse.
- **Commutativity**: $(f + g)(x) = f(x) + g(x) = g(x) + f(x) = (g + f)(x)$.

Therefore $\operatorname{Hom}_R(M, N)$ is an abelian group under pointwise addition.
