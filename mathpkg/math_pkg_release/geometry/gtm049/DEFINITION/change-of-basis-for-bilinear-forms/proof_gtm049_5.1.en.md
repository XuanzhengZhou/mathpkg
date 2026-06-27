---
role: proof
locale: en
of_concept: change-of-basis-for-bilinear-forms
source_book: gtm049
source_chapter: "V"
source_section: "5.1"
---

**Proof.** Given two ordered bases $(a_1, \ldots, a_n), (b_1, \ldots, b_n)$ there is a unique $f$ in $\operatorname{Aut} V$ such that

$$b_i = a_i f \quad (i = 1, \ldots, n).$$

Now $(\sigma^f; (a_i)) = (\sigma; (b_i))$, by the definition of $\sigma^f$, while $(\sigma^f; (a_i))$ and $(\sigma; (a_i))$ are congruent by definition. Thus the matrices of $\sigma$ with respect to all ordered bases lie in a single congruence class.

To prove that we obtain the whole class, take any matrix $T$ congruent to $(\sigma; (a_i))$. By Proposition 1, $T = (\tau; (a_i))$ for some bilinear form $\tau$, and by the definition of congruence, $\tau = \sigma^f$ for some automorphism $f$ of $V$. Hence $T = (\sigma; (b_i))$ where $b_i = a_i f$ for $i = 1, \ldots, n$.
