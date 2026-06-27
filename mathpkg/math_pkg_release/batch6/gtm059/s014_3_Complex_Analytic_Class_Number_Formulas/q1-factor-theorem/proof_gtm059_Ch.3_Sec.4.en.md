---
role: proof
locale: en
of_concept: q1-factor-theorem
source_book: gtm059
source_chapter: "3"
source_section: "4.6 The (±1)-conjectures"
---

Let $a$ be a generator of the group of roots of unity in $K = \mathbb{Q}(\zeta_m)$. Suppose first that $m$ is a prime power, $m = p^n$. Then the cyclotomic units generate a subgroup of index $1$ in the full unit group. Let $a$ be a primitive root of unity and let $b$ be a unit. The cyclotomic units are of the form

$$
\frac{1 - \zeta^a}{1 - \zeta}
$$

for integers $a$ coprime to $m$. When $m$ is a prime power, the cyclotomic field has a unique prime ideal above $p$, and the cyclotomic units together with the roots of unity generate the full unit group up to index $1$, so $Q_1 = 1$.

Now suppose $m$ is not a prime power, so $m$ has at least two distinct prime factors. In this case, the cyclotomic units generate a subgroup of index $2$ in the full unit group. Specifically, let $w$ denote the number of roots of unity in $K$. Then the cyclotomic units, together with $-1$ and a suitably chosen real unit, generate the full group of units, but the real unit coming from the cyclotomic construction is not always sufficient: the index is $2$ because of the presence of a square root of a unit that is not itself a cyclotomic unit. In this case $Q_1 = 2$.

The theorem therefore follows from the structure of the unit group in cyclotomic fields: the cyclotomic units are the full group of units when $m$ is a prime power, and form a subgroup of index $2$ when $m$ is composite.
