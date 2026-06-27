---
role: proof
locale: en
of_concept: subobject-classifier-for-arrow-category
source_book: gtm005
source_chapter: "I"
source_section: "9. Subsets and Characteristic Functions"
---

Given a subobject $m : (S, f|_S) \hookrightarrow (X, f)$ in $\mathbf{Sets}^{\mathbf{2}}$, we construct the classifying map $\psi : X \to \{0,1,2\}$ as the three-valued function:

$$\psi(x) =
\begin{cases}
0 & \text{if } x \in S, \\
1 & \text{if } x \notin S \text{ but } f(x) \in T, \\
2 & \text{if } f(x) \notin T.
\end{cases}$$

This map is well-defined because the three cases are mutually exclusive and exhaustive. To verify the pullback property: $x \in \psi^{-1}(\{0,2\})$ if and only if $\psi(x) = 0$ or $\psi(x) = 2$, which means either $x \in S$ (so $\psi(x) = 0$) or $f(x) \notin T$ (so $\psi(x) = 2$). In either case $x$ satisfies the defining property of $S$: $x \in S$ or $f(x) \notin T$, which is equivalent to the condition that $(x, f(x))$ belongs to the subobject. Hence $S = \psi^{-1}(\{0,2\})$, giving the required pullback square. The map $j$ restricts to the identity on $\{0,2\}$ (since $j(0)=0$ and $j(2)=2$), and this square commutes in $\mathbf{Sets}^{\mathbf{2}}$ because the upper horizontal arrow sends $S$ to $\{0,2\}$ compatibly with the restricted function $f|_S$. Uniqueness of $\psi$ follows because any classifying map must send elements of $S$ to $0$, elements outside $S$ whose $f$-image lies in $T$ to $1$, and the remainder to $2$.
