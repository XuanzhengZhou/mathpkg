---
role: proof
locale: en
of_concept: haar-measure-existence
source_book: gtm018
source_chapter: "XI"
source_section: "58"
---

In view of 53.E and 53.F it is sufficient to construct a left invariant content which is not identically zero; 53.C implies that the induced measure is not identically zero and hence is a regular Haar measure.

Let $A$ be a fixed compact set with a non empty interior and let $\mathbf{N}$ be the class of all neighborhoods of the identity. For each $U$ in $\mathbf{N}$, we construct the set function $\lambda_U$, defined for all compact sets $C$ by $\lambda_U(C) = \frac{C:U}{A:U}$; since $C:U \leq (C:A)(A:U)$, it follows that $0 \leq \lambda_U(C) \leq C:A$ for every $C$ in $\mathbf{C}$. Theorem A shows that each $\lambda_U$ is almost a content; it fails to be a content only because it is not necessarily additive. We shall make use of the modern form of Cantor's diagonal process, i.e. of Tychonoff's theorem on the compactness of product spaces, to pick out a limit of the $\lambda_U$'s which has all their properties and is in addition additive.

If to each compact set $C$ we make correspond the closed interval $[0, C:A]$, and if we denote by $\Phi$ the Cartesian product (in the topological sense) of all these intervals, then $\Phi$ is a compact Hausdorff space whose points are real valued functions $\varphi$ defined on $\mathbf{C}$ such that for each $C$ in $\mathbf{C}$, $0 \leq \varphi(C) \leq C:A$. Each $\lambda_U$ is such a function, so that $\lambda_U \in \Phi$.

For each $U$ in $\mathbf{N}$ we denote by $\Lambda(U)$ the set of all those functions $\lambda_V$ for which $V \subset U$; i.e.

$$\Lambda(U) = \{\lambda_V : U \supset V \in \mathbf{N}\}.$$

If $\{U_1, \cdots, U_n\}$ is any finite class of neighborhoods of the identity, i.e. any finite subclass of $\mathbf{N}$, then $\bigcap_{i=1}^{n} U_i$ is also a neighborhood of the identity and, moreover,

$$\bigcap_{i=1}^{n} U_i \subset U_j, \quad j = 1, \cdots, n.$$

It follows that

$$\Lambda(\bigcap_{i=1}^{n} U_i) \subset \bigcap_{i=1}^{n} \Lambda(U_i),$$

and hence, since $\Lambda(U)$ always contains $\lambda_U$ and is therefore non empty, that the class of all sets of the form $\Lambda(U), U \in \mathbf{N}$, has the finite intersection property. The compactness of $\Phi$ implies that there is a point $\lambda$ in the intersection of the closures of all $\Lambda(U)$; i.e. there exists a function $\lambda$ on $\mathbf{C}$ such that for each $U$ in $\mathbf{N}$ and each $\epsilon > 0$, there is a $V$ in $\mathbf{N}$ with $V \subset U$ and $|\lambda(C) - \lambda_V(C)| < \epsilon$ for all $C$ in $\mathbf{C}$. This function $\lambda$ inherits all the properties of the $\lambda_U$ (non negativity, finiteness, monotonicity, subadditivity, left invariance, and the restricted additivity property), and it can be shown that, because of the limit process, $\lambda$ is in fact fully additive, hence a content. Since $\lambda(A) = 1$, $\lambda$ is not identically zero. The measure induced by this content (via the extension theorem) is the desired Haar measure.
