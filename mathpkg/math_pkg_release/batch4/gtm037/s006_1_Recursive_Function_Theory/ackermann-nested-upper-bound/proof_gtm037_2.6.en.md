---
role: proof
locale: en
of_concept: ackermann-nested-upper-bound
source_book: gtm037
source_chapter: "2"
source_section: "2.6"
---

We proceed by induction on $p$:

Base case $p = 0$:

$$a(a(m, n), 0) = a(m, n) = a(m, n + 2 \cdot 0).$$

Inductive step: assume the result holds for $p$. Then

$$a(a(m, n), p + 1) = a(m, n)^{a(a(m, n), p)} \leq a(m, n)^{a(m, n + 2p)}$$

by the inductive hypothesis. Applying Lemma 2.42,

$$\leq a(m, \max(n + 2p + 2, n + 1))$$
$$= a(m, n + 2(p + 1)).$$

Thus the statement holds for $p + 1$, completing the induction.
