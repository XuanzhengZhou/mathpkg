---
role: proof
locale: en
of_concept: semisimple-g-module-via-invariant-hermitian-form
source_book: gtm020
source_chapter: "9"
source_section: "6"
---

**Proof.** Let $L$ be a $G$-submodule, and let $\beta$ be a $G$-invariant hermitian form on $M$. Let $L'$ denote the subset of $y \in M$ with $\beta(x, y) = 0$ for all $x \in L$. Clearly, $L'$ is a $G$-submodule of $M$ (since $\beta$ is $G$-invariant) and $L \cap L' = \{0\}$.

For each $x \in M$, the function $y \mapsto \beta(x, y)$ is an element of the dual space $L^+$. Since the map $c_\beta: L \to L^+$ induced by $\beta$ is an isomorphism (by non-degeneracy of the hermitian form restricted to $L$), there exists $z \in L$ with $\beta(x, y) = \beta(z, y)$ for all $y \in L$. Then $x - z = z'$ satisfies $\beta(z', y) = 0$ for all $y \in L$, so $z' \in L'$. Hence $x = z + z'$ with $z \in L$, $z' \in L'$, proving $M = L \oplus L'$.

By induction on dimension, $M$ decomposes as a direct sum of simple $G$-submodules. $\square$
