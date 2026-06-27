---
role: proof
locale: en
of_concept: properties-of-bounded-and-totally-bounded-sets
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

**(i)** Let $B$ be bounded and let $U$ be a given circled $0$-neighborhood. By (1.3)(i), there exists a circled $0$-neighborhood $V$ such that $V + V \subset U$. Since $B$ is bounded, there exists $\lambda \in K$ such that $B \subset \lambda V$. It follows from (1.3)(ii) that $\overline{B} \subset \overline{\lambda V} = \lambda \overline{V} \subset \lambda(V + V) \subset \lambda U$, so $\overline{B}$ is bounded. The proof for total boundedness is similar: if $B$ is totally bounded, then for any $0$-neighborhood $U$, there exists a finite set $B_0 \subset B$ with $B \subset B_0 + U$. Then $\overline{B} \subset \overline{B_0 + U} = B_0 + \overline{U}$, and we can choose a finer $0$-neighborhood inside $U$ to obtain the conclusion.

**(ii)** By induction, it suffices to prove for two sets. If $A_1, A_2$ are bounded and $U$ is a $0$-neighborhood, find $V$ with $V + V \subset U$. Then $A_i \subset \lambda_i V$ for $i = 1,2$. Taking $\lambda = \max\{|\lambda_1|, |\lambda_2|\}$ (or using the fact that $V$ is circled, so $\lambda_i V \subset \lambda V$ if $|\lambda_i| \leq \lambda$), we get $A_1 \cup A_2 \subset \lambda U$.

**(iii)** The circled hull of a bounded set $B$ is contained in the circled hull of $\lambda U$ for suitable $\lambda$, and the circled hull of $\lambda U$ is $\lambda U$ itself since $U$ is circled. Hence the circled hull is bounded.

**(iv)** Assume $K$ is locally precompact and let $B$ be totally bounded. Given a circled $0$-neighborhood $U$, choose a circled $0$-neighborhood $V$ with $V + V \subset U$. Since $B$ is totally bounded, there exists a finite set $B_0 \subset B$ such that $B \subset B_0 + V$. Now $B_0 \subset \lambda_0 V$, and we can assume $|\lambda_0| \geq 1$ since $V$ is circled. We obtain $B \subset \lambda_0(V + V) \subset \lambda_0 U$, so $\lambda_0^{-1} B \subset U$. The circled hull of $B$ is then a subset of $\lambda_0 \Gamma(B_0) + \lambda_0 V$ (where $\Gamma$ denotes circled hull). The circled hull of the finite set $B_0$ is $\Gamma(B_0) = \{\sum \mu_i b_i : |\mu_i| \leq 1\}$, which is the image of the compact set $S^n \times B_0^n$ under a continuous multilinear map, hence compact (thus totally bounded). Therefore, the circled hull of $B$ is totally bounded if $K$ is locally precompact.

To prove the final assertion, it is evidently sufficient to show that the circled hull of a finite subset of $L$ is totally bounded, provided that $K$ is locally precompact. In view of (iii), it suffices to observe that each set $Sa$ is totally bounded where $a \in L$ and $S = \{\lambda: |\lambda| \leq 1\}$; but this is clear from $(LT)_2$ and the assumed precompactness of $S$ (cf. (5.4) below). This completes the proof.
