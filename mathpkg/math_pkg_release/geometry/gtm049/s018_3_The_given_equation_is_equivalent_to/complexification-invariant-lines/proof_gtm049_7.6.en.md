---
role: proof
locale: en
of_concept: complexification-invariant-lines
source_book: gtm049
source_chapter: "7"
source_section: "7.6"
---

Complexify the real vector space $U$ to $U_{(c)} = U \otimes_{\mathbb{R}} \mathbb{C}$ and extend $f$ to a complex-linear endomorphism $f_{(c)}$ of $U_{(c)}$. The complex conjugation on $U_{(c)}$ is defined by $\overline{u \otimes z} = u \otimes \overline{z}$ for $u \in U$, $z \in \mathbb{C}$.

If $L \subset U_{(c)}$ is a one-dimensional $f_{(c)}$-invariant subspace, then $L = \mathbb{C} \cdot v$ for some eigenvector $v$ of $f_{(c)}$ with eigenvalue $\lambda \in \mathbb{C}$.

Now consider the conjugate subspace $\overline{L} = \mathbb{C} \cdot \overline{v}$. Since $f_{(c)}$ commutes with complex conjugation (as $f$ is real), $\overline{L}$ is also $f_{(c)}$-invariant, with eigenvalue $\overline{\lambda}$.

The sum $L + \overline{L} \subset U_{(c)}$ is invariant under both $f_{(c)}$ and complex conjugation. Its intersection with the real subspace $U$ (the fixed points of conjugation) is
$$V = (L \oplus \overline{L}) \cap U = \{ w + \overline{w} : w \in L \},$$
which is a real $f$-invariant subspace of $U$. If $\lambda \in \mathbb{R}$, then $L = \overline{L}$ and $\dim_{\mathbb{R}} V = 1$ (a real eigenvector). If $\lambda \notin \mathbb{R}$, then $L \cap \overline{L} = \{0\}$ and $\dim_{\mathbb{R}} V = 2$, corresponding to a pair of conjugate complex eigenvectors.
