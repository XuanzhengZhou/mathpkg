---
role: proof
locale: en
of_concept: stolzenberg-no-analytic-disk-example
source_book: gtm035
source_chapter: "24"
source_section: "24.1"
---
# Proof of Stolzenberg Example: Rational Hull Without Analytic Disks

**Theorem 24.1.** There exists $S$ such that $h_r(X_S) \neq X_S$ and $h_r(X_S)$ contains no analytic disk.

**Proof.** The proof proceeds via three claims.

**Construction of $X_S$.** Let $S$ be a closed subset of $\{|\zeta| \leq 1\}$ that contains the unit circle. Denote by $D_1, D_2, \ldots$ the components of the complement of $S$ in $\{|\zeta| < 1\}$. For each $i$, put

$$H_i = \{(z, w) \in \mathbb{C}^2 : z \in D_i, |w| = 1\}$$

and

$$K_i = \{(z, w) \in \mathbb{C}^2 : |z| = 1, w \in D_i\}.$$

Let $\Delta^2$ denote the closed bidisk and $\partial \Delta^2$ its topological boundary. Define

$$X_S = \partial \Delta^2 \setminus \bigcup_{i=1}^{\infty} (H_i \cup K_i).$$

Equivalently,

$$X_S = \{(z, w) : z \in S, |w| = 1\} \cup \{(z, w) : |z| = 1, w \in S\}.$$

**Claim 1.** Assume that $S$ has no interior. Then $h_r(X_S)$ contains no analytic disk.

*Proof of Claim 1.* Suppose that $E$ is an analytic disk contained in $h_r(X_S)$. Either $z$ or $w$ is not constant on $E$. Suppose that $z$ is not constant. Then $z(E)$ contains interior in $\mathbb{C}$ and so the $z$-projection of $h_r(X_S)$ has interior points. On the other hand, this $z$-projection is contained in $S$. To see this, consider $(z_0, w_0) \in h_r(X_S)$. If $z_0 \notin S$, then $z - z_0 \neq 0$ on $S$. But $z - z_0$ vanishes at $(z_0, w_0)$, and since $h_r(X_S)$ is rationally convex, $(z_0, w_0)$ cannot belong to $h_r(X_S)$. This contradiction shows that $z_0 \in S$. Hence the $z$-projection of $h_r(X_S)$ is contained in $S$, contradicting that $S$ has no interior. The case where $w$ is not constant is similar. Thus $h_r(X_S)$ contains no analytic disk. $\square$

**Claim 2.** Fix $n$ and let $V$ be a neighborhood of $\bigcup_{i=1}^{n} (H_i \cup K_i)$. Let $Y_n = \bigcup_{i=1}^{n} (H_i \cup K_i)$. If a point $p$ lies in $h_r(X_S)$ but outside $V$, then $|f(p)| \leq \sup_{Y_n} |f|$ whenever $f$ is analytic on a neighborhood of $X_S \cup V$.

*Proof of Claim 2.* By the local maximum modulus principle applied to $V$, we have

$$|f(p)| \leq \max_{V \cap \partial \Delta^2} |f| \leq \sup_{Y_n} |f|,$$

where the sup is taken over $\bigcup_{i=1}^{n} (H_i \cup K_i)$, as claimed. $\square$

**Claim 3.** There exists a sequence $D_1, D_2, \ldots$ of disjoint open subsets of $\{|\zeta| < 1\}$ such that, if we put

$$S = \{|\zeta| \leq 1\} \setminus \bigcup_{i=1}^{\infty} D_i,$$

and define $H_i, K_i$ as earlier, then $S$ has no interior and $(0, 0) \in h_r(X_S)$.

*Proof of Claim 3.* We choose a countable dense subset $\{a_j\}$ of $\{|\zeta| < 1\}$ avoiding $0$. We construct disjoint open disks $D_1, D_2, \ldots$ contained in $\{|\zeta| < 1\}$ such that for each $n$:

(4) $a_j \in \bigcup_{i=1}^{n} D_i$ for $1 \leq j \leq n$, and

(5) $0 \notin \widehat{Y_n}$, where $Y_n = \bigcup_{i=1}^{n} (H_i \cup K_i)$.

**Base case $n = 1$:** Fix $r_1$ with $2r_1/|a_1|^2 < 1$. Put $G(z, w) = (z - a_1)(w - a_1)/a_1^2$. Put $D_1 = \{|\zeta - a_1| < r_1\}$. Then $G(0, 0) = 1$ and, for $(z, w) \in H_1 \cup K_1$, $|G(z, w)| \leq 2r_1/|a_1|^2 < 1$. So (4) and (5) hold for $n = 1$.

**Inductive step:** Suppose that disjoint open disks $D_1, D_2, \ldots, D_s$ have been chosen satisfying (4) and (5) for $n = 1, \ldots, s$. Consider $a_{s+1}$. If $a_{s+1} \in \bigcup_{i=1}^{s} D_i$, set $D_{s+1} = \emptyset$. Otherwise, choose $r > 0$ small and then $\lambda > 0$ large with $2r \lambda/|a|^2 < 1$ where $a = a_{s+1}$. Choose an integer $k$ large and define

$$Q(z, w) = \left( \frac{(z - a)(w - a)}{\lambda |a|^2} \right)^k.$$

Select $D_{s+1} = \{|\zeta - a| < r\}$ disjoint from $\bigcup_{i=1}^{s} D_i$. Then $|Q(0)| > 1$ and on $\bigcup_{i=1}^{s} (H_i \cup K_i)$,

$$|Q|^2 \leq \frac{(1/2)^k \cdot 4}{|a|^2} < 1,$$

so $0 \notin \widehat{Y_n}$ for $n = 1, 2, \ldots, s$. On $H_{s+1} \cup K_{s+1}$, either $|z - a| < r$ or $|w - a| < r$, so $|Q| < \lambda^k \cdot 2r/|a|^2 < 1$. Thus $0 \notin \widehat{Y_{s+1}}$, and (5) holds for $n = s + 1$. By the choice of $D_{s+1}$, $a_{s+1} \in \bigcup_{i=1}^{s+1} D_i$.

By induction, the desired sequence $\{D_i\}$ exists satisfying (4) and (5) for each $n$. Put $S = \{|\zeta| \leq 1\} \setminus \bigcup_{i=1}^{\infty} D_i$.

Because of Claim 2 together with (5), we have that $0 \in h_r(X_S)$. Also, $\bigcup_{i=1}^{\infty} D_i$ contains each $a_j$, and hence $S$ has no interior. This gives Claim 3. $\square$

Finally, Claim 1 shows that $h_r(X_S)$ contains no analytic disk, while Claim 3 shows $h_r(X_S) \neq X_S$. This proves Theorem 24.1. $\square$
