---
role: proof
locale: en
of_concept: conditional-smoothing-countable-partition
source_book: gtm046
source_chapter: "VIII"
source_section: "28.2"
---

**Proof.** Let $\mathfrak{B}$ be the minimal $\sigma$-field over a countable partition $\{B_j\}$ of $\Omega$, so the $B_j$ are atoms of $\mathfrak{B}$. On every nonnull atom $B \in \mathfrak{B}$, $E^\mathfrak{B}X$ is constant, and its value $E_B X$ is given by

$$E_B X \cdot PB = \int_B E^\mathfrak{B}X \, dP = \int_B X \, dP,$$

from which

$$E_B X = \frac{1}{PB} \int_B X \, dP$$

for $PB > 0$. On null atoms, $E^\mathfrak{B}X$ may be defined arbitrarily without affecting the almost-sure equivalence class.

Since the $B_j$ form a partition, any $\omega \in \Omega$ belongs to exactly one $B_j$. The conditional expectation at $\omega$ is the average of $X$ over the atom containing $\omega$. Therefore,

$$E^\mathfrak{B}X = \sum_j (E_{B_j}X) I_{B_j} \quad \text{a.s.},$$

where the right-hand side is a.s. defined because it is defined on each $B_j$ (and on null $B_j$ the value is irrelevant). This shows that conditional expectation with respect to a countably generated atomic $\sigma$-field reduces to averaging over the atoms of the partition.
