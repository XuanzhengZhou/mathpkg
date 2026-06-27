---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Godel's $\beta$-function lemma states that for any finite sequence of natural numbers there exists a single natural number $x$ from which each $y_i$ can be recovered as $\beta(x, i)$. The proof uses the Chinese remainder theorem: one chooses pairwise coprime moduli $m_i = 1 + (i + 1) \cdot s!$ where $s = \max\{y_0, \ldots, y_{n-1}, n\}$, then finds $x$ satisfying the simultaneous congruences $x \equiv y_i \pmod{m_i}$. This lemma is fundamental to Godel numbering and the arithmetization of syntax, establishing that finite sequences of arbitrary length can be encoded within elementary arithmetic.
