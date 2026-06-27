---
role: proof
locale: en
of_concept: gauss-lemma
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** It suffices to prove the second assertion: if $f_1(x)$ and $g_1(x)$ are primitive, then $f_1(x) g_1(x)$ is primitive. Suppose $f_1 g_1$ is not primitive. Let $p$ be an irreducible element of $R$ which divides all the coefficients of $f_1 g_1$. Write $f_1(x) = \sum a_i x^i$ and $g_1(x) = \sum b_j x^j$ with $a_i, b_j \in R$. Let $a_s$ and $b_t$ be the first coefficients of $f_1$ and $g_1$ respectively which are not divisible by $p$ (these exist since $f_1$ and $g_1$ are primitive).

The coefficient of $x^{s+t}$ in $f_1(x) g_1(x)$ is

$$\cdots + a_{s-1} b_{t+1} + a_s b_t + a_{s+1} b_{t-1} + \cdots.$$

Since $R$ is a unique factorization domain, $p$ does not divide $a_s b_t$ (as $p$ is irreducible and divides neither $a_s$ nor $b_t$). However, $p$ divides all other terms in the sum (each contains a factor $a_i$ with $i < s$ or $b_j$ with $j < t$, which by definition are divisible by $p$). Hence $p$ divides the sum itself — a contradiction. Thus $f_1(x) g_1(x)$ is primitive.

The first assertion follows: writing $f = c(f) f_1$ and $g = c(g) g_1$ with $f_1, g_1$ primitive, we have $fg = c(f)c(g) \cdot f_1 g_1$. Since $f_1 g_1$ is primitive, $c(fg) = c(f)c(g)$ up to a unit factor.
