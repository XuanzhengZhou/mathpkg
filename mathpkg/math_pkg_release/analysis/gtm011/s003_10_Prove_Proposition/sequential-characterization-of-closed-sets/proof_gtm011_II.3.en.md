---
role: proof
locale: en
of_concept: sequential-characterization-of-closed-sets
source_book: gtm011
source_chapter: "II"
source_section: "3"
---

Suppose $F$ is closed and $x = \lim x_n$ where each $x_n$ is in $F$. So for every $\epsilon > 0$, there is a point $x_n$ in $B(x; \epsilon)$; that is $B(x; \epsilon) \cap F \neq \varnothing$, so that $x \in F^{-} = F$ by Proposition 1.13(f).

Now suppose $F$ is not closed; so there is a point $x_0$ in $F^{-}$ which is not in $F$. By Proposition 1.13(f), for every $\epsilon > 0$ we have $B(x_0; \epsilon) \cap F \neq \varnothing$. In particular for every integer $n$ there is a point $x_n$ in $B(x_0; 1/n) \cap F$. Thus, $d(x_0, x_n) < 1/n$ which implies that $x_n \to x_0$. Since $x_0 \notin F$, this says the condition fails.
