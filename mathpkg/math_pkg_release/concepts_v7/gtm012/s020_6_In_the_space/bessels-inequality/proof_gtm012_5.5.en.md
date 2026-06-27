---
role: proof
locale: en
of_concept: bessels-inequality
source_book: gtm012
source_chapter: "5"
source_section: "§5. Orthogonal expansions"
---

# Proof of Bessel's Inequality

**Bessel's Inequality.** Let $H$ be a Hilbert space and let $(e_n)$ be an orthonormal set in $H$. For any $u \in H$ and any finite collection of indices,

$$\sum_{n=1}^{N} |(u, e_n)|^2 \leq \|u\|^2.$$

For a doubly-indexed orthonormal set, the symmetric form is

$$\sum_{n=-N}^{N} |(u, e_n)|^2 \leq \|u\|^2.$$

*Proof.* Let $(e_n)$ be an orthonormal set in $H$ (not necessarily a basis). Fix $N$ and consider the subspace $H_N = \operatorname{span}\{e_1, \ldots, e_N\}$. Define the orthogonal projection of $u$ onto $H_N$:

$$u_N = \sum_{n=1}^{N} (u, e_n) e_n.$$

Observe that $u_N \in H_N$ and that for each $k = 1, \ldots, N$,

$$(u - u_N, e_k) = (u, e_k) - \sum_{n=1}^{N} (u, e_n)(e_n, e_k) = (u, e_k) - (u, e_k) = 0.$$

Hence $u - u_N \perp H_N$. Therefore, by the Pythagorean theorem in inner product spaces,

$$\|u\|^2 = \|u_N\|^2 + \|u - u_N\|^2.$$

Since $\|u - u_N\|^2 \geq 0$, it follows that

$$\|u_N\|^2 \leq \|u\|^2.$$

Now, by orthonormality of the $e_n$,

$$\|u_N\|^2 = \left( \sum_{n=1}^{N} (u, e_n) e_n, \sum_{m=1}^{N} (u, e_m) e_m \right) = \sum_{n=1}^{N} |(u, e_n)|^2.$$

Combining these results,

$$\sum_{n=1}^{N} |(u, e_n)|^2 = \|u_N\|^2 \leq \|u\|^2.$$

This is Bessel's inequality for a singly-indexed orthonormal set. The same argument applied to the symmetric subspace $H_N = \operatorname{span}\{e_{-N}, \ldots, e_N\}$ yields the doubly-indexed form

$$\sum_{n=-N}^{N} |(u, e_n)|^2 \leq \|u\|^2. \quad \square$$

**Remark.** When $(e_n)$ is an *orthonormal basis* (i.e., a complete orthonormal set), the sequence of partial sums $u_N$ converges to $u$, the remainder $\|u - u_N\| \to 0$, and Bessel's inequality becomes Bessel's *equality*: $\|u\|^2 = \sum_{n=1}^{\infty} |(u, e_n)|^2$. For a general orthonormal set (not necessarily complete), only the inequality holds.
