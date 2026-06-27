---
role: proof
locale: en
of_concept: weyls-complete-reducibility-theorem
source_book: gtm009
source_chapter: "II"
source_section: "6"
---

The proof proceeds by induction. First consider the special case where $W \subset V$ is an irreducible submodule of codimension 1. Since $L$ acts trivially on $V/W$ (one-dimensional, by Lemma 6.3), $\phi(L)$ sends $V$ into $W$.

Construct the Casimir element $c_\phi$ of $\phi$ (see 6.2), which acts on $V$ and has $\operatorname{Tr}(c_\phi) = \dim L \neq 0$. Since $L$ maps $V$ into $W$, $c_\phi$ (as a linear combination of products $\phi(x_i)\phi(y_i)$) also maps $V$ into $W$. Thus $c_\phi$ has trace 0 on $V/W$. But $c_\phi$ acts as a scalar $\lambda$ on $W$ by Schur's Lemma (since $W$ is irreducible and $c_\phi$ commutes with $L$). If $\lambda = 0$, then $\operatorname{Tr}_V(c_\phi) = 0$, contradiction. Hence $\lambda \neq 0$, so $\ker c_\phi$ is a one-dimensional $L$-submodule intersecting $W$ trivially — the desired complement.

For the general case: Let $W \subset V$ be a nonzero proper submodule, $0 \rightarrow W \rightarrow V \rightarrow V/W \rightarrow 0$. Consider $\operatorname{Hom}(V, W)$ as an $L$-module (6.1). Define $\mathcal{V} \subset \operatorname{Hom}(V, W)$ as the subspace of maps whose restriction to $W$ is scalar multiplication. If $f|_W = a \cdot 1_W$, then for $x \in L$, $w \in W$:
$$(x.f)(w) = x.f(w) - f(x.w) = a(x.w) - a(x.w) = 0,$$
so $x.f|_W = 0$. Let $\mathcal{W} \subset \mathcal{V}$ be the subspace of maps with zero restriction to $W$. Then $\mathcal{V}/\mathcal{W}$ is one-dimensional, and $L$ maps $\mathcal{V}$ into $\mathcal{W}$.

By the codimension-1 case, $\mathcal{W}$ has a complement in $\mathcal{V}$: there exists $f \in \mathcal{V}$ with $f|_W = 1_W$ and $L.f = 0$. The condition $L.f = 0$ means $x.f(v) - f(x.v) = 0$ for all $x \in L$, $v \in V$, i.e., $f$ is an $L$-module homomorphism. Thus $\ker f$ is an $L$-submodule of $V$ complementary to $W$.

By induction, every submodule has a complement, so $V$ is completely reducible.
