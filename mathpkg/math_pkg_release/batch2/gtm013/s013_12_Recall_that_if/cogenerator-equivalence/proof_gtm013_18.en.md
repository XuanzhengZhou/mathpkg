---
role: proof
locale: en
of_concept: cogenerator-equivalence
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

(a) $\Rightarrow$ (b): If $C$ is a cogenerator and $f: M \to N$ with $\operatorname{Hom}_R(f, C) = 0$, then for any $x \in M$, since $\operatorname{Rej}_M(C) = 0$, there exists $\alpha: N \to C$ with $\alpha f(x) \neq 0$, contradicting $\operatorname{Hom}_R(f, C)(\alpha) = \alpha f = 0$. Thus $f = 0$.

(b) $\Rightarrow$ (c): $\operatorname{Hom}_R(f, C) = 0 \implies f = 0$ means the functor is faithful.

(c) $\Rightarrow$ (d): If $\operatorname{Hom}_R(f, C)$ and $\operatorname{Hom}_R(g, C)$ form an exact sequence, then $\operatorname{Hom}_R(g f, C) = 0$, so faithfulness gives $g f = 0$. Exactness of the original sequence then follows from the fact that $C$ reflects kernels and cokernels.

(d) $\Rightarrow$ (a): Let $n: M \to M/\operatorname{Rej}_M(C)$ be the natural map. Then $n^* : \operatorname{Hom}_R(M/\operatorname{Rej}_M(C), C) \to \operatorname{Hom}_R(M, C)$ is an isomorphism. Under hypothesis (d), $n$ must be monic, so $\operatorname{Rej}_M(C) = 0$.
