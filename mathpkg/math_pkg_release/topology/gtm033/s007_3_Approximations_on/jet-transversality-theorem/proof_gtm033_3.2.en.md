---
role: proof
locale: en
of_concept: jet-transversality-theorem
source_book: gtm033
source_chapter: "3"
source_section: "2. Transversality"
---

# Proof of the Jet Transversality Theorem (Theorem 2.8)

**Theorem 2.8 (Jet Transversality Theorem).** Let $M, N$ be $C^\infty$ manifolds without boundary, and let $A \subset J^r(M,N)$ be a $C^\infty$ submanifold. For $1 \leqslant r < s \leqslant \infty$, the set

$$\{f \in C^s(M,N) : j^r f \pitchfork A\}$$

is residual in $C^s_S(M,N)$. If $A$ is closed (as a subset), this set is also open.

*Proof.* The strategy is to apply the Parametric Transversality Theorem (Theorem 2.7) locally and then globalize.

**Local construction.** It suffices to consider the case $M = U \subset \mathbb{R}^m$ and $N = \mathbb{R}^n$, since the general case follows by using charts and partitions of unity.

Let $f: U \to \mathbb{R}^n$ be a $C^s$ map. We need to approximate $f$ in the strong $C^s$ topology by a map $h$ such that $j^r h$ is transverse to $A \cap J^r(U, \mathbb{R}^n)$.

Put $X = J_0^s(\mathbb{R}^m, \mathbb{R}^n)$, the space of $s$-jets at $0$. Every element of $X$ is the $s$-jet at $0$ of a unique map $g: \mathbb{R}^m \to \mathbb{R}^n$ whose coordinate maps $g_1, \ldots, g_n$ are polynomials of degree $\leqslant s$ in the coordinates of $\mathbb{R}^m$. We identify the elements of $X$ with such maps $g$.

Define $\alpha: X \to C_W^s(U, \mathbb{R}^n)$ by $g \mapsto f + g|_U$ and

$$F = j^r \circ \alpha: X \to C^{s-r}(U, J^r(U, \mathbb{R}^n)).$$

Then $F(0) = j^r f$.

**Verification that the evaluation map is transverse.** Make the natural identification

$$J^r(U, \mathbb{R}^n) = J_0^r(\mathbb{R}^m, \mathbb{R}^n) \times U.$$

Then the evaluation map of $F$ is

$$F^{\text{ev}}: J_0^s(\mathbb{R}^m, \mathbb{R}^n) \times U \to J_0^r(\mathbb{R}^m, \mathbb{R}^n) \times U$$

given by

$$(j_0^s(g), x) \mapsto (j_0^r(g + f), x).$$

The map

$$\beta: J_0^s(\mathbb{R}^m, \mathbb{R}^n) \to J_0^r(\mathbb{R}^m, \mathbb{R}^n), \quad j_0^s(g) \mapsto j_0^r(g + f)$$

is affine (it is the forgetful map from $s$-jets to $r$-jets, composed with translation by $j_0^r f$). The derivative of $\beta$ at any point is the "forgetful" linear map

$$J_0^s(\mathbb{R}^m, \mathbb{R}^n) \to J_0^r(\mathbb{R}^m, \mathbb{R}^n),$$

which is a linear surjection (since $s > r$). Therefore $F^{\text{ev}}$ is a $C^\infty$ submersion, and in particular transverse to any submanifold of $J_0^r(\mathbb{R}^m, \mathbb{R}^n) \times U$. In particular, $F^{\text{ev}}$ is transverse to $A$.

**Applying parametric transversality.** By the Parametric Transversality Theorem (Theorem 2.7), the set of parameters $g \in X = J_0^s(\mathbb{R}^m, \mathbb{R}^n)$ for which $F_g = j^r(f + g)$ is transverse to $A$ is residual (and open if $A$ is closed). Since $0 \in X$ corresponds to the original map $f$, we can find $g$ arbitrarily close to $0$ such that $j^r(f + g) \pitchfork A$. This gives a local $C^s$ approximation to $f$ with the desired transversality property.

**Globalization.** To extend from the local to the global setting, one uses the Globalization Theorem (Theorem 2.2). Define a mapping class $\mathcal{X}$ on $(M,N)$ by: for an open set $U \subset M$, $V \subset N$, and closed $L \subset U$,

$$\mathcal{X}_L(U,V) = \{h \in C^s(U,V) : j^r h \pitchfork A \text{ on } L\}.$$

The local construction above shows that $\mathcal{X}$ is rich (the local density and openness of jet transversality). By the Globalization Theorem 2.2, $\mathcal{X}_M(M,N)$ is dense and open in $C^s_S(M,N)$ when $A$ is closed, and residual in general.

QED
