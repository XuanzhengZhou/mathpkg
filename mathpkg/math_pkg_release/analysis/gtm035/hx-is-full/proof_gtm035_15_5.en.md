---
role: proof
locale: en
of_concept: hx-is-full
source_book: gtm035
source_chapter: "15"
source_section: "15.5"
---
# Proof that $\mathcal{H}(X)$ is a Full Subalgebra

**Lemma 15.5.** Let $X$ be a compact polynomially convex subset of $\mathbb{C}^n$. Then $\mathcal{H}(X)$ is a full subalgebra of $C(X)$.

Recall:
- $\mathcal{H}(X) = \{f \in C(X) \mid \exists \text{ neighborhood } U \text{ of } X \text{ and } \exists F \in \mathcal{H}(U) \text{ with } F|_X = f\}$.
- $\mathcal{L}$ is full if (a) $\eta$ maps $\mathcal{L}^{-1}$ onto $H^1(X, \mathbb{Z})$, and (b) $x \in \mathcal{L}^{-1}$ with $\eta(x) = 0$ implies $x \in \exp \mathcal{L}$.

## Proof

**Verification of condition (a): Surjectivity onto $H^1(X, \mathbb{Z})$.**

Fix $\gamma \in H^1(X, \mathbb{Z})$. By definition of the Čech cohomology limit group, there exists a covering $\mathcal{U} = \{U_\alpha\}_{\alpha=1}^s$ and a 1-cocycle $h_{\alpha\beta} \in \mathbb{Z}$ on $\mathcal{U}$ such that $K^{\mathcal{U}}([h]) = \gamma$. Since $X$ is compact, we may take $\mathcal{U}$ to be a finite open covering.

Choose smooth functions $g_\alpha \in C^\infty(U_\alpha)$ (after possibly shrinking $U_\alpha$ to a neighborhood $N$ of $X$) such that

$$\frac{1}{2\pi i}(g_\beta - g_\alpha) = h_{\alpha\beta} \quad \text{in } U_\alpha \cap U_\beta. \tag{7}$$

(These $g_\alpha$ are constructed using a partition of unity, as in the proof of Theorem 15.4.)

By Lemma 7.4, there exists a $p$-polyhedron $\Pi$ with $X \subset \Pi \subset N$. By Theorem 7.6, there exists a neighborhood $W$ of $\Pi$ and $u \in C^\infty(W)$ such that

$$\bar{\partial} u = \bar{\partial} g_\alpha \quad \text{in } W \cap U_\alpha. \tag{8}$$

Set $V_\alpha = U_\alpha \cap W$ for $1 \leq \alpha \leq s$. Put $\mathcal{V} = \{V_\alpha \cap X \mid 1 \leq \alpha \leq s\}$.

Define $g'_\alpha = g_\alpha - u$ in $V_\alpha$. Then by (8), $g'_\alpha \in \mathcal{H}(V_\alpha)$ (holomorphic, since $\bar{\partial} g'_\alpha = 0$). Moreover, from (7),

$$\frac{1}{2\pi i}(g'_\beta - g'_\alpha) = \frac{1}{2\pi i}(g_\beta - g_\alpha) = h_{\alpha\beta} \quad \text{in } V_\alpha \cap V_\beta.$$

Now define a function $f$ in $\bigcup_\alpha V_\alpha$ by

$$f = e^{g'_\alpha} \quad \text{in } V_\alpha.$$

On $V_\alpha \cap V_\beta$, the two definitions agree:

$$e^{g'_\beta} = e^{g'_\alpha + 2\pi i h_{\alpha\beta}} = e^{g'_\alpha},$$

since $h_{\alpha\beta} \in \mathbb{Z}$. Hence $f$ is well-defined and holomorphic in $\bigcup_\alpha V_\alpha$. Consequently, $f|_X \in \mathcal{H}(X)$ and in fact $f|_X \in (\mathcal{H}(X))^{-1}$. Finally,

$$\eta(f) = K^{\mathcal{U}}([h]) = \gamma.$$

Thus condition (a) holds.

**Verification of condition (b): Kernel equals $\exp \mathcal{H}(X)$.**

Now fix $f \in (\mathcal{H}(X))^{-1}$ with $\eta(f) = 0$. Let $F$ be a holomorphic function in a neighborhood of $X$ such that $F|_X = f$.

Since $\eta(f) = 0$, by the construction of $\eta$, the cocycle associated to $f$ (via admissible local logarithms) is a coboundary. This means there exists a covering and smooth local logarithms $g_\alpha$ of $F$ with $g_\beta - g_\alpha = 2\pi i (H_\beta - H_\alpha)$ for a 0-cochain $H$ with integer values. Then $g_\alpha - 2\pi i H_\alpha$ patch together to give a globally defined holomorphic function $G$ in a neighborhood of $X$, satisfying

$$F = e^G \quad \text{near } X.$$

Thus $f = F|_X = e^{G|_X}$, and $G|_X \in \mathcal{H}(X)$. Therefore $f \in \exp \mathcal{H}(X)$, verifying condition (b).

Both conditions of Definition 15.3 are satisfied, so $\mathcal{H}(X)$ is a full subalgebra of $C(X)$.
