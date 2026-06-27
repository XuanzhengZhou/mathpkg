---
role: proof
locale: en
of_concept: characteristic-function-pullback
source_book: gtm005
source_chapter: "I"
source_section: "9. Subsets and Characteristic Functions"
---

Given $S \subset X$ with inclusion $i : S \hookrightarrow X$, and the characteristic function $\psi_S : X \to \{0,1\}$ defined by $\psi_S(x) = 0$ for $x \in S$ and $\psi_S(x) = 1$ for $x \notin S$, and $t : \{0\} \hookrightarrow \{0,1\}$ the inclusion:

To verify the square is a pullback, recall that in $\mathbf{Sets}$ a pullback of $t$ along $\psi_S$ is the set $\{ (x, 0) \in X \times \{0\} \mid \psi_S(x) = t(0) = 0 \}$. Since $\psi_S(x) = 0$ precisely when $x \in S$, this pullback is $\{ (x, 0) \mid x \in S \} \cong S$. The pullback square commutes because both paths $S \to \{0\} \to \{0,1\}$ and $S \to X \to \{0,1\}$ send every $x \in S$ to $0$.

Moreover, the top arrow $S \to \{0\}$ is the unique map from $S$ to the terminal object $\{0\}$ (a singleton in $\mathbf{Sets}$), and the bottom arrow $\psi_S$ is the classifying map. The uniqueness of this pullback representation follows from the fact that $\psi_S$ is the only function $X \to \{0,1\}$ whose fiber over $0$ is exactly $S$, showing that $S = \psi_S^{-1}(\{0\})$.
