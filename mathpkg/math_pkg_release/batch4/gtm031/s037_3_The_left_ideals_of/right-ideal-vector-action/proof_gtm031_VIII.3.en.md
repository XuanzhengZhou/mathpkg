---
role: proof
locale: en
of_concept: right-ideal-vector-action
source_book: gtm031
source_chapter: "VIII"
source_section: "3"
---
We first show that $x\mathfrak{R}$ is mapped into itself by every $A \in \mathfrak{R}$. If $y \in x\mathfrak{R}$, then $y = xB$ for some $B \in \mathfrak{R}$, and $yA = xBA = xB'$ where $B' = BA$ is in $\mathfrak{R}$ since $\mathfrak{R}$ is a right ideal. Hence $yA \in x\mathfrak{R}$.

Next we show that $x\mathfrak{R}$ is closed under scalar multiplication. If $\alpha \in \Delta$ (the underlying division ring), there exists an $A \in \mathfrak{R}$ such that $yA = \alpha y$ for any $y$ (such an $A$ exists in $\mathfrak{L}$, and since $\mathfrak{R}$ is a right ideal containing elements of all ranks, the scalar multiplication is realized within $\mathfrak{R}$). Then $\alpha y = yA$ is in $x\mathfrak{R}$.

Thus $x\mathfrak{R}$ is a nonzero subspace invariant under $\mathfrak{R}$. As established in Chapter IV (p. 116), the only such subspace of the simple module $\mathfrak{R}$ is $\mathfrak{R}$ itself. Therefore $x\mathfrak{R} = \mathfrak{R}$.

The mapping $B \mapsto xB$ is an operator (module) homomorphism: $(BA)\chi = (B\chi)A$ for all $B, A \in \mathfrak{R}$. The kernel of $\chi$ is a right ideal of the ring $\mathfrak{R}$; for if $B\chi = 0$, then $(BA)\chi = (B\chi)A = 0A = 0$. It follows that if $\mathfrak{R}$ is a minimal right ideal, then the kernel of $\chi$ is $0$, making $\chi$ an isomorphism of $\mathfrak{R}$ onto $\mathfrak{R}$ as modules.
