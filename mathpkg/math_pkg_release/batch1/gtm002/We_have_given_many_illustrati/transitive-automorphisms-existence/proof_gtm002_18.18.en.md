---
role: proof
locale: en
of_concept: transitive-automorphisms-existence
source_book: gtm002
source_chapter: "18"
source_section: "18"
---
We have shown that $\bigcap_{i,j} E_{ij}$ is a dense $G_\delta$ in $M$, and therefore nonempty. It remains to show that any $T \in \bigcap_{i,j} E_{ij}$ is transitive.

For $T \in \bigcap_{i,j} E_{ij}$, we have by definition
$$U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset$$
for all $i$ and $j$. Hence for each $j$, the set
$$G_j = \bigcup_{k=1}^{\infty} T^{-k} U_j$$
intersects every basic open set $U_i$, so $G_j$ is open and dense in the square.

Since $X$ (the closed unit square) is a complete metric space, the Baire category theorem applies, and
$$\bigcap_{j=1}^{\infty} G_j \neq \emptyset.$$

For any point $x$ in this intersection, the positive semiorbit $\{x, Tx, T^2x, \ldots\}$ meets every basic open set $U_j$ infinitely often (since $x \in G_j$ means $T^k x \in U_j$ for some $k \geq 1$). Therefore the positive semiorbit of $x$ is dense in $X$, which means the full orbit $\{T^n x : n = 0, \pm 1, \pm 2, \ldots\}$ is also dense in $X$. Hence $T$ is transitive.

Thus $\bigcap_{i,j} E_{ij}$ is contained in the set of transitive automorphisms. Since $\bigcap_{i,j} E_{ij}$ is a dense $G_\delta$ in $M$, the set of transitive measure-preserving automorphisms contains a dense $G_\delta$ and is therefore nonempty. This establishes the existence of transitive automorphisms of the closed unit square.

Moreover, since $M$ is a complete metric space and we have exhibited a dense $G_\delta$ of transitive automorphisms, transitivity is the generic (typical) property in the sense of Baire category among measure-preserving automorphisms.
