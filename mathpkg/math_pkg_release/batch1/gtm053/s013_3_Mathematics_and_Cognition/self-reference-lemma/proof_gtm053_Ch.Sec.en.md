---
role: proof
locale: en
of_concept: self-reference-lemma
source_book: gtm053
source_chapter: "VII"
source_section: "7"
---

Let the formula "$y = \text{diag } x$" express that $y$ is the Godel number of the diagonalization of the formula with Godel number $x$ (substituting the numeral of $x$ into the formula coded by $x$). Construct $R(x) : \exists y (\text{"}y = \text{diag } x" \wedge P(y))$, and set $Q_P : \neg R(\overline{N}(\neg R(x)))$, the diagonalization of $\neg R(x)$. By construction, $Q_P$ is true iff the number of $\neg R(x)$ does not satisfy $R(x)$ iff the number of $Q_P$ does not satisfy $P(x)$.
