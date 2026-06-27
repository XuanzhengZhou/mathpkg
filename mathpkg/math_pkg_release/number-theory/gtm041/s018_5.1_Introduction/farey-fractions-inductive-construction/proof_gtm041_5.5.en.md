---
role: proof
locale: en
of_concept: farey-fractions-inductive-construction
source_book: gtm041
source_chapter: "5"
source_section: "5.4"
---

We use induction on $n$. When $n = 1$ the fractions $0/1$ and $1/1$ are consecutive and satisfy the unimodular relation. We pass from $F_1$ to $F_2$ by inserting the mediant $1/2$.

Now suppose $a/b$ and $c/d$ are consecutive in $F_n$ and satisfy the unimodular relation $bc - ad = 1$. By Theorem 5.3, they will be consecutive in $F_m$ for all $m$ satisfying

$$\max(b, d) \leq m \leq b + d - 1.$$

Form their mediant $h/k$, where $h = a + c$, $k = b + d$. By Theorem 5.4 we have $bh - ak = 1$ and $ck - dh = 1$, so $h$ and $k$ are coprime. Thus $h/k$ is a reduced fraction with denominator $k = b+d$, which is inserted into $F_{b+d}$ to form $F_{b+d}$. The new pairs $(a/b, h/k)$ and $(h/k, c/d)$ again satisfy the unimodular relation, completing the induction.
