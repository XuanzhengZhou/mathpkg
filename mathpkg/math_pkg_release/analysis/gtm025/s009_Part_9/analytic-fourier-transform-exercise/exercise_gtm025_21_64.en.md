---
role: exercise
locale: en
chapter: "21"
section: "SS 21"
exercise_number: "21.64"
---

Some rudimentary facts about analytic functions are needed.

(a) Let $f, g \in \mathfrak{L}_1(R)$ such that $f(x) = g(x) = 0$ for all $x < 0$. Suppose $f * g = 0$ a.e. Prove that $f = 0$ a.e. or $g = 0$ a.e.

[Hints. For $z = s + it$ with $t \leq 0$, extend the Fourier transform to $f(z) = (2\pi)^{-\frac{1}{2}} \int_0^\infty \exp(-izx)f(x)dx$. Show $f$ is analytic in $\{z: \operatorname{Im} z < 0\}$ and continuous in $\{z: \operatorname{Im} z \leq 0\}$. Show $\widehat{f*g}(z) = f(z)g(z)$ for $\operatorname{Im} z \leq 0$. The analytic function $f \cdot g$ vanishing identically implies $f = 0$ or $g = 0$, and by the uniqueness theorem, $f = 0$ a.e. or $g = 0$ a.e.]

If $f$ is orthogonal to all Hermite functions, then $F^{(n)}(0) = (2\pi)^{-\frac{1}{2}}(-i)^n \int_R x^n \exp(-x^2/2)\overline{f(x)}dx = 0$ for all $n$, forcing $F \equiv 0$. Hence $\exp(-x^2/2)f(x) = 0$ a.e., so $f = 0$ a.e.
