---
role: proof
locale: en
of_concept: injective-cogenerator-equivalence
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

(a) $\Rightarrow$ (c) $\Rightarrow$ (b) are trivial.

(b) $\Rightarrow$ (a): Assume $E$ satisfies (b). Let $M$ be a left $R$-module and $0 \neq x \in M$. Since $Rx$ is cyclic, it contains a maximal submodule, so $Rx$ has a simple factor module $T$. By (b) there exists a non-zero homomorphism $h: T \to E$. Composing with the natural map $Rx \to T$ gives a non-zero $h: Rx \to E$ with $h(x) \neq 0$. Since $E$ is injective, $h$ extends to $\bar{h}: M \to E$ with $\bar{h}(x) \neq 0$. Thus $\operatorname{Rej}_M(E) = 0$, so $E$ is a cogenerator.
