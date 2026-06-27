---
role: proof
locale: en
of_concept: dimension-formula-modular-forms
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

The dimension formula follows from Theorem 4. Parts (i) and (ii) establish the base cases: $\dim M_k = 0$ for $k < 0$ and $k = 1$, and $\dim M_k = 1$ for $k = 0, 2, 3, 4, 5$.

Part (iii) gives $\dim M_k^0 = \dim M_{k-6}$ for $k \geq 6$. Since $M_k = M_k^0 \oplus \mathbf{C} G_k$ for $k \geq 2$ (the Eisenstein series provides the non-cusp part), we have $\dim M_k = \dim M_{k-6} + 1$ for $k \geq 6$, with the exception $k = 1$ (where $M_1 = 0$ and the formula correctly gives $[1/6] = 0$).

Formula (21) holds for $0 \leq k < 6$ by checking directly. For $k \geq 6$, both $\dim M_k$ and the formula expression increase by one when $k$ is replaced by $k + 6$. By induction, the formula holds for all $k \geq 0$.
