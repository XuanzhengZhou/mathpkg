---
role: proof
locale: en
of_concept: characterization-of-maximal-linear-subspace
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Equivalent Characterizations of Maximal Linear Subspaces

Let $E$ be a vector space over $\mathbb{K}$ ($\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$), and let $M$ be a linear subspace of $E$. The following conditions are equivalent:

**(a)** $M$ is a maximal linear subspace of $E$ (i.e., $M \neq E$ and if $N$ is a linear subspace with $M \subset N$, then $N = M$ or $N = E$);

**(b)** $M$ is the null space of some nonzero linear form $f$ on $E$;

**(c)** $E/M$ is one-dimensional;

**(d)** there exists a vector $z \notin M$ such that $E = M + \mathbb{K}z$;

**(e)** $M \neq E$ and, for each vector $x \notin M$, $E = M + \mathbb{K}x$.

*Proof.*

**(b) $\Rightarrow$ (a):** Let $f: E \to \mathbb{K}$ be a nonzero linear form with null space $M$. Since $\mathbb{K}$ has no linear subspaces other than $\{0\}$ and $\mathbb{K}$, and since the range of $f$ is a nonzero linear subspace of $\mathbb{K}$, necessarily $f(E) = \mathbb{K}$. Thus, the quotient vector space $E/M$ is isomorphic to $\mathbb{K}$ by the first isomorphism theorem, and the absence of subspaces of $\mathbb{K}$ between $\{0\}$ and $\mathbb{K}$ precludes the existence of subspaces of $E$ between $M$ and $E$.

**(c) $\Rightarrow$ (a):** If $E/M$ is one-dimensional, it has no proper nonzero subspaces. Any subspace $N$ with $M \subsetneq N \subsetneq E$ would yield a proper nonzero subspace $N/M$ of $E/M$, contradiction. Hence $M$ is maximal.

**(a) $\Rightarrow$ (d):** Since $M \neq E$, choose $z \in E \setminus M$. Then $M + \mathbb{K}z$ is a linear subspace containing $M$, and $z \in M + \mathbb{K}z \setminus M$, so $M \subsetneq M + \mathbb{K}z$. By maximality of $M$, we must have $M + \mathbb{K}z = E$.

**(d) $\Rightarrow$ (e):** Given $z \notin M$ with $E = M + \mathbb{K}z$, in particular $M \neq E$. For any $x \notin M$, write $x = m_0 + \lambda_0 z$ with $m_0 \in M$, $\lambda_0 \in \mathbb{K}$. Since $x \notin M$, $\lambda_0 \neq 0$. For arbitrary $y \in E$, write $y = m + \lambda z$ ($m \in M$, $\lambda \in \mathbb{K}$). Then $y = m + \lambda \lambda_0^{-1}(x - m_0) = (m - \lambda \lambda_0^{-1} m_0) + \lambda \lambda_0^{-1} x \in M + \mathbb{K}x$. Thus $E = M + \mathbb{K}x$.

**(e) $\Rightarrow$ (c):** For any $x \notin M$, the map $\mathbb{K} \to E/M$ given by $\lambda \mapsto \lambda x + M$ is surjective (since every $y \in E$ can be written as $y = m + \lambda x$, whence $y + M = \lambda x + M$) and injective (if $\lambda x \in M$, then $\lambda = 0$, else $x \in M$). Hence $E/M \cong \mathbb{K}$ is one-dimensional.

**(c) $\Rightarrow$ (b):** If $E/M$ is one-dimensional, fix an isomorphism $\varphi: E/M \to \mathbb{K}$. Let $\pi: E \to E/M$ be the canonical quotient map. Define $f = \varphi \circ \pi$. Then $f$ is a nonzero linear form on $E$ and $\ker f = \ker \pi = M$. Thus $M$ is the null space of a nonzero linear form.

All conditions are equivalent. Moreover, suppose $f$ and $g$ are nonzero linear forms with

$$M = \{x \in E : f(x) = 0\} = \{x \in E : g(x) = 0\}.$$

Choose any $z \notin M$. Then $f(z) \neq 0$ and we may define $\rho = g(z)/f(z)$. Given any $x \in E$, by condition (e) we may write $x = y + \lambda z$ with $y \in M$ and $\lambda \in \mathbb{K}$. Then $f(y) = g(y) = 0$, therefore

$$g(x) = \lambda g(z) = \frac{g(z)}{f(z)} \cdot \lambda f(z) = \rho f(x).$$

Thus $g = \rho f$; the linear form is uniquely determined up to a nonzero scalar multiple.
