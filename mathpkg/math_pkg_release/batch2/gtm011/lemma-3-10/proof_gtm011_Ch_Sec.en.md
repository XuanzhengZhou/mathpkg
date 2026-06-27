---
role: proof
locale: en
of_concept: lemma-3-10
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. For each $\epsilon > 0$ let $g_\epsilon(z) = [1 + \epsilon(z-a)]^{-1}$ for each $z$ in $G^-$. Then for $z = x+iy$

for $a < u < b$ (see (3.8)). To do this recall that for a constant $A > 0$, $A^z = \exp(z \log A)$ is an entire function of $z$ with no zeros. So $g(z)$ defined by

$$g(z) = M(a)^{(b-z)/(b-a)} M(b)^{(z-a)/(b-a)}$$

is entire, never vanishes, and (because $|A^z| = A^{Rez}$) for $z = x + iy$

3.12 $|g(z)| = M(a)^{(b-x)/(b-a)} M(b)^{(x-a)/(b-a)}$.

(It is assumed here that $M(a)$ and $M(b) \neq 0$. However, if either $M(a)$ or $M(b)$ is zero then $f \equiv 0$.) Since the expression on the right hand side of (3.12) is continuous for $x$ in $[a, b]$ and never vanishes, $|g|^{-1}$ must be bounded in $G^-$. Also, $|g(a+iy)| = M(a)$ and $|g(b+iy)| = M(b)$ so that $|f(z)/g(z)| \leq 1$ for $z$ in $\partial G$; and $f/g$ satisfies the hypothesis of Lemma 3.10. Thus

$$|f(z)| \leq |g(z)|, z \in G.$$

Using (3.12) this gives for $a < u < b$

$$M(u) \leq M(a)^{(b-u)/(b-a)} M(b)^{(u-a)/(b-a)}$$

which is the desired conclusion.

Hadamard’s Three Circles Theorem is an analogue of the preceding theorem for an annulus. Consider ann $(0; R_1, R_2) = A$ where $0 < R_1 < R_2 < \infty$. If $G$ is the strip $\{x+iy: \log R_1 < x < \log R_2\}$ then the exponential function maps $G$ onto $A$ and $\partial G$ onto $\partial A$. Using this fact one can prove the following from
