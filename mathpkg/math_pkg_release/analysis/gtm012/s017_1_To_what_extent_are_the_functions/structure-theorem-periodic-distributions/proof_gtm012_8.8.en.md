---
role: proof
locale: en
of_concept: structure-theorem-periodic-distributions
source_book: gtm012
source_chapter: "8"
source_section: "8. Summary of operations on periodic distributions"
---

# Proof of the Structure Theorem for Periodic Distributions

**Theorem (Structure Theorem).** If $v \in \mathcal{C}$ (the space of continuous periodic functions) and $f$ is constant, then

$$D^k F_v + F_f \in \mathcal{P}'.$$

Conversely, if $F \in \mathcal{P}'$ is of order $k + 2$, $k \geq 0$, then there exist $v \in \mathcal{C}$ and a constant function $f$ such that

$$F = D^k F_v + F_f.$$

*Proof.* The forward direction is immediate: since $F_v$ and $F_f$ are periodic distributions and differentiation preserves $\mathcal{P}'$, the sum $D^k F_v + F_f$ is a periodic distribution.

The converse direction is Theorem 6.1, proved earlier in the chapter. The proof proceeds as follows. Given a periodic distribution $F$ of order $k+2$, one constructs a continuous function $v$ by integrating (or anti-differentiating) $F$ an appropriate number of times. Specifically, the order bound

$$|F(u)| \leq c \sum_{j=0}^{k+2} \|D^j u\|_\infty$$

implies that $F$ can be extended to a continuous linear functional on $C^{k+2}(\mathbb{T})$. By repeated integration (solving $D^{k+2} w = u$), one obtains a representation of $F$ acting on $u$ as the action of a continuous function $v$ on $D^k u$ plus a constant term. The constant term $F_f$ accounts for the kernel of the differentiation operator, which consists precisely of constant functions on the circle. $\square$

The uniqueness question for the functions $v$ and $f$ in this representation is subtle: $v$ is determined only up to addition of a polynomial in the anti-derivative process of degree at most $k$, and the constant $f$ is adjusted accordingly. See the exercises following Theorem 6.1 for details.
