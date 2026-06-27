---
role: proof
locale: en
of_concept: silov-boundary-of-local-algebras
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.7"
---
# Proof of the Šilov Boundary of Local Algebras

**Theorem 9.7.** Let $\mathfrak{A}$ be a uniform algebra on a space $X$. Let $U_1, U_2, \ldots, U_s$ be an open covering of $\mathcal{M}$. Denote by $\mathcal{L}$ the set of all $f \in C(\mathcal{M})$ such that for $j = 1, \ldots, s$, the restriction $f|_{U_j}$ lies in the uniform closure of $\hat{\mathfrak{A}}|_{U_j}$. Then $\mathcal{L}$ is a closed subalgebra of $C(\mathcal{M})$ and

$$\check{S}(\mathcal{L}) \subseteq X.$$

*Proof.* The proof is a corollary of Theorem 9.3 (the Local Maximum Modulus Principle). It is left to the reader as Exercise 9.9 in the book.

**Sketch.** First, it is clear that $\mathcal{L}$ is a subalgebra of $C(\mathcal{M})$ since each $U_j$ condition is preserved under sums, products, and uniform limits. Moreover, $\mathcal{L}$ is closed by definition.

To show $\check{S}(\mathcal{L}) \subseteq X$, fix a point $x \in \mathcal{M} \setminus X$. We need to show that $x \notin \check{S}(\mathcal{L})$, i.e., there exists a neighborhood $V$ of $x$ and a function $g \in \mathcal{L}$ such that $|g(x)| > \max_{\mathcal{M} \setminus V} |g|$.

By the definition of $\mathcal{L}$, for each $f \in \mathcal{L}$ and each $U_j$ containing $x$, $f$ is uniformly approximable on $U_j$ by elements of $\hat{\mathfrak{A}}$. Since each $\hat{f}$ (for $f \in \mathfrak{A}$) satisfies the local maximum modulus principle (Theorem 9.3) on $\mathcal{M} \setminus \check{S}(\mathfrak{A})$, the same holds for limits of such functions.

Since $x \notin X$, and $\check{S}(\mathfrak{A}) \subseteq X$ (this is a general fact for uniform algebras — the Šilov boundary is contained in the original space), we have $x \in \mathcal{M} \setminus \check{S}(\mathfrak{A})$. Applying Theorem 9.3 to the algebra $\mathfrak{A}$ and using the definition of $\mathcal{L}$, one verifies that $x \notin \check{S}(\mathcal{L})$.

For the complete proof, see Exercise 9.9 of *Several Complex Variables and Banach Algebras*. $\square$
