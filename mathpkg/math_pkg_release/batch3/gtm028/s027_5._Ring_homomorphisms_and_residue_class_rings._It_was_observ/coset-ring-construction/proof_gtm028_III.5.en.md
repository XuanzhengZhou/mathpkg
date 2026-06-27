---
role: proof
locale: en
of_concept: coset-ring-construction
source_book: gtm028
source_chapter: "III"
source_section: "§5"
---

Addition of cosets has been defined in §3 and we know that $\bar{R}$ is an additive group. We define multiplication of cosets by $(a + N)(b + N) = ab + N$. We must show that this product is independent of the particular elements $a$ and $b$ of the cosets, that is, that if $a \equiv a_1 \pmod{N}$ and $b \equiv b_1 \pmod{N}$, then $ab \equiv a_1b_1 \pmod{N}$. This follows from the properties of congruence mod $N$ established above. Thus $\bar{R}$ is a set with two operations defined in it, and the mapping $T$, defined by $aT = a + N$ for $a \in R$, is a mapping of $R$ onto $\bar{R}$. It follows from the definition of multiplication that $(ab)T = (aT)(bT)$; that $(a+b)T = aT + bT$ we know from §3. From the lemma of I, §12, we conclude that $\bar{R}$ is a ring, that $T$ is a homomorphism of $R$ onto $\bar{R}$, and $N$ is the kernel.
