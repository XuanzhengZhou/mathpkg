---
role: proof
locale: en
of_concept: binary-expansion-correspondence
source_book: gtm095
source_chapter: "2"
source_section: "1"
---

# Proof of Binary Expansion Correspondence

**Statement.** Let $\Omega = \{\omega : \omega = (a_1, a_2, \ldots), a_i = 0, 1\}$ be the space of infinite sequences of zeros and ones. There is a one-to-one correspondence between $\Omega$ and the interval $[0, 1)$. Consequently, $\Omega$ has the cardinality of the continuum.

**Proof.** Every real number $a \in [0, 1)$ admits a binary expansion of the form

$$a = \frac{a_1}{2} + \frac{a_2}{2^2} + \frac{a_3}{2^3} + \cdots = \sum_{i=1}^{\infty} \frac{a_i}{2^i}, \qquad a_i \in \{0, 1\},$$

with the additional condition that the expansion contains infinitely many zeros. This representation is unique: if a number had two distinct binary expansions, subtracting them would yield a nontrivial relation $\sum (b_i - c_i)/2^i = 0$ with $b_i, c_i \in \{0,1\}$, which is impossible under the infinitely-many-zeros convention (dyadic rationals have exactly two expansions when expansions ending in all-ones are allowed; the restriction to expansions with infinitely many zeros selects a unique representative for each $a \in [0,1)$).

Conversely, given any sequence $\omega = (a_1, a_2, \ldots) \in \Omega$, the series $\sum_{i=1}^{\infty} a_i / 2^i$ converges (since it is bounded above by the geometric series $\sum 1/2^i = 1$) and defines a real number in $[0, 1)$.

Thus the mapping

$$\varphi : \Omega \longrightarrow [0, 1), \qquad \varphi(a_1, a_2, \ldots) = \sum_{i=1}^{\infty} \frac{a_i}{2^i}$$

is a bijection between $\Omega$ and $[0, 1)$.

Since $[0, 1)$ has the cardinality of the continuum $\mathfrak{c} = 2^{\aleph_0}$, the space $\Omega$ also has the cardinality of the continuum. Hence $N(\Omega) = \mathfrak{c}$, and the sample space for an infinite sequence of independent coin tosses is uncountable, in contrast to the finite sample space $|\Omega| = 2^n$ for $n$ tosses.

$\square$
