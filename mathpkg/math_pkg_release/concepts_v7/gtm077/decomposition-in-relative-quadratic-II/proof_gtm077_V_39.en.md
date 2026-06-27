---
role: proof
locale: en
of_concept: decomposition-in-relative-quadratic-II
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of Theorem 117

**Theorem.** Only the following possibilities exist for the behavior of a prime ideal $\mathfrak{p}$ of $k$ under passage to $K = K(\sqrt[l]{\mu}; k)$:

1. $\mathfrak{p}$ remains a prime ideal in $K$ (inert),
2. $\mathfrak{p}$ becomes the $l$th power of a prime ideal in $K$ (totally ramified),
3. $\mathfrak{p}$ becomes the product of $l$ distinct prime ideals in $K$ (totally split).

*Proof.* Let $\mathfrak{P}$ be a prime ideal in $K$ dividing $\mathfrak{p}$. By Theorem 107, the relative norm of $\mathfrak{P}$ is

$$N_{K/k}(\mathfrak{P}) = \mathfrak{P} \cdot s\mathfrak{P} \cdot s^2\mathfrak{P} \cdots s^{l-1}\mathfrak{P} = \mathfrak{p}^{f_1},$$

where $f_1$ is the relative degree of $\mathfrak{P}$. This shows that no prime ideal other than the conjugates $s^m \mathfrak{P}$ can divide $\mathfrak{p}$.

Now consider two cases:

**Case 1:** $\mathfrak{P}$ is equal to one of its conjugates $s^m \mathfrak{P}$ for some $m \not\equiv 0 \pmod{l}$. Then $\mathfrak{P} = s\mathfrak{P} = \cdots = s^{l-1}\mathfrak{P}$, and the relative norm formula becomes $\mathfrak{P}^l = \mathfrak{p}^{f_1}$. Since $\mathfrak{p}$ is prime in $k$, this forces $f_1 = 1$ and $\mathfrak{P}^l = \mathfrak{p}$, which is case (2).

**Case 2:** $\mathfrak{P}$ is distinct from all its conjugates $s^m \mathfrak{P}$ ($m \not\equiv 0 \pmod{l}$). Then $\mathfrak{p}$ is divisible by the $l$ distinct prime ideals $\mathfrak{P}, s\mathfrak{P}, \ldots, s^{l-1}\mathfrak{P}$. Because no other primes divide $\mathfrak{p}$, we have

$$\mathfrak{p} = \mathfrak{P} \cdot s\mathfrak{P} \cdots s^{l-1}\mathfrak{P} \quad \text{or} \quad \mathfrak{p} = \mathfrak{P}.$$

In the first subcase we obtain case (3): $\mathfrak{p}$ splits into $l$ distinct prime ideals. In the second subcase we obtain case (1): $\mathfrak{p} = \mathfrak{P}$ remains prime in $K$. $\square$
