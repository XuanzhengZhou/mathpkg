---
role: proof
locale: en
of_concept: endomorphism-ring-injective
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

If $\operatorname{Ker} a \trianglelefteq E$, then it suffices to prove that $a S \ll S_S$ (see (15.3)). The proof is entirely dual to that of (17.11).

For the forward direction: assume $a \in J(S)$ and suppose $\operatorname{Ker} a$ is not essential in $E$. Then there exists $0 \neq K \leq E$ with $\operatorname{Ker} a \cap K = 0$. Since $E$ is injective, the isomorphism $K \cong a(K)$ extends to an endomorphism $b \in S$ with $b|_{a(K)} = (a|_K)^{-1}$. Then $(1 - ba)|_K = 0$, so $1 - ba$ is not monic. But $a \in J(S)$ implies $ba \in J(S)$, so $1 - ba$ is invertible, a contradiction. Thus $\operatorname{Ker} a \trianglelefteq E$.
