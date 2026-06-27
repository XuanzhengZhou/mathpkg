---
role: proof
locale: en
of_concept: positive-root-simple-sum-corollary
source_book: gtm009
source_chapter: "10"
source_section: "10.2"
---

Use Lemma 10.2A and induction on $\operatorname{ht} \beta$. If $\beta$ is simple, the statement is trivial (take $k=1$, $\alpha_1 = \beta$). Otherwise, by Lemma 10.2A, $\beta - \alpha$ is a positive root for some $\alpha \in \Delta$, with $\operatorname{ht}(\beta - \alpha) = \operatorname{ht}(\beta) - 1$. By the induction hypothesis, $\beta - \alpha = \alpha_1 + \ldots + \alpha_{k-1}$ with all partial sums $\alpha_1 + \ldots + \alpha_i$ being roots. Then $\beta = \alpha_1 + \ldots + \alpha_{k-1} + \alpha$, and each partial sum (including the full sum when $i = k$) is a root by construction. The proof works upward from the induction hypothesis.
