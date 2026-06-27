---
role: proof
locale: en
of_concept: classical-groups-compactness
source_book: gtm020
source_chapter: "7"
source_section: "1"
---

$O(k)$ is the subset of $M_k(\mathbf{R}) \cong \mathbf{R}^{k^2}$ defined by the equations $(u(x)|u(y)) = (x|y)$ for all $x, y \in \mathbf{R}^k$. These are polynomial equations in the entries of $u$, so $O(k)$ is closed. Moreover, for any $u \in O(k)$, each column $u(e_j)$ satisfies $\|u(e_j)\| = \|e_j\| = 1$, so the entries of $u$ are bounded by $1$ in absolute value. Thus $O(k)$ is a closed and bounded subset of $\mathbf{R}^{k^2}$, hence compact by the Heine--Borel theorem.

The same argument applies to $U(k)$ as a subset of $M_k(\mathbf{C}) \cong \mathbf{C}^{k^2} \cong \mathbf{R}^{2k^2}$, and to $Sp(k)$ as a subset of $M_k(\mathbf{H}) \cong \mathbf{R}^{4k^2}$. In each case the inner-product-preserving condition defines a closed set and each column having norm $1$ gives boundedness. Therefore $O(k)$, $U(k)$, and $Sp(k)$ are compact topological groups.
