---
role: proof
locale: en
of_concept: smooth-arc-polynomially-convex
source_book: gtm035
source_chapter: "12"
source_section: "12.4"
---
# Proof of Smooth Arcs are Polynomially Convex

**Statement.** Let $\gamma$ be a smooth arc in $\mathbb{C}^N$. Then $\gamma$ is polynomially convex and $P(\gamma) = C(\gamma)$.

**First part: $\gamma$ is polynomially convex.** We argue by contradiction. Suppose there exists $x^0 \in \hat{\gamma} \setminus \gamma$. By Step 1 in the proof of Theorem 12.1, there exists a polynomial $f$ in $z_1, \ldots, z_N$ such that $f(x^0) = 0$ and $f \neq 0$ on $\gamma$.

Since $\gamma$ is an arc, there exists an open simply connected neighborhood $U$ of $\gamma$ in $\mathbb{C}^N$ such that $f$ has an analytic logarithm on $U$. That is, there exists an analytic function $h$ defined on $U$ with $e^h = f$ on $U$. This is possible because $\gamma$ has topological dimension $1 < 2N$ for $N \geq 1$, and $f$ is nowhere zero on $\gamma$, so $\gamma$ can be enclosed in a simply connected domain where $\log f$ exists.

By Theorem 12.1, $A = \hat{\gamma} \setminus \gamma$ is a one-dimensional analytic subset of $\mathbb{C}^N \setminus \gamma$.

Choose $U_0$ open in $\mathbb{C}^N$ such that $x^0 \in U_0$ and $U_0 \cap \gamma = \emptyset$. Since $A$ is a one-dimensional analytic variety near $x^0$, we can find a one-dimensional analytic curve $\Sigma \subseteq A$ passing through $x^0$ on which $f$ is a non-constant analytic function with $f(x^0) = 0$. By the openness of analytic maps on one-dimensional varieties, the image $f(\Sigma)$ contains a neighborhood of $0$ in $\mathbb{C}$.

Now consider the set $Q = f(\Sigma)$ near $0$ and the preimage $f^{-1}(Q) \cap U$. Since $f$ has a logarithm $h$ on $U$, we have $f = e^h$ there, so $df/f = dh$ on $U$.

After canceling common boundaries along the triangles comprising $\Sigma$, we can arrange that $\partial\Sigma \subseteq U$. Then by the argument principle,

$$\frac{1}{2\pi i} \int_{\partial\Sigma} \frac{df}{f} = \frac{1}{2\pi i} \int_{\partial\Sigma} dh = 0,$$

since $h$ is analytic (hence $dh$ is exact) on $U \supseteq \partial\Sigma$. On the other hand, by the argument principle applied to the analytic function $f$ on the one-dimensional variety $\Sigma$, this integral must equal the number of zeros of $f$ on $\Sigma$ (counting multiplicity). Since $f(x^0) = 0$ with $x^0 \in \Sigma$, this number is at least $1$, yielding

$$\frac{1}{2\pi i} \int_{\partial\Sigma} \frac{df}{f} \geq 1,$$

a contradiction. Therefore no point $x^0 \in \hat{\gamma} \setminus \gamma$ can exist, and $\hat{\gamma} = \gamma$. Hence $\gamma$ is polynomially convex.

**Second part: $P(\gamma) = C(\gamma)$.** Since $\gamma$ is polynomially convex, $\gamma$ is the maximal ideal space of $\mathbf{P}(\gamma)$. Consequently, if $g$ is analytic on a neighborhood of $z_j(\gamma) \subseteq \mathbb{C}$ (for any coordinate projection $z_j$), then $g \circ z_j \in \mathbf{P}(\gamma)$. The argument used in Step 1 of the proof of Theorem 12.1 (showing $R(X) = C(X)$ in the one-dimensional case) adapts to the present setting: the algebra $\mathbf{P}(\gamma)$ separates points on $\gamma$ and contains enough analytic functions of each coordinate to approximate any continuous function. By the Stone-Weierstrass theorem for function algebras, $\mathbf{P}(\gamma) = C(\gamma)$. $\square$
