---
role: proof
locale: en
of_concept: injective-test-lemma
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

(a) $\Leftrightarrow$ (b). This is by (16.14), since ${}_R R$ is a generator.

(b) $\Rightarrow$ (c). If $E$ is ${}_R R$-injective and $I \leq {}_R R$ with $h: I \to E$, then there exists $\bar{h}: R \to E$ such that $(\bar{h}|_I) = h$. Let $x = \bar{h}(1)$. Then for all $a \in I$, $h(a) = \bar{h}(a) = a \cdot \bar{h}(1) = ax$.

(c) $\Rightarrow$ (b). Let $I \leq {}_R R$ and $h: I \to E$. By (c) there exists $x \in E$ with $h(a) = ax$ for all $a \in I$. Define $\bar{h}: R \to E$ by $\bar{h}(r) = rx$. Then $\bar{h}$ is an $R$-homomorphism extending $h$.
