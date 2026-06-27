---
role: proof
locale: en
of_concept: intersection-of-maximal-subspaces-containing-subspace
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Intersection of All Maximal Subspaces Containing a Given Subspace

Let $E$ be a vector space over $\mathbb{K}$ and let $N$ be a proper linear subspace of $E$. Denote by $\mathcal{M}(N)$ the family of all maximal linear subspaces of $E$ that contain $N$.

**Theorem 21.8.** $\bigcap_{M \in \mathcal{M}(N)} M = N$.

*Proof.*

The inclusion $N \subset \bigcap \mathcal{M}(N)$ is trivial, since every $M \in \mathcal{M}(N)$ contains $N$ by definition. To establish the reverse inclusion, suppose $x \in E \setminus N$; we must exhibit a maximal linear subspace $M$ containing $N$ but not $x$.

Consider the quotient vector space $E/N$ and the canonical projection $\pi: E \to E/N$. Since $x \notin N$, the coset $\pi(x) = x + N$ is a nonzero vector in $E/N$. Choose a basis $\mathcal{B}$ for $E/N$ that includes $\pi(x)$. Let $L$ be the linear span of all basis vectors in $\mathcal{B} \setminus \{\pi(x)\}$. Then $L$ is a linear subspace of $E/N$ with codimension 1, hence $L$ is a maximal linear subspace of $E/N$, and $\pi(x) \notin L$ by construction.

Define $M = \pi^{-1}(L) = \{y \in E : \pi(y) \in L\}$. Then $M$ is a linear subspace of $E$ containing $\ker \pi = N$. Since $\pi$ induces an isomorphism $E/M \cong (E/N)/L$ and $L$ is maximal in $E/N$, $(E/N)/L$ is one-dimensional, so $E/M$ is one-dimensional; by Theorem 21.3, $M$ is a maximal linear subspace of $E$. Moreover, $\pi(x) \notin L$, so $x \notin M$.

Thus for every $x \notin N$, there exists $M \in \mathcal{M}(N)$ with $x \notin M$, which proves $\bigcap \mathcal{M}(N) \subset N$.

**Alternative argument via linear forms:** For $x \notin N$, the coset $\pi(x)$ is nonzero in $E/N$. Let $\varphi: E/N \to \mathbb{K}$ be a linear form with $\varphi(\pi(x)) \neq 0$ (for instance, the coordinate functional corresponding to $\pi(x)$ in a basis of $E/N$). Then $f = \varphi \circ \pi$ is a linear form on $E$ with $f(x) \neq 0$, and $f|_N = 0$. By Theorem 21.3, $M = \ker f$ is a maximal linear subspace, $M \supset N$, and $x \notin M$.
