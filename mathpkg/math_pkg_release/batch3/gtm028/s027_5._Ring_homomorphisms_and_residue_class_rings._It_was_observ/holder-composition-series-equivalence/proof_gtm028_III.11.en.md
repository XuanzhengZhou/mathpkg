---
role: proof
locale: en
of_concept: holder-composition-series-equivalence
source_book: gtm028
source_chapter: "III"
source_section: "§11"
---

By Theorem 19 we know that any two composition series have the same length $r$. Let them be
$$M = M_0 > M_1 > \cdots > M_r = (0)$$
$$M = N_0 > N_1 > \cdots > N_r = (0)$$
The proof proceeds by induction on the length $r$. Since the theorem is trivial for length 1, we assume it true for all modules of length less than $r$. If $M_1 = N_1$, then we have two composition series for $M_1$, and by the induction hypothesis they are equivalent. Since $M - M_1 = M - N_1$, so are the given series for $M$.

Assume, then, that $M_1 \neq N_1$, so that $M = M_1 + N_1$. By taking a fixed composition series for $M_1 \cap N_1$ we obtain two composition series for $M_1$ (one from the given series and one constructed via $M_1 \cap N_1$) and two for $N_1$. By the induction hypothesis these are equivalent respectively. In like manner the two given series are equivalent.
