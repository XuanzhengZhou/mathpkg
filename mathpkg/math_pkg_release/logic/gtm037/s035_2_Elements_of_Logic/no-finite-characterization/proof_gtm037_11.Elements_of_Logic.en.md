---
role: proof
locale: en
of_concept: no-finite-characterization
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

Assume the contrary: there exists a set $\Gamma$ of $\mathcal{L}$-sentences such that $\mathfrak{A} \models \Gamma$ iff $\mathfrak{A}$ is finite.

Expand $\mathcal{L}$ to $\mathcal{L}'$ by adjoining new individual constants $c_m$ for each $m \in \omega$. Let $\Delta = \Gamma \cup \{\neg(c_i = c_j) : i, j \in \omega, i \neq j\}$.

We claim every finite subset $\Delta' \subseteq \Delta$ has a model. Choose a finite set $T \subseteq \omega$ such that all constants in $\Delta' \setminus \Gamma$ are among $\{c_i : i \in T\}$. Let $\mathfrak{A}$ be any finite $\mathcal{L}'$-structure in which $c_i^{\mathfrak{A}} \neq c_j^{\mathfrak{A}}$ for all distinct $i, j \in T$ (this is possible since we can take a finite set with at least $|T|$ elements). The $\mathcal{L}$-reduct $\mathfrak{A} \upharpoonright \mathcal{L}$ is a finite $\mathcal{L}$-structure, so by the assumed property of $\Gamma$, $\mathfrak{A} \upharpoonright \mathcal{L} \models \Gamma$. Thus $\mathfrak{A} \models \Delta'$.

By the compactness theorem (a consequence of the completeness theorem), $\Delta$ has a model $\mathfrak{B}$. Since $c_i^{\mathfrak{B}} \neq c_j^{\mathfrak{B}}$ for all distinct $i, j \in \omega$, the universe of $\mathfrak{B}$ contains infinitely many distinct elements, so $\mathfrak{B}$ is infinite. But $\mathfrak{B} \upharpoonright \mathcal{L} \models \Gamma$, contradicting the assumed property that models of $\Gamma$ are exactly the finite structures.
