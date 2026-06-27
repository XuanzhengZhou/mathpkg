---
role: proof
locale: en
of_concept: decomposition-law-relative-quadratic
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of the Decomposition Law in Relative Quadratic Extensions

**Theorem.** Let $K = k(\sqrt{\mu})$ be a relative quadratic extension ($l = 2$), where $k$ contains a primitive $2$nd root of unity (i.e., $\zeta = -1 \in k$, which is automatic). For a prime ideal $\mathfrak{p}$ of $k$ not dividing $2\mu$, the decomposition in $K$ is:
- $\mathfrak{p}$ splits iff $\mu$ is a quadratic residue modulo $\mathfrak{p}$,
- $\mathfrak{p}$ is inert iff $\mu$ is a quadratic non-residue modulo $\mathfrak{p}$,
- $\mathfrak{p}$ ramifies iff $\mathfrak{p} \mid \mu$.

*Proof.* This is the special case $l = 2$ of the general Kummer decomposition theory (Theorems 117-118). When $l = 2$, the primitive root of unity is $\zeta = -1 \in k$, so the hypothesis that $k$ contains $\zeta$ is always satisfied.

By Theorem 116, $K/k$ has relative degree $2$ provided $\mu$ is not a square in $k$.

Applying Theorem 118 with $l = 2$: let $a$ be the exponent of $\mathfrak{p}$ in $\mu$.

- If $2 \nmid a$ (i.e., $\mathfrak{p} \parallel \mu$), then $\mathfrak{p}$ is ramified: $\mathfrak{p} = \mathfrak{P}^2$.

- If $2 \mid a$ (i.e., $\mathfrak{p} \nmid \mu$ after adjusting), then $\mathfrak{p}$ is unramified. The decomposition depends on the solvability of $\mu \equiv \xi^2 \pmod{\mathfrak{p}}$:
  - Solvable $\implies$ $\mathfrak{p}$ splits: $\mathfrak{p} = \mathfrak{P}_1 \mathfrak{P}_2$ with $\mathfrak{P}_1 \neq \mathfrak{P}_2$.
  - Unsolvable $\implies$ $\mathfrak{p}$ remains prime (inert).

This generalizes the classical decomposition of rational primes $p$ in quadratic number fields $\mathbb{Q}(\sqrt{d})$ to arbitrary base fields $k$, with the Legendre symbol $\left(\frac{\mu}{\mathfrak{p}}\right)$ governing the splitting behavior. The case $\mathfrak{p} \mid 2$ is handled by Theorem 119, which gives the decomposition of prime divisors of $2$ in terms of higher power congruences. $\square$
