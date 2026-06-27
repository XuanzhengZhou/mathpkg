---
role: proof
locale: en
of_concept: dcc-equivalent-to-acc-with-maximal-primes
source_book: gtm028
source_chapter: "IV"
source_section: "§2. Rings with descending chain condition"
---

We first show that if the ideal $(0)$ is a product of maximal ideals, then the a.c.c. and d.c.c. hold.

Assume conversely that $R$ satisfies the d.c.c. We have already seen that every prime ideal $\mathfrak{B} \neq R$ is maximal. It remains to show that $(0)$ is a product of maximal (or prime) ideals.

Let $\mathfrak{D}$ be a minimal element of the set of ideals which are products of prime ideals. Suppose $\mathfrak{D} \neq (0)$ and derive a contradiction. Set $\mathfrak{A} = (0):\mathfrak{D}$. Since $\mathfrak{D} \neq (0)$ and $R$ contains an identity, $\mathfrak{A} \neq R$, so the family of ideals properly containing $\mathfrak{A}$ is non-empty. Let $\mathfrak{B}$ be a minimal element of this family. The ideal $\mathfrak{B}$ contains $\mathfrak{A}$; we claim it is prime.

If $c \notin \mathfrak{B}$ and $d \notin \mathfrak{B}$, then $c\mathfrak{B} + \mathfrak{A} = d\mathfrak{B} + \mathfrak{A} = \mathfrak{B}$, since both properly contain $\mathfrak{A}$ and are contained in $\mathfrak{B}$ while being distinct from $\mathfrak{A}$ by minimality. Hence
$$cd\mathfrak{B} + \mathfrak{A} = c(d\mathfrak{B} + \mathfrak{A}) + \mathfrak{A} = c\mathfrak{B} + \mathfrak{A} = \mathfrak{B},$$
so $cd\mathfrak{B} \not\subset \mathfrak{A}$ and $cd \notin \mathfrak{B}$. Thus $\mathfrak{B}$ is prime.

Since $\mathfrak{D} \neq (0)$ and $\mathfrak{B}$ is a minimal proper over-ideal of $\mathfrak{A} = (0):\mathfrak{D}$, one can show $\mathfrak{B}$ contains $\mathfrak{D}$. Since $\mathfrak{B}$ is prime and contains the product $\mathfrak{D}$ of primes, $\mathfrak{B}$ contains one factor of $\mathfrak{D}$, contradicting the minimality of $\mathfrak{D}$. Hence $\mathfrak{D} = (0)$, proving that $(0)$ is a product of maximal ideals. The a.c.c. then follows.
