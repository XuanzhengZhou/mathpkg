---
role: proof
locale: en
of_concept: binomial-expansion-term-bound
source_book: gtm041
source_chapter: "7"
source_section: "7.5"
---

Since $1 + \sum a_{r_1, \ldots, r_n} = g^p(1, 1, \ldots, 1) = (1 + n)^p$, this proves the coefficient sum identity.

Let $1 + N$ be the number of terms in the expansion. We shall prove that

$$1 + N \leq (p + 1)^n$$

by induction on $n$. For $n = 1$ we have

$$(1 + x_1)^p = 1 + \binom{p}{1}x_1 + \binom{p}{2}x_1^2 + \cdots + x_1^p$$

and the sum on the right has exactly $p + 1$ terms. Thus the inequality holds for $n = 1$.

If $n > 1$ we have

$$g^p = \{(1 + x_1 + \cdots + x_{n-1}) + x_n\}^p$$

$$= (1 + x_1 + \cdots + x_{n-1})^p + \binom{p}{1}(1 + \cdots + x_{n-1})^{p-1}x_n + \cdots + x_n^p,$$

so if there are at most $(p + 1)^{n-1}$ terms in each group on the right there will be at most $(p + 1)^n$ terms altogether. This proves the bound by induction.
