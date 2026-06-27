---
role: proof
locale: en
of_concept: proposition-1-1
source_book: gtm011
source_chapter: "Runge's Theorem"
source_section: "1. Runge's Theorem"
---

Proof. Since $K$ and $\{\gamma\}$ are disjoint there is a number $r$ with $0 < r < d(K, \{\gamma\})$. If $\gamma$ is defined on $[0, 1]$ then for $0 \leq s, t \leq 1$ and $z$ in $K$

$$\left| \frac{f(\gamma(t))}{\gamma(t)-z} - \frac{f(\gamma(s))}{\gamma(s)-z} \right| \leq \frac{1}{r^2} \left| f(\gamma(t))\gamma(s) - f(\gamma(s))\gamma(t) - z[f(\gamma(t)) - f(\gamma(s))] \right|$$

$$\leq \frac{1}{r^2} \left| f(\gamma(t)) \right| \left| \gamma(s) - \gamma(t) \right| + \frac{1}{r^2} \left| \gamma(t) \right| \left| f(\gamma(s)) \right|$$

$$- f(\gamma(t)) \left| + \frac{|z|}{r^2} \left| f(\gamma(s)) - f(\gamma(t)) \right| \right|$$

There is a constant $c > 0$ such that $|z| \leq c$ for all $z$ in $K$, $|\gamma(t)| \leq c$ and $|f(\gamma(t))| \leq c$ for all $t$ in $[0, 1]$. This gives that for all $s$ and $t$ in $[0, 1]$ and $z

Before stating Runge’s Theorem let us agree to say that a polynomial is a rational function with a pole at $\infty$. It is easy to see that a rational function whose only pole is at $\infty$ is a polynomial.

1.7 Runge’s Theorem. Let $K$ be a compact subset of $\mathbb{C}$ and let $E$ be a subset of $\mathbb{C}_\infty - K$ that meets each component of $\mathbb{C}_\infty - K$. If $f$ is analytic in an open set containing $K$ and $\epsilon > 0$ then there is a rational function $R(z)$ whose only poles lie in $E$ and such that

$$|f(z) - R(z)| < \epsilon$$

for all $z$ in $K$.

The proof that will be given here was obtained by S. Grabiner (Amer. Math. Monthly, 83 (1976), 807–808). For this proof we place the result in a different setting. On the space $C(K, \mathbb{C})$ we define a distance function $\rho$ by

$$\rho(f, g) = \sup \left\{ |f(z) - g(z)| : z \in K \right\}$$

for $f$ and $g$ in $C(K, \mathbb{C})$. It is easy to see that $\rho(f_n, f) \to 0$ iff $f = u - \lim f_n$ on $K$. Hence $C(K, \mathbb{C})$ is a complete metric space.

So Runge’s Theorem says that if $f$ is analytic on a neighborhood of $K$ and $\epsilon > 0$ then there is a rational function $R(z)$ with poles in $E$ such that $\rho(f, R) < \epsilon$. By taking $\epsilon = 1/n$ it is seen that we want to find a sequence of rational functions $\{R_n(z)\}$ with poles in $E$ such that $\rho(f, R_n) \to 0$; that is, such that $f = u - \lim R_n$ on $K$.

Let $B(E) = \text{all functions } f \text{ in } C(K, \mathbb{C})$ such that there
