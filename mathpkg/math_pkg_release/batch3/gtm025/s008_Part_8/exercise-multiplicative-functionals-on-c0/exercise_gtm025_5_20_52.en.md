---
role: exercise
locale: en
chapter: "5"
section: "20"
exercise_number: 52
---

More on the structure of $\mathfrak{C}_{00}(X)$ and $\mathfrak{C}_0(X)$.

(a) Let $X$ be a nonvoid locally compact Hausdorff space, and let $M$ be a multiplicative linear functional on $\mathfrak{C}_0(X)$. Prove that there is a point $a \in X$ such that $M(f) = f(a)$ for all $f \in \mathfrak{C}_0(X)$.

[Hints. It is convenient to prove first that $M$ is continuous. In fact, $|M(f)| \leq \|f\|_u$ for all $f \in \mathfrak{C}_0$. To see this, assume that $M(f) = \alpha$ where $|\alpha| > \|f\|_u$. Let $g = -\sum_{k=1}^{\infty} \alpha^{-k}f^k$. The series converges uniformly and so $g \in \mathfrak{C}_0$. Check that $\alpha^{-1}f + g - \alpha^{-1}fg = 0$. Then $0 = M(0) = 1 + M(g) - M(g) = 1$, a contradiction. Now apply (20.47) to write $M(f) = \int_X f d\mu$ where $\mu \in M(X)$. The multiplicative property forces $\mu$ to be a point mass.]

(b) In the commutative Banach algebra $\mathfrak{C}_0(X)$, every set $\{f \in \mathfrak{C}_0(X) : f(a) = 0\}$ is a closed maximal ideal. Furthermore, every maximal ideal in $\mathfrak{C}_0(X)$ has this form.
