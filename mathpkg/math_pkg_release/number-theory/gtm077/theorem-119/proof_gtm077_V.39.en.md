---
role: proof
locale: en
of_concept: theorem-119
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of Theorem 119

**Theorem 119.** Let $\mathfrak{l}$ be the prime ideal divisor of $1 - \zeta$, which divides $1 - \zeta$ exactly to the $a$-th power: $1 - \zeta = \mathfrak{l}^a \mathfrak{l}_1$ (with $\mathfrak{l}_1$ prime to $\mathfrak{l}$). Suppose that $\mathfrak{l}$ does not divide $\mu$. Then the behavior of $\mathfrak{l}$ in $K = k(\sqrt[l]{\mu})$ is as follows:

1. $\mathfrak{l}$ splits into $l$ distinct prime ideals in $K$ if the congruence
   $$\mu \equiv \xi^l \pmod{\mathfrak{l}^{a+1}} \tag{82}$$
   can be solved by a number $\xi$ in $k$.

2. $\mathfrak{l}$ remains prime in $K$ if the congruence
   $$\mu \equiv \xi^l \pmod{\mathfrak{l}^a} \tag{83}$$
   can be solved, but (82) cannot be solved.

3. $\mathfrak{l}$ becomes the $l$-th power of a prime ideal in $K$ if the congruence (83) is also unsolvable.

**Proof.**

**I: Splitting case.** Suppose (82) is solvable, so $\mathfrak{l}$ splits into distinct factors: $\mathfrak{l} = \mathfrak{L} \cdot s\mathfrak{L} \cdots s^{l-1}\mathfrak{L}$ with distinct conjugates. As in the proof of Theorem 110, every integer in $K$ is congruent to an integer in $k$ modulo every power of $\mathfrak{L}$. Thus for each rational integer $b$ there exists $\xi \in k$ such that

$$M - \xi \equiv 0 \pmod{\mathfrak{L}^b}.$$

The relative norm of $M - \xi$ is then divisible by a high power of $\mathfrak{l}$. Working through the factorization shows that $\mathfrak{l}$ indeed decomposes into $l$ distinct conjugate prime ideals.

**II: Inert case.** Suppose (83) is solvable but (82) is not. Set $A = \rho(M - \xi)$ with a suitable multiplier $\rho$ so that $A$ is an integer in $K$ whose relative different is relatively prime to $\mathfrak{l}$. By Theorem 114, $\mathfrak{l}$ cannot be the $l$-th power of a prime ideal in $K$. Since (82) is unsolvable, $\mathfrak{l}$ does not split into distinct factors either (by part I). Therefore, by Theorem 117, $\mathfrak{l}$ must remain prime in $K$.

**III: Ramified case.** Suppose even (83) is unsolvable. Let $u$ be the highest exponent for which

$$\mu \equiv \xi^l \pmod{\mathfrak{l}^u}$$

is solvable. By Fermat's little theorem, every number is congruent to an $l$-th power modulo $\mathfrak{l}$, so $u \geq 1$. Moreover, $u$ is not divisible by $l$. For if

$$\mu \equiv \xi^l \pmod{\mathfrak{l}^{bl}}, \quad 0 < b \leq a-1,$$

were solvable, then we could lift the solution to modulo $\mathfrak{l}^{bl+1}$ as follows: choose an integer $\lambda$ in $k$ divisible by $\mathfrak{l}^b$ but not by $\mathfrak{l}^{b+1}$. Then for any integer $\omega$,

$$(\xi + \lambda\omega)^l \equiv \xi^l + \lambda^l \omega^l \pmod{\mathfrak{l}^{bl+1}}$$

provided $b \leq a-1$. Since $\omega^l$ represents every residue class modulo $\mathfrak{l}$, we can determine $\omega$ so that $\mu - (\xi + \lambda\omega)^l$ is divisible by $\mathfrak{l}^{bl+1}$. This would extend the solvability, contradicting the maximality of $u$.

Now with $u$ not divisible by $l$, one shows that the ideal $\mathfrak{P} = (\mathfrak{l}, \sqrt[l]{\mu})$ satisfies $\mathfrak{P}^l = \mathfrak{l}$, i.e., $\mathfrak{l}$ ramifies as the $l$-th power of the prime ideal $\mathfrak{P}$ in $K$.
