---
role: proof
locale: en
of_concept: lemma-2-3-transversality-compact
source_book: gtm033
source_chapter: "3"
source_section: "2. Transversality"
---

# Proof of Lemma 2.3: Dense and Open Transversality on Compact Sets

**Lemma 2.3.** Let $K$ be a compact set in a manifold $U$, $\mathbb{R}^a \subset \mathbb{R}^n$ a linear subspace, and $V \subset \mathbb{R}^n$ an open set. Then

$$\bigcap_K^{\,r}(U,V; \mathbb{R}^a \cap V)$$

is dense and open in $C^r_W(U,V)$, $1 \leqslant r \leqslant \infty$.

*Proof.* **Openness:** Let $f \in \bigcap_K^{\,r}(U,V; \mathbb{R}^a \cap V)$. For each $x \in K$, transversality of $f$ to $\mathbb{R}^a$ at $x$ is an open condition in the $C^1$ topology (it depends only on $Df_x$ and the positions of $f(x)$ relative to $\mathbb{R}^a$). Since $K$ is compact, there exists a weak $C^r$ neighborhood of $f$ consisting entirely of maps transverse to $\mathbb{R}^a$ on $K$. Thus the set is open.

**Density:** Given $f \in C^r(U,V)$ and a weak $C^r$ neighborhood $\mathcal{N}$ of $f$, we need to find $g \in \mathcal{N} \cap \bigcap_K^{\,r}(U,V; \mathbb{R}^a \cap V)$.

Consider the map $\Phi: K \times \mathbb{R}^{n-a} \to \mathbb{R}^n$ defined by $\Phi(x, v) = f(x) + v$, where we identify $\mathbb{R}^{n-a}$ with a complementary subspace to $\mathbb{R}^a$ in $\mathbb{R}^n$. For each $x \in K$, the derivative of $\Phi$ with respect to $v$ is an isomorphism onto the complement of $\mathbb{R}^a$. By the inverse function theorem and compactness of $K$, there exists an open cover of $K$ by coordinate neighborhoods $U_i$ and small vectors $v_i \in \mathbb{R}^{n-a}$ such that the perturbed maps $f(x) + \sum \lambda_i(x) v_i$ are transverse to $\mathbb{R}^a$ on $K$. Choosing the $v_i$ sufficiently small ensures the perturbed map lies in $\mathcal{N}$. Near $K$, this gives the required $g \in \mathcal{N}$.

More formally: pick a finite set of points $\{x_j\}$ in $K$ and vectors $\{v_j\}$ in $\mathbb{R}^{n-a}$ such that translating $f$ by a linear combination of the $v_j$ (via a partition of unity subordinate to small neighborhoods of the $x_j$) makes the resulting map transverse to $\mathbb{R}^a$ on $K$. The size of the perturbation tends to zero with the size of the $v_j$, so we stay within $\mathcal{N}$.

QED
