---
role: proof
locale: en
of_concept: homotopy-isomorphism-so-versus-o
source_book: gtm020
source_chapter: "4"
source_section: "12"
---

Consider the determinant map $\det: O(n) \to \mathbf{Z}_2$. Its kernel is $SO(n)$, giving the fibre sequence
$$SO(n) \xrightarrow{i} O(n) \xrightarrow{\det} \mathbf{Z}_2,$$
which is a fibration (in fact, a principal $\mathbf{Z}_2$-bundle).

The homotopy exact sequence of this fibration reads:
$$\cdots \to \pi_{i+1}(\mathbf{Z}_2) \to \pi_i(SO(n)) \xrightarrow{i_*} \pi_i(O(n)) \xrightarrow{\det_*} \pi_i(\mathbf{Z}_2) \to \cdots$$

Since $\mathbf{Z}_2$ is a discrete group, its homotopy groups are:
$$\pi_j(\mathbf{Z}_2) = \begin{cases} \mathbf{Z}_2 & j = 0 \\ 0 & j \geq 1 \end{cases}$$

For $i \geq 1$, we have $\pi_{i+1}(\mathbf{Z}_2) = 0$ and $\pi_i(\mathbf{Z}_2) = 0$, so the exact sequence fragment becomes:
$$0 \to \pi_i(SO(n)) \xrightarrow{i_*} \pi_i(O(n)) \to 0,$$
which proves that $i_*$ is an isomorphism for all $i \geq 1$.
