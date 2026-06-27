---
role: proof
locale: en
of_concept: fundamental-theorem-of-galois-theory
source_book: gtm028
source_chapter: "II"
source_section: "§7. The fundamental theorem of Galois theory"
---

It is clear that $H \subset G(K/L)$. Let $n$ denote the order of the group $H$. Suppose that it has already been proved that

\[
[K:L] \leq n. \tag{1}
\]

Since $K$ is a normal and separable extension of $L$, we have, by Theorem 16, Corollary (§6), that the order of $G(K/L)$ is equal to $[K:L]$, hence is $\leq n$, by (1). On the other hand, $H$ is a subgroup of $G(K/L)$ and has order $n$. It follows at once that $H = G(K/L)$, as asserted.

It remains to prove the inequality (1). Let $\alpha_1, \alpha_2, \cdots, \alpha_{n+1}$ be arbitrary $n+1$ elements of $K$. We have to show that these elements are linearly dependent over $L$. In the proof we may assume that no $\alpha_i$ is zero. Let $\tau_1, \tau_2, \cdots, \tau_n$ be the elements of the group $H$. We find a set of $n+1$ elements $c_j$ in $K$, not all zero, such that the following system of $n$ homogeneous equations is satisfied:

\[
\sum_{j=1}^{n+1} c_j(\alpha_j \tau_i) = 0, \quad i = 1, 2, \cdots, n. \tag{2}
\]

Among all such sets $\{c_1, c_2, \cdots, c_{n+1}\}$ we choose one with the smallest number of non-zeros. We assume that $\{c_1, c_2, \cdots, c_{n+1}\}$ has already been chosen in this fashion. Let, say, $c_1, c_2, \cdots, c_r \neq 0$, $c_{r+1} = c_{r+2} = \cdots = c_{n+1} = 0$. Then $r \geq 2$, for if $r = 1$, then $\alpha_1 \tau_i = 0$ for all $i$, whence $\alpha_1 = 0$, contrary to our assumption. Moreover, we may assume that $c_1 = 1$, since we may divide each of the equations (2) by $c_1$ (and the resulting set will again be a solution of (2) with $r$ non-zero elements). We have therefore:

\[
\sum_{j=1}^{r} c_j(\alpha_j \tau_i) = 0, \quad i = 1, 2, \cdots, n, \quad c_1 = 1. \tag{3}
\]

We now assert that all the $c_j$ belong to the fixed field $L$ of $H$. Let us prove for instance that $c_j \tau_1 = c_j$. If we apply to (3) the automorphism $\tau_1$ of $K$ we find

\[
\sum_{j=1}^{r} (c_j \tau_1)(\alpha_j \tau_i \tau_1) = 0, \quad i = 1, 2, \cdots, n. \tag{4}
\]

The $n$ products $\tau_i \tau_1$ give again all the elements of the finite group $H$. Hence we have

\[
\sum_{j=1}^{r} (c_j \tau_1)(\alpha_j \tau_i) = 0, \quad i = 1, 2, \cdots, n. \tag{5}
\]

Subtracting (5) from (3) and taking into account that $c_1 = c_1 \tau_1 = 1$, we find

\[
\sum_{j=2}^{r} (c_j \tau_1 - c_j)(\alpha_j \tau_i) = 0, \quad i = 1, 2, \cdots, n.
\]

Here we have a set of $n$ relations similar to (2), but the number of terms in each of these relations is less than $r$. Hence, by our choice of the set $\{c_1, c_2, \cdots, c_r, 0, 0, \cdots, 0\}$, we must have $c_j \tau_1 = c_j$, $j = 2, 3, \cdots, r$. In a similar fashion we can prove that $c_j \tau_i = c_j$, $j = 2, 3, \cdots, r$, $i = 1, 2, \cdots, n$.

Thus all $c_j$ belong to $L$, the fixed field of $H$. Taking $i = 1$ in (3) and noting that $\tau_1$ is the identity, we obtain:

\[
\sum_{j=1}^{r} c_j \alpha_j = 0,
\]

which is a non-trivial linear relation with coefficients in $L$ among the $\alpha_j$. Since the $\alpha_1, \cdots, \alpha_{n+1}$ were arbitrary $n+1$ elements of $K$, it follows that $[K:L] \leq n$. This completes the proof.
