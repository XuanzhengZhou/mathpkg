---
role: proof
locale: en
of_concept: closed-star-subalgebra-full
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of Closed *-Subalgebra is Full

Proof. As in (49.5), we regard $A$ as a subalgebra of $A_1$. We write $a, b, \ldots$ for elements of $A$, and $x, y, \ldots$ for elements of $A_1$. Each $x \in A_1$ defines a left-multiplication mapping $y \mapsto xy (y \in A_1)$; since $A$ is an ideal of $A_1$, it is invariant under this mapping. Thus, for each $x \in A_1$, we may define a linear mapping

$$T_x: A \rightarrow A$$

by the formula $T_x b = xb (b \in A)$. Clearly $T_x \in \mathcal{L}(A)$ and $\| T_x \| \leq \| x \|$.

It is straightforward to check that the mapping $x \mapsto T_x$ is an algebra homomorphism $A_1 \rightarrow \mathcal{L}(A)$. We assert that this mapping is injective. Indeed, if $T_x = 0$, where $x = a + \lambda 1$, then $ab + \lambda b = 0$ for all $b \in A$. Since $A$ has no unity element, it follows that $\lambda = 0$. {Proof: If $\lambda \neq 0$, then $(- \lambda^{-1} a) b = b$ for all $b \in A$, thus $- \lambda^{-1} a$ is a left unity element for $A$; in a ring with involution, a left unity element is a unity element.} Then $ab = 0$ for all $b \in A$. In particular $aa^* = 0$, and $a = 0$ results from $\| a \|^2 = \| aa^* \|$. Thus $x = 0$ as asserted.

It follows that the formula

$$|x| = \| T_x \| \quad (x \in A_1)$$

that $A_1$ is complete for the norm $|x|$ (48.5). In view of (iii), $(A, ||)$ is a complete and therefore closed linear subspace of $(A_1, ||)$; the quotient normed space $A_1/A$ induced by the norm $|x|$ (16.7) is one-dimensional, hence is trivially complete; therefore $(A_1, ||)$ is also complete (16.12). {Alternatively, the image of $A$ in $\mathcal{L}(A)$ is complete, hence closed; therefore the image of $A_1$ in $\mathcal{L}(A)$ is closed (23.6), hence complete.}
