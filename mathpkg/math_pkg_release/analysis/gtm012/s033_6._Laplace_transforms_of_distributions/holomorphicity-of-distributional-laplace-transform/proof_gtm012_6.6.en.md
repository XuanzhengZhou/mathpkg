---
role: proof
locale: en
of_concept: holomorphicity-of-distributional-laplace-transform
source_book: gtm012
source_chapter: "6"
source_section: "§6. Laplace transforms of distributions"
---

# Proof of Holomorphicity and Representation of the Distributional Laplace Transform

**Theorem 6.2.** Suppose $F \in \mathcal{L}'$ and suppose there exist constants $k, a, M, K$ such that

$$|F(u)| \leq K |u|_{k,a,M}, \quad \text{for all } u \in \mathcal{L}.$$

Then the Laplace transform $LF$ is holomorphic in the half plane

$$\{z \mid \operatorname{Re} z > a\}.$$

Moreover,

$$F = D^{k+2} F_f,$$

where $f$ is the function defined by

$$f(t) = \frac{1}{2\pi i} \int_C e^{zt} z^{-k-2} LF(z) \, dz,$$

and $C$ is the line $\{z \mid \operatorname{Re} z = b\}$ with $b > \max\{a, 0\}$.

*Proof.* Consider first the case $a \geq 0$. By Theorem 5.2 applied to the function $h(z) = z^{-k-2} LF(z)$, there exists a continuous function $f$ with $\operatorname{supp} f \subset [M, \infty)$ and $|f(t)| \leq c e^{bt}$ such that $Lf = h$. Therefore $Lf$ is holomorphic for $\operatorname{Re} z > \max\{a, 0\}$. By Proposition 6.1 (property relating $D^k$ to the Laplace transform),

$$LF(z) = z^{k+2} Lf(z), \quad \operatorname{Re} z > \max\{a, 0\}.$$

Therefore $LF$ is holomorphic in this half plane. This completes the proof of the first statement in the case $a \geq 0$.

When $a < 0$, let $G = e_a F$. Then the bound (1) implies

$$|G(u)| = |F(e_a u)| \leq K |e_a u|_{k,a,M} = K |u|_{k,0,M}.$$

Thus by the argument just given for the case $a \geq 0$, $LG$ is holomorphic for $\operatorname{Re} z > 0$. Since $LF(z) = LG(z - a)$ by Proposition 6.1, $LF$ is holomorphic for $\operatorname{Re} z > a$. This proves the first statement in all cases.

Now let $C$ be the line $\{z \mid \operatorname{Re} z = b\}$, where $b > \max\{a, 0\}$. Let $f$ be the function such that

$$F = D^{k+2} F_f.$$

Then by Theorem 5.2 and the relation $LF(z) = z^{k+2} Lf(z)$, the function $f$ is the $k+2$-fold derivative of the function

$$g(t) = \frac{1}{2\pi i} \int_C e^{zt} z^{-k-4} LF(z) \, dz.$$

From the definition of $LF$ it follows that on $C$,

$$|LF(z)| \leq K |e_z|_{k,a,M} = K |z|^k e^{aM - bM}.$$

Using this estimate we may justify differentiating the integral for $g$ twice under the integral sign (bringing down two factors of $z$) to obtain the representation

$$f(t) = \frac{1}{2\pi i} \int_C e^{zt} z^{-k-2} LF(z) \, dz.$$

This completes the proof. $\square$
