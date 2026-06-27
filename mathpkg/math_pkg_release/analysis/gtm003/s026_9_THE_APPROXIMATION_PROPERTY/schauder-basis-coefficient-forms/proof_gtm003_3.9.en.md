---
role: proof
locale: en
of_concept: schauder-basis-coefficient-forms
source_book: gtm003
source_chapter: "Chapter III"
source_section: "9. The Approximation Property. Compact Maps"
---

Letting $\|x\|_1 = \sup_n \| \sum_{k=1}^{n} \alpha_k x_k\|$, $x \mapsto \|x\|_1$ is a new norm on $E$ under which $E$ is complete. Since $\|x\| \leq \|x\|_1$, the new norm also generates the topology of $E$ by Corollary 2 of (2.1). It follows that there exists a number $C \geq 1$ such that $\|x\|_1 \leq C \|x\|$ for all $x \in E$ (cf. Chapter II, Exercise 5). Now for each $n \in \mathbb{N}$,

$$|\alpha_n| = \|\alpha_n x_n\| = \| \sum_{k=1}^{n+1} \alpha_k x_k - \sum_{k=1}^{n} \alpha_k x_k\| \leq 2 \|x\|_1 \leq 2C \|x\|,$$

which implies that $x \mapsto \alpha_n = f_n(x)$ are equicontinuous linear forms. The remainder is immediate from (4.6).
