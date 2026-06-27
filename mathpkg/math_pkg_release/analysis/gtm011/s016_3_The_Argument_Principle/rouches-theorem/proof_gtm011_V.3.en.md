---
role: proof
locale: en
of_concept: rouches-theorem
source_book: gtm011
source_chapter: "V"
source_section: "3"
---

**Proof.** From the hypothesis $|f(z) + g(z)| < |f(z)| + |g(z)|$ on $\gamma$, it follows that $f(z)/g(z)$ is never a non-negative real number on $\gamma$. Indeed, if $f(z)/g(z) = \lambda \geq 0$ for some $z \in \{\gamma\}$, then $f(z) = \lambda g(z)$ and

$$
|f(z) + g(z)| = |\lambda g(z) + g(z)| = (\lambda + 1)|g(z)| = \lambda|g(z)| + |g(z)| = |f(z)| + |g(z)|,
$$

contradicting the strict inequality. Thus $f(z)/g(z) \notin [0, \infty)$ for all $z \in \{\gamma\}$.

Since the set $[0, \infty)$ is closed in $\mathbb{C}$, the image of the compact set $\{\gamma\}$ under the continuous map $f/g$ is a compact set disjoint from $[0, \infty)$. Hence there is a simply connected neighborhood of this image that does not intersect $[0, \infty)$, and on this neighborhood a continuous branch of the logarithm can be defined. Consequently, $\log(f/g)$ is a well-defined continuous function on $\{\gamma\}$, and

$$
\int_{\gamma} \frac{(f/g)'(z)}{(f/g)(z)} \, dz = 0,
$$

since the integrand is the derivative of $\log(f/g)$. But

$$
\frac{(f/g)'}{f/g} = \frac{f'}{f} - \frac{g'}{g},
$$

so

$$
\int_{\gamma} \frac{f'(z)}{f(z)} \, dz = \int_{\gamma} \frac{g'(z)}{g(z)} \, dz.
$$

Dividing by $2\pi i$ and applying the Argument Principle (Theorem 3.4) to both sides yields

$$
Z_f - P_f = Z_g - P_g,
$$

where the winding numbers $n(\gamma; z)$ are all $1$ for points inside the circle $\gamma$ and $0$ for points outside. This completes the proof. $\square$

---

**Remark.** The use of a circle in the statement was a convenience. Any closed rectifiable curve $\gamma$ with $\gamma \sim 0$ in $G$ could be used, with the conclusion modified to include winding numbers:

$$
\sum_j n(\gamma; a_j) m(a_j) - \sum_k n(\gamma; b_k) m(b_k) = \sum_j n(\gamma; c_j) m(c_j) - \sum_k n(\gamma; d_k) m(d_k)
$$

where $\{a_j\}, \{b_k\}$ are zeros and poles of $f$, and $\{c_j\}, \{d_k\}$ are zeros and poles of $g$.
