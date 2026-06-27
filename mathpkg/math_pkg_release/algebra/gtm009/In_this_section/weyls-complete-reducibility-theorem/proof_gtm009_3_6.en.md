---
role: proof
locale: en
of_concept: weyls-complete-reducibility-theorem
source_book: gtm009
source_chapter: "3"
source_section: "6"
---

We proceed in two steps.

**Step 1: Codimension one case.** Let $W \subset V$ be an $L$-submodule of codimension one. We may assume $W$ is irreducible (if not, replace by a proper nonzero submodule). The quotient $V/W$ is one-dimensional, and by the Lemma, $L$ acts trivially on $V/W$, so $\phi(L)$ sends $V$ into $W$. Consider the Casimir element $c_\phi$ of the (possibly non-faithful) representation $\phi$. Since $c_\phi$ is a linear combination of products $\phi(x)\phi(y)$, it also sends $V$ into $W$, so $c_\phi$ has trace $0$ on $V/W$.

On the other hand, $c_\phi$ commutes with $\phi(L)$. By Schur's Lemma, $c_\phi$ acts as a scalar on the irreducible submodule $W$. This scalar cannot be $0$, because then $\operatorname{Tr}_V(c_\phi) = 0$, contradicting $\operatorname{Tr}(c_\phi) = \dim L' \neq 0$ (where $L'$ is the sum of simple ideals on which $\phi$ is faithful). Hence $\ker c_\phi$ is a one-dimensional $L$-submodule intersecting $W$ trivially, giving the desired complement.

**Step 2: General case.** Let $W$ be a proper nonzero submodule of $V$. Consider the $L$-module $\operatorname{Hom}(V, W)$ with the natural action. Let $\mathcal{V}$ be the subspace of maps whose restriction to $W$ is scalar multiplication, and $\mathcal{W}$ the subspace of maps vanishing on $W$. Both are $L$-submodules and $L$ maps $\mathcal{V}$ into $\mathcal{W}$. Moreover, $\mathcal{V}/\mathcal{W}$ is one-dimensional. By Step 1, there exists an $L$-invariant complement to $\mathcal{W}$ in $\mathcal{V}$, i.e., a map $f \in \mathcal{V}$ with $f|_W = 1_W$ and $L.f = 0$. The condition $L.f = 0$ means $f$ is an $L$-module homomorphism, so $\ker f$ is an $L$-submodule of $V$ complementary to $W$.
