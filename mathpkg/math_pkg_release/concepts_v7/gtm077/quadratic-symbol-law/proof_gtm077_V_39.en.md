---
role: proof
locale: en
of_concept: quadratic-symbol-law
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of Theorem 119

**Theorem.** Let $\mathfrak{l}$ be a prime ideal of $k$ dividing $1 - \zeta$, and let $a$ be the exact exponent such that $\mathfrak{l}^a \parallel 1 - \zeta$, i.e., $1 - \zeta = \mathfrak{l}^a \mathfrak{l}_1$ with $\mathfrak{l} \nmid \mathfrak{l}_1$. Assume $\mathfrak{l} \nmid \mu$. Then in $K = k(\sqrt[l]{\mu})$:

1. $\mathfrak{l}$ splits into $l$ distinct prime ideals if $\mu \equiv \xi^l \pmod{\mathfrak{l}^{al+1}}$ is solvable in $k$.
2. $\mathfrak{l}$ remains prime if $\mu \equiv \xi^l \pmod{\mathfrak{l}^{al}}$ is solvable but the congruence modulo $\mathfrak{l}^{al+1}$ is not.
3. $\mathfrak{l}$ becomes the $l$th power of a prime ideal if even $\mu \equiv \xi^l \pmod{\mathfrak{l}^{al}}$ is unsolvable.

*Proof.* **Case I.** Assume $\mu \equiv \xi^l \pmod{\mathfrak{l}^{al+1}}$ is solvable. From the splitting $\mathfrak{l} = \mathfrak{L} \cdot s\mathfrak{L} \cdots s^{l-1}\mathfrak{L}$ with distinct conjugates, it follows (as in the proof of Theorem 110) that every integer in $K$ is congruent to an integer in $k$ modulo every power of $\mathfrak{L}$. Hence for each rational integer $b$ there exists $\xi \in k$ such that

$$M - \xi \equiv 0 \pmod{\mathfrak{L}^b},$$

where $M = \sqrt[l]{\mu}$. The relative norm $N_{K/k}(M - \xi) = \prod_{m=0}^{l-1} (\zeta^m M - \xi)$ is then divisible by a high power of $\mathfrak{l}$, showing that $\mu \equiv \xi^l$ modulo the corresponding power of $\mathfrak{l}$.

Conversely, if the congruence $\mu \equiv \xi^l \pmod{\mathfrak{l}^{al+1}}$ holds, then one verifies that the element

$$\rho = \frac{1 - \zeta}{M - \xi}$$

is an integer in $K$ whose relative norm is relatively prime to $\mathfrak{l}$. The ideal $(\rho, s\rho)$ then contains an element relatively prime to $\mathfrak{l}$, which means $\mathfrak{l}$ has a factor in $K$ distinct from all its conjugates. By Theorem 117, $\mathfrak{l}$ splits into $l$ distinct prime factors.

**Case II.** Suppose $\mu \equiv \xi^l \pmod{\mathfrak{l}^{al}}$ is solvable but not modulo $\mathfrak{l}^{al+1}$. Setting $A = \rho(M - \xi)$ with $\rho$ as above, $A$ is an integer in $K$ whose relative different is relatively prime to $\mathfrak{l}$. Consequently, by Theorem 114, $\mathfrak{l}$ cannot be the $l$th power of a prime ideal in $K$. Since case (I) is excluded by hypothesis, Theorem 117 forces $\mathfrak{l}$ to remain prime in $K$.

**Case III.** Suppose even $\mu \equiv \xi^l \pmod{\mathfrak{l}^{al}}$ is unsolvable. Let $u$ be the maximal exponent for which $\mu \equiv \xi^l \pmod{\mathfrak{l}^u}$ is solvable. Since $\mathfrak{l} \mid (1 - \zeta)$, we have $\mathfrak{l} \mid l$, and by Fermat's little theorem in residue fields, every element is congruent to an $l$th power modulo $\mathfrak{l}$, so $u \geq 1$.

We claim $l \nmid u$. Suppose to the contrary that $u = bl$ with $0 < b \leq a - 1$ and $\mu \equiv \xi^l \pmod{\mathfrak{l}^{bl}}$ is solvable. Choose $\lambda \in k$ divisible by $\mathfrak{l}^b$ but not by $\mathfrak{l}^{b+1}$. Then for any integer $\omega$,

$$(\xi + \lambda \omega)^l \equiv \xi^l + \lambda^l \omega^l \pmod{\mathfrak{l}^{bl+1}},$$

since all intermediate binomial coefficients $\binom{l}{j}$ for $1 \leq j \leq l-1$ are divisible by $l$ and hence by $\mathfrak{l}$, giving at least one extra factor of $\mathfrak{l}$. The term $\lambda^l \omega^l$ is divisible by $\mathfrak{l}^{bl}$ but not necessarily by $\mathfrak{l}^{bl+1}$ (since $\lambda$ is exactly divisible by $\mathfrak{l}^b$ and $\mathfrak{l} \nmid \omega$). Because $\omega^l$ runs through all residue classes modulo $\mathfrak{l}$, we can choose $\omega$ so that

$$\mu - (\xi + \lambda \omega)^l \equiv 0 \pmod{\mathfrak{l}^{bl+1}},$$

contradicting the maximality of $u$. Hence $l \nmid u$.

Since $u$ is not divisible by $l$, the method of Case I of Theorem 118 (replacing $\mu$ by an associated generator) shows that $\mathfrak{l}$ is the $l$th power of a prime ideal in $K$. $\square$
