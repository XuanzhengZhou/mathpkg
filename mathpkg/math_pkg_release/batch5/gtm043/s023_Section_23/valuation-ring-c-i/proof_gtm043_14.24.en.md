---
role: proof
locale: en
of_concept: valuation-ring-quotient-theorem
source_book: gtm043
source_chapter: "14"
source_section: "23"
---

(3) implies (4). This holds in any ring; for if $(a) \subset (b)$, then $(a, b) = (b)$.

(4) implies (1). By the lemma, $C/I$ is a totally ordered integral domain. Given $a, b \in C/I$, with $0 < a < b$, we are to show that $a$ is a multiple of $b$. By hypothesis, $(a, b) = (d)$ for some $d$, and we may assume that $d > 0$. There exist $a_1, b_1, s, t \in C/I$ such that $a = a_1d$, $b = b_1d$, and $sa + tb = d$. Then $(sa_1 + tb_1)d = d$, whence $sa_1 + tb_1 = 1$, since $C/I$ has no zero-divisors. Now, $0 < a_1 < b_1$. It follows that $b_1$ is a unit, since otherwise we would have

$$sa_1 + tb_1 \leq (|s| + |t|)b_1 < 1,$$

by 14.5(a). Thus, $b_1^{-1}$ exists, and $a = a_1b_1^{-1}b$.

It has already been noted that condition (4) implies that $I$ is a prime ideal. (See also 14B.3.) This completes the proof of the theorem.
