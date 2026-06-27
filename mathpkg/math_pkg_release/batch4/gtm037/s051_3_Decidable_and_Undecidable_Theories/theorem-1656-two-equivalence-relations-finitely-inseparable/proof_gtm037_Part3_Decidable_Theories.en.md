---
role: proof
locale: en
of_concept: theorem-1656-two-equivalence-relations-finitely-inseparable
source_book: gtm037
source_chapter: "Part 3"
source_section: "Decidable and Undecidable Theories"
---

We interpret a symmetric binary relation into this theory. Let

$$\mathcal{L} : \text{language with a single binary relation symbol } \mathbf{R};$$
$$\Gamma = \{\varphi \in \text{Sent}_{\mathcal{L}} : \Theta \models \varphi\}, \text{where } \Theta = \{\forall v_0 \forall v_1 (\mathbf{R}v_0v_1 \rightarrow \mathbf{R}v_1v_0)\}.$$
$$\mathcal{L}' : \text{language with two binary relation symbols } \mathbf{L} \text{ and } \mathbf{M};$$
$$\Gamma' = \{\varphi \in \text{Sent}_{\mathcal{L}} : \Omega \models \varphi\}, \text{where } \Omega \text{ consists of the natural axioms for two equivalence relations:}$$
$$\begin{array}{l}
\forall v_1 \mathbf{L}v_0v_0; \\
\forall v_0 \forall v_1 (\mathbf{L}v_0v_1 \rightarrow \mathbf{L}v_1v_0); \\
\forall v_0 \forall v_1 \forall v_2 (\mathbf{L}v_0v_1 \wedge \mathbf{L}v_1v_2 \rightarrow \mathbf{L}v_0v_2); \\
\forall v_0 \mathbf{M}v_0v_0; \\
\forall v_0 \forall v_1 (\mathbf{M}v_0v_1 \rightarrow \mathbf{M}v_1v_0); \\
\forall v_0 \forall v_1 \forall v_2 (\mathbf{M}v_0v_1 \wedge \mathbf{M}v_1v_2 \rightarrow \mathbf{M}v_0v_2).
\end{array}$$

Given a finite model $\mathfrak{A}$ of $\Gamma'$, we construct a finite model $\mathfrak{B}$ of $\Gamma''$ as follows. Let $B = A$. To define $\mathbf{O}^{\mathfrak{A}}$ and $\mathbf{P}^{\mathfrak{A}}$, first let $f$ be a choice function for non-empty subsets of $A$. Thus $fx \in x$ whenever $\emptyset \neq x \subseteq A$. Now define $\mathbf{O}^{\mathfrak{A}}x = f[x]_{\mathbf{L}^{\mathfrak{A}}}$ and $\mathbf{P}^{\mathfrak{A}}x = f[x]_{\mathbf{M}^{\mathfrak{A}}}$ for any $x \in A$ (where $\mathfrak{A} = (A, \mathbf{L}^{\mathfrak{A}}, \mathbf{M}^{\mathfrak{A}})$); clearly $\mathfrak{B}$ is the desired interpretation of $\mathfrak{A}$.
