---
role: proof
locale: en
of_concept: multiplicative-group-of-finite-field-is-cyclic
source_book: gtm007
source_chapter: "I"
source_section: "1"
---

Let $n = q-1$. For each divisor $d$ of $n$, let $\psi(d)$ be the number of elements of $\mathbb{F}_q^*$ of order exactly $d$. Since the order of every element divides $n$, we have $n = \sum_{d|n} \psi(d)$. If $\psi(d) > 0$, let $a$ be an element of order $d$. The cyclic subgroup $\langle a \rangle$ has order $d$ and all its elements satisfy $x^d = 1$. The equation $x^d = 1$ has at most $d$ solutions in a field, so $\langle a \rangle$ contains all of them. Thus all elements of order $d$ lie in $\langle a \rangle$, whose generators number $\phi(d)$. Hence $\psi(d) = 0$ or $\psi(d) = \phi(d)$.

Since $n = \sum_{d|n} \phi(d)$ (Lemma 1), and $\psi(d) \leq \phi(d)$ for each $d$, we must have $\psi(d) = \phi(d)$ for all $d|n$. In particular, $\psi(n) = \phi(n) \geq 1$, so there exists an element of order $n$. Hence $\mathbb{F}_q^*$ is cyclic.
