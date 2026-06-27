---
role: proof
locale: en
of_concept: interlacing-lemma
source_book: gtm027
source_chapter: "4"
source_section: "E. Problems (Ordinal Space Properties)"
---

# Proof of the Interlacing Lemma

Let $X$ be a linearly ordered set and let $\{x_n\}_{n \in \omega}$ and $\{y_n\}_{n \in \omega}$ be sequences in $X$ such that
$$x_n \leq y_n \leq x_{n+1} \qquad \text{for each } n \in \omega.$$

**Claim**: Both sequences converge (in the order topology), and they converge to the same point.

**Proof**:

The inequalities $x_0 \leq x_1 \leq x_2 \leq \cdots$ follow by induction from $x_n \leq y_n \leq x_{n+1}$. Thus $\{x_n\}$ is a non-decreasing sequence. Similarly, $y_0 \leq y_1 \leq y_2 \leq \cdots$.

If the sequence $\{x_n\}$ is bounded above, then by properties of well-ordered sets (or by taking the supremum in a complete lattice), it has a least upper bound. Let $\xi = \sup_n x_n$. Then for any open interval $(a, b)$ containing $\xi$, we have $a < \xi < b$. Since $\xi = \sup_n x_n$, there exists $N$ such that $a < x_N \leq \xi < b$, and by monotonicity, $x_n \in (a, b)$ for all $n \geq N$. Thus $x_n \to \xi$.

For $\{y_n\}$, since $x_n \leq y_n \leq x_{n+1}$, we have $x_n \leq y_n \leq \xi$ for all $n$. Given any neighborhood $(a, b)$ of $\xi$, choose $N$ such that $x_n \in (a, b)$ for $n \geq N$. Then for $n \geq N$, $a < x_n \leq y_n \leq x_{n+1} < b$ (adjusting $N$ if needed), so $y_n \to \xi$ as well.

If the sequence is unbounded, then in the context of $\Omega_0$ (the space of countable ordinals), an unbounded non-decreasing sequence converges to $\Omega$ (the first uncountable ordinal), and by the same interlacing argument, both sequences converge to $\Omega$.

In particular, when $X = \Omega_0 = [0, \Omega)$, both $\{x_n\}$ and $\{y_n\}$ converge to the same point, which is either a countable ordinal (if bounded) or $\Omega$ (if unbounded).
