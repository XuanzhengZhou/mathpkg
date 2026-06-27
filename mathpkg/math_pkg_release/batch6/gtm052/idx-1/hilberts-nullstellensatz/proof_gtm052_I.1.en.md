---
role: proof
locale: en
of_concept: hilberts-nullstellensatz
source_book: gtm052
source_chapter: "I"
source_section: "1"
---

The proof of Hilbert's Nullstellensatz is lengthy. See Lang [2, p. 256], Atiyah--Macdonald [1, p. 85], or Zariski--Samuel [1, vol. 2, p. 164].

A standard proof proceeds via the Rabinowitsch trick: given $f$ vanishing on $Z(\mathfrak{a})$, introduce a new variable $y$ and consider the ideal $\mathfrak{a}' = \mathfrak{a} + (1 - yf)$ in $k[x_1, \ldots, x_n, y]$. Then $Z(\mathfrak{a}') = \varnothing$, so by the weak Nullstellensatz, $\mathfrak{a}' = (1)$. Writing $1 = \sum g_i h_i + g(1 - yf)$ and setting $y = 1/f$ yields $f^r \in \mathfrak{a}$ after clearing denominators.
