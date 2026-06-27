---
role: proof
locale: en
of_concept: linking-number-theorem
source_book: gtm035
source_chapter: "Chapter 22"
source_section: "22.6"
---
# Proof of Linking Number Theorem for Polynomial Hulls

**Theorem 22.6 (Linking Number Theorem for Polynomial Hulls).** Let $K$ be a compact polynomially convex set in $\mathbb{C}^n$ ($n \geq 2$) and let $V$ be a compact one-dimensional analytic subset of $\mathbb{C}^n \setminus K$. Then the linking number of $V$ with $K$ is zero.

Equivalently, $V$ is homologous to zero in $\mathbb{C}^n \setminus K$, i.e., $[V] = 0$ in $H_2(\mathbb{C}^n \setminus K; \mathbb{Z})$.

**Proof.** The proof uses Theorem 22.2 (Andreotti-Narasimhan) and the Oka-Weil approximation theorem. We follow the approach of Alexander [Al3, Al4], which uses a construction suggested by J.-P. Rosay.

By Lemma 22.5, since $K$ is polynomially convex, there exists a Runge domain $\Omega$ with $K \subset \Omega \subset \mathbb{C}^n \setminus V$. (More precisely, for any open neighborhood $U$ of $K$ disjoint from $V$, we can find a Runge domain $\Omega$ such that $K \subset \Omega \subset U$.)

Since $\Omega$ is Runge, Theorem 22.2 (Andreotti-Narasimhan) implies that

$$H_k(\Omega; \mathbb{Z}) = 0 \quad \text{for } k \geq n.$$

In particular, for $n \geq 3$, we have $H_2(\Omega; \mathbb{Z}) = 0$. For $n = 2$, the Andreotti-Narasimhan theorem gives $H_k(\Omega; \mathbb{Z}) = 0$ for $k \geq 2$, so again $H_2(\Omega; \mathbb{Z}) = 0$.

Consider the inclusion $i : \Omega \hookrightarrow \mathbb{C}^n \setminus K$. The cycle $V$ is contained in $\mathbb{C}^n \setminus K$. Using the Bochner-Martinelli kernel and approximation techniques (or more directly using the fact that $V$ is contained in a Runge domain whose complement contains $K$), one shows that $V$ is homologous in $\mathbb{C}^n \setminus K$ to a cycle $\Gamma$ contained in $\Omega$.

More precisely, for a sufficiently small tubular neighborhood $N$ of $V$, there exists a smooth $(2n-3)$-form $\omega$ on $\mathbb{C}^n \setminus K$ (the Bochner-Martinelli form) that is $d$-closed and whose restriction to any sphere around $V$ gives the linking number. By pushing the integration cycle from $\partial N$ into $\Omega$ using the fact that $\Omega$ is a Runge domain containing $K$ and the Oka-Weil theorem, we obtain the homologous cycle $\Gamma$ in $\Omega$.

Since $H_2(\Omega; \mathbb{Z}) = 0$, the cycle $\Gamma$ is homologous to zero in $\Omega$, and hence $V$ is homologous to zero in $\mathbb{C}^n \setminus K$.

Thus the linking number of $V$ with $K$ vanishes, i.e., $[V] = 0$ in $H_2(\mathbb{C}^n \setminus K; \mathbb{Z})$.

For the refined statement using Theorem 22.3 (Forstneric), when $n \geq 3$ one additionally has that $\pi_2(\mathbb{C}^n \setminus K) = 0$, which implies that any 2-sphere in $\mathbb{C}^n \setminus K$ bounds a 3-ball, strengthening the vanishing of linking.
