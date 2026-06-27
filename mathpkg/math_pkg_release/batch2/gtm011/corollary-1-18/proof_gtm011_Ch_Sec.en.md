---
role: proof
locale: en
of_concept: corollary-1-18
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. (a) If $a_n = 0$ for $n \leq -1$ then let $g(z)$ be defined in $B(a; R)$ by $g(z) = \sum_{n=0}^{\infty} a_n(z-a)^n$; thus, $g$ must be analytic and agrees with $f$ in the punctured disk. The converse is equally as easy.

(b) Suppose $a_n = 0$ for $n \leq -(m+1)$; then $(z-a)^m f(z)$ has a Laurent Expansion which has no negative powers of $(z-a)$. By part (a), $(z-a)^m f(z)$ has a removable singularity at $z = a$. Thus $f$ has a pole of order $m$ at $z = a$. The converse follows by retracing the steps in the preceding argument.

(c) Since $f$ has an essential singularity at $z = a$ when it has neither a removable singularity nor a pole, part (c) follows from parts (a) and (b).

One can also classify isolated singularities by examining the equations

1.19 $$\lim_{z \to a} |z-a|^s |f(z)| = 0$$

1.20 $$\lim_{z \to a} |z-a|^s |f(z)| = \infty$$

where $s$ is some real number. This

Hence $|z - a|^{m+1}|f(z)| \leq |z - a|^{m+1}|f(z) - c| + |z - a|^{m+1}|c|$ gives that $\lim_{z \to a} |z - a|^{m+1}|f(z)| = 0$ since $m \geq 1$. But, according to Theorem 1.2, this gives that $f(z)(z - a)^m$ has a removable singularity at $z = a$. This contradicts the hypothesis and completes the proof of the theorem.

Exercises

1. Each of the following functions $f$ has an isolated singularity at $z = 0$. Determine its nature; if it is a removable singularity define $f(0)$ so that $f$ is analytic at $z = 0$; if it is a pole find the singular part; if it is an essential singularity determine $f(\{z: 0 < |z| < \delta\})$ for arbitrarily small values of $\delta$.

(a) $f(z) = \frac{\sin z}{z}$;

(b) $f(z) = \frac{\cos z}{z}$;

(c) $f(z) = \frac{\cos z - 1}{z}$;

(d) $f(z) = \exp(z^{-1})$;

(e) $f(z) = \frac{\log(z+1)}{z^2}$;

(f) $f(z) = \frac{\cos(z^{-1})}{z^{-1}}$;

(g) $f(z) = \frac{z^2 + 1}{z(z-1)}$;

(h) $f(z) = (1 - e^z)^{-1}$;

(i) $f(z) = z \sin \frac{1}{z}$;

2. Give the partial fraction expansion of $r(z) = \frac{z^2 + 1}{(z^2 + z + 1)(z - 1)^2}$.

3. Give the details of the derivation of (1.17) from (1.16).

4. Let $f(z) = \frac{1}{z(z-1)(z-2)}$; give the Laurent Expansion of $f(z)$ in each

10. Suppose that $f$ has an essential singularity at $z = a$. Prove the following strengthened version of the Casorati–Weierstrass Theorem. If $c \in \mathbb{C}$ and $\epsilon > 0$ are given then for each $\delta > 0$ there is a number $\alpha$, $|c - \alpha| < \epsilon$, such that $f(z) = \alpha$ has infinitely many solutions in $B(a; \delta)$.

11. Give the Laurent series development of $f(z) = \exp \left( \frac{1}{z} \right)$. Can you generalize this result?

12. (a) Let $\lambda \in \mathbb{C}$ and show that

$$\exp \left\{ \frac{1}{2} \lambda \left( z + \frac{1}{z} \right) \right\} = a_0 + \sum_{n=1}^{\infty} a_n \left( z^n + \frac{1}{z^n} \right)$$

for $0 < |z| < \infty$, where for $n \geq 0$

$$a_n = \frac{1}{\pi} \int_0^{\pi} e^{\lambda \cos t} \cos nt \, dt$$

(b) Similarly, show

$$\exp \left\{ \frac{1}{2} \lambda \left( z - \frac{1}{z} \right) \right\} = b_0 + \sum
