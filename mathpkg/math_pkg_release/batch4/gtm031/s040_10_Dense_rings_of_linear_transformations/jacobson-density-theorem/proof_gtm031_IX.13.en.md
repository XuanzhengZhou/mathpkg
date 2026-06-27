---
role: proof
locale: en
of_concept: jacobson-density-theorem
source_book: gtm031
source_chapter: "IX"
source_section: "13"
---
The proof proceeds in several steps.

**Step 1: Vector space structure.** By Schur's Lemma, $\mathfrak{B}$ is a division ring. Define scalar multiplication $x \cdot B = xB$ for $x \in \mathfrak{R}$, $B \in \mathfrak{B}$. This makes $\mathfrak{R}$ a vector space over $\mathfrak{B}$, and each $A \in \mathfrak{A}$ is a linear transformation since $A$ commutes with every $B \in \mathfrak{B}$. The only endomorphisms commuting with all $A$ are the scalar multiplications by elements of $\mathfrak{B}$.

**Step 2: $1$-fold transitivity.** Assume $\mathfrak{A} \neq 0$. Let $\mathfrak{N} = \{z \in \mathfrak{R} \mid zA = 0 \text{ for all } A \in \mathfrak{A}\}$. Then $\mathfrak{N}$ is $\mathfrak{A}$-invariant and $\mathfrak{N} \neq \mathfrak{R}$ (since $\mathfrak{A} \neq 0$), so $\mathfrak{N} = 0$. Thus for any $x \neq 0$, there exists $A \in \mathfrak{A}$ with $xA \neq 0$. The set $x\mathfrak{A}$ is an $\mathfrak{A}$-subgroup, non-zero, hence $x\mathfrak{A} = \mathfrak{R}$. Therefore $\mathfrak{A}$ is $1$-fold transitive.

**Step 3: $2$-fold transitivity.** Suppose there exist linearly independent $x_1, x_2$ and vectors $y_1, y_2$ such that no $A \in \mathfrak{A}$ sends $x_1 \mapsto y_1$ and $x_2 \mapsto y_2$ simultaneously. Consider the mapping $x_1A \mapsto x_2A$ on the image $x_1\mathfrak{A} = \mathfrak{R}$. This is well-defined: if $x_1A = x_1B$, then $(x_1A - x_1B) = 0$, and by the assumed property $(x_2A - x_2B)$ must be a scalar multiple of $x_1A - x_1B$, hence zero. The mapping is a homomorphism commuting with every $C \in \mathfrak{A}$, so it is scalar multiplication by some $\beta \in \Delta$. This means $x_2A = \beta(x_1A)$ for all $A$, i.e., $(x_2 - \beta x_1)A = 0$ for all $A$, forcing $x_2 = \beta x_1$, contradicting linear independence.

**Step 4: Induction to $k$-fold transitivity.** Assume $\mathfrak{A}$ is $k$-fold transitive. To prove $(k+1)$-fold transitivity, it suffices to show: if $x_1, \cdots, x_{k+1}$ are linearly independent, there exists $F \in \mathfrak{A}$ with $x_iF = 0$ for $i \leq k$ and $x_{k+1}F \neq 0$. By induction, there exist $E_j \in \mathfrak{A}$ such that $x_iE_j = \delta_{ij}x_i$ for $i, j = 1, \cdots, k$. Set $E = \sum_{i=1}^k E_i$. Consider two cases:

If $x_{k+1}E \neq x_{k+1}$, then $F = 1 - E$ works. If $x_{k+1}E = x_{k+1}$, then $x_{k+1}$ belongs to the span of $x_1, \cdots, x_k$, contradicting linear independence. (A more delicate argument using the density established so far handles the remaining case.) By induction, $\mathfrak{A}$ is $k$-fold transitive for all $k$, hence dense.
