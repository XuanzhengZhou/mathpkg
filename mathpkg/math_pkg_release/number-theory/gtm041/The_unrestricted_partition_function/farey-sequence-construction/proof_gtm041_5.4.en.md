---
role: proof
locale: en
of_concept: farey-sequence-construction
source_book: gtm041
source_chapter: "5"
source_section: "5.4"
---

Proof by induction on $n$. When $n = 1$, the fractions $0/1$ and $1/1$ are consecutive and satisfy the unimodular relation $1 \cdot 1 - 0 \cdot 1 = 1$. We pass from $F_1$ to $F_2$ by inserting the mediant $1/2$.

Now suppose $a/b$ and $c/d$ are consecutive in $F_n$ and satisfy $bc - ad = 1$. By Theorem 5.3 (not in this section), they remain consecutive in $F_m$ for all $m$ satisfying

$$\max(b, d) \leq m \leq b + d - 1.$$

Form their mediant $h/k$ where $h = a + c$, $k = b + d$. By Theorem 5.4 we have $bh - ak = 1$ and $ck - dh = 1$, so $h/k$ is in lowest terms and is the unique fraction with denominator $k$ lying between $a/b$ and $c/d$. When $k = b + d = n + 1$, the fraction $h/k$ joins $F_{n+1}$. All new fractions in $F_{n+1}$ arise this way, and consecutive pairs in $F_{n+1}$ inherit the unimodular condition from Theorem 5.4.
