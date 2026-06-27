---
role: proof
locale: en
of_concept: riesz-representation-theorem
source_book: gtm023
source_chapter: "7"
source_section: "7.7"
---

The spaces $L(E)$ and $E$ are dual with respect to the bilinear function defined by $(f, x) \mapsto f(x)$ for $f \in L(E)$ and $x \in E$. On the other hand, $E$ is dual to itself with respect to the inner product $(\cdot, \cdot)$. Hence, by Corollary II to Proposition I (sec. 2.33), there exists a linear isomorphism $a \colon E \to L(E)$ defined by the condition

$$(a(x), y) = (x, y)$$

for all $x, y \in E$, where the pairing on the left is the evaluation of the linear functional $a(x)$ at $y$. Equivalently, $a(x)(y) = (x, y)$. This isomorphism is the Riesz representation: every linear functional on $E$ is of the form $y \mapsto (x, y)$ for a unique $x \in E$.
