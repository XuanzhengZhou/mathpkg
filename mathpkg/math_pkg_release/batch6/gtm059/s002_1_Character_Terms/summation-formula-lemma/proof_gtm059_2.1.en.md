---
role: proof
locale: en
of_concept: summation-formula-lemma
source_book: gtm059
source_chapter: "2"
source_section: "1"
---

We may assume without loss of generality that $1 \leq k < n$. Both sides of the desired equality are $(q-1)$-periodic in the relevant variable, and the relation is trivially satisfied for $k=0$. Working modulo $q-1$, we write $k$ in its base-$p$ expansion:

$$k = k_0 + k_1 p + k_2 p^2 + \dots + k_{n-1} p^{n-1}$$

and

$$p^{n-1} k_0 + k_1 + k_2 p + \dots + k_{n-1} p^{n-2} \pmod{q-1}.$$

Both sides can then be compared term by term, and the periodicity together with the congruence modulo $q-1$ yields the stated equality.
