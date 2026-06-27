---
role: proof
locale: en
of_concept: projective-limit-nonempty
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "2. p-adic equations"
---

*Proof.* The fact that $D \neq \varnothing$ is clear if the maps $D_n \to D_{n-1}$ are surjective; we reduce the lemma to this special case. For this, denote by $D_{n,p}$ the image of $D_{n+p}$ in $D_n$ under the composite map $D_{n+p} \to D_{n+p-1} \to \cdots \to D_n$. For fixed $n$, the $D_{n,p}$ form a decreasing family of finite nonempty subsets; hence this family is stationary, i.e., $D_{n,p}$ is independent of $p$ for $p$ large enough. Let $E_n$ be this limit value of the $D_{n,p}$. One checks immediately that the map $D_n \to D_{n-1}$ carries $E_n$ onto $E_{n-1}$; since the $E_n$ are nonempty and the restricted maps $E_n \to E_{n-1}$ are now surjective, we have $\varprojlim E_n \neq \varnothing$ by the remark made at the beginning. But $\varprojlim E_n \subset \varprojlim D_n = D$, hence $D \neq \varnothing$. $\square$
