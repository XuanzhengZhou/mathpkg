---
role: proof
locale: en
of_concept: thm-suppose-a-three-dimensional-random-walk
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: To emphasize the essential features of the proof—which are the results of section 25, the estimate which comes from P1, and the way they are applied to the problem—we shall be a little casual about the measure theoretical aspects. Suffice

It seems reasonable to estimate the probabilities $P_0[E_n]$ from T25.1 which gives

$$P_0[E_n] = H_{A_n}(0) = \sum_{x \in A_n} G(0,x)E_{A_n}(x).$$

Letting $c_1, c_2, \ldots$ denote positive constants, one has

$$c_1|x|^{-1} \leq G(0,x) \leq c_2|x|^{-1} \text{ for all } x \neq 0$$

according to P1, and so

$$c_3 \sum_{x \in A_n} 2^{-n}E_{A_n}(x) \leq P_0[E_n] \leq c_4 \sum_{x \in A_n} 2^{-n}E_{A_n}(x),$$

or

$$c_3 2^{-n}C(A_n) \leq P_0[E_n] \leq c_4 2^{-n}C(A_n).$$

This inequality makes it plain what T1 is about, and what is left to prove. We have to show that

$$P_0\left[ \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} E_k \right] = 1$$

if and only if $\sum P_0[E_n] = \infty$. This conclusion can be obtained from a well-known form of the Borel-Cantelli Lemma.$^6$
