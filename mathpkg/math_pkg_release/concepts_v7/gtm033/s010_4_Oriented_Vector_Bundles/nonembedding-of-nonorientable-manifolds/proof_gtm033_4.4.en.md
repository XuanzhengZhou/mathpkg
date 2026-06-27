---
role: proof
locale: en
of_concept: nonembedding-of-nonorientable-manifolds
source_book: gtm033
source_chapter: "4"
source_section: "4. Oriented Vector Bundles"
---

# Proof of Theorem 4.7 (Nonembedding Theorem for Nonorientable Manifolds)

**Theorem 4.7.** A compact nonorientable $n$-manifold without boundary cannot be embedded in a simply connected $(n+1)$-manifold. In particular, projective $2n$-space $\mathbb{P}^{2n}$ does not embed in $\mathbb{R}^{2n+1}$ for $n \geq 1$.

**Proof of the first statement.** Let $M$ be a compact nonorientable $n$-manifold with $\partial M = \varnothing$, and let $N$ be a simply connected $(n+1)$-manifold. Suppose, for contradiction, that there exists an embedding $f: M \hookrightarrow N$.

A simply connected manifold is always orientable (its orientation double cover would be a nontrivial covering if it were nonorientable, contradicting $\pi_1(N) = 0$). Hence $N$ is orientable.

Since $M$ is compact and $N$ is Hausdorff, the image $f(M) \subset N$ is a closed subset. Moreover, $f(M)$ is a closed connected submanifold of codimension $1$ (since $\dim M = n$ and $\dim N = n+1$), with $\partial f(M) = f(\partial M) = \varnothing$ and $\partial N = \varnothing$.

Now apply Theorem 4.6 (or rather its contrapositive given by Theorem 4.5): Since $N$ is simply connected, $f(M)$ is a closed connected codimension-$1$ submanifold, and by the Jordan-Brouwer separation theorem (or more precisely, by the fact that a closed connected hypersurface in $\mathbb{R}^{n+1}$ separates it), $f(M)$ separates $N$. Wait---the argument is more direct: embed $M$ into $N$. Then by Theorem 4.5 applied to the pair $(N, f(M))$, if $f(M)$ separates $N$, then $f(M)$ must be orientable, contradicting the hypothesis that $M$ is nonorientable. Therefore $f(M)$ does not separate $N$.

But a compact connected hypersurface in a simply connected manifold always separates (this is a consequence of Alexander duality or the Jordan-Brouwer separation theorem generalized to manifolds). Thus we obtain a contradiction: $f(M)$ must separate $N$ (by topological reasons), yet it cannot separate $N$ (because it would then be orientable by Theorem 4.5). Hence no such embedding exists.

**Alternative direct argument.** Together with Theorems 4.6 and 4.5, we reason as follows: if $M$ embeds in $N$, then $f(M)$ would be a closed connected codimension-$1$ submanifold of a simply connected orientable manifold. Any such submanifold separates $N$ (by the generalized Jordan separation theorem). But if $f(M)$ separates $N$, then Theorem 4.5 implies $f(M)$ is orientable, contradicting the nonorientability of $M$. This proves the first statement.

**Proof of the second statement (projective space).** We show that $\mathbb{P}^{2n}$ is nonorientable for $n \geq 1$. Consider $\mathbb{P}^{2n}$ as the identification space of the sphere $S^{2n}$ under the antipodal map $A: S^{2n} \to S^{2n}$, $A(x) = -x$. Let $p: S^{2n} \to \mathbb{P}^{2n}$ be the canonical projection.

The antipodal map $A$ on $S^{2n}$ is the restriction of the linear map $-\operatorname{id}$ on $\mathbb{R}^{2n+1}$. Since $\dim \mathbb{R}^{2n+1} = 2n+1$ is odd, $\det(-\operatorname{id}) = (-1)^{2n+1} = -1 < 0$, so $A$ is orientation-reversing.

Suppose $\mathbb{P}^{2n}$ were orientable, with an orientation $\omega$. Then $S^{2n}$, being the oriented double cover of $\mathbb{P}^{2n}$, would inherit a unique orientation $\theta$ such that the derivative $T_x p: T_x S^{2n} \to T_{p(x)} \mathbb{P}^{2n}$ maps the orientation $\theta_x$ to $\omega_{p(x)}$ for every $x \in S^{2n}$. Since the fibre of $p$ over each point consists of the pair $\{x, -x\}$, and $p \circ A = p$, we would have $T_x(p \circ A)(\theta_x) = \omega_{p(x)}$ as well. But $T_x(p \circ A) = T_{A(x)}p \circ T_x A$. Since $T_{A(x)}p$ maps $\theta_{A(x)}$ to $\omega_{p(x)}$, the orientation $\theta$ would have to satisfy $\theta_{A(x)} = T_x A(\theta_x)$. In other words, $\theta$ would be invariant under the antipodal map $A$. But $A$ is orientation-reversing, so an $A$-invariant orientation cannot exist: if $\theta$ is any orientation of $S^{2n}$, then $A^*\theta$ is the opposite orientation $-\theta$. Hence $\mathbb{P}^{2n}$ cannot be orientable.

Since $\mathbb{R}^{2n+1}$ is simply connected, the first part of the theorem implies that the compact nonorientable $2n$-manifold $\mathbb{P}^{2n}$ cannot embed in $\mathbb{R}^{2n+1}$.

**Remark.** The case $n = 1$ gives the familiar result that the real projective plane $\mathbb{P}^2$ does not embed in $\mathbb{R}^3$. Theorem 4.7 generalizes this to all even-dimensional real projective spaces.

QED
