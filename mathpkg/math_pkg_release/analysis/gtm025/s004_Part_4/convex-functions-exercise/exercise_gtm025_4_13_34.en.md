---
role: exercise
locale: en
chapter: "4"
section: "13"
exercise_number: 34
---

Let $I$ be an interval of $R$. A real-valued function $\Phi$ defined on $I$ is said to be convex if whenever $a < b$ in $I$ and $0 \le t \le 1$ we have $\Phi(t a + (1 - t) b) \le t \Phi(a) + (1 - t) \Phi(b)$.

(a) Prove that if $t_1, \ldots, t_n$ are positive real numbers and $\{x_1, \ldots, x_n\} \subset I$, then
$$\Phi\left(\frac{t_1 x_1 + \cdots + t_n x_n}{t_1 + \cdots + t_n}\right) \le \frac{t_1 \Phi(x_1) + \cdots + t_n \Phi(x_n)}{t_1 + \cdots + t_n}.$$
[Use induction.]

(b) Prove that $\Phi$ is continuous on the interior $I^\circ$ of $I$ and show by an example that $\Phi$ may be discontinuous at the endpoints of $I$.

(c) Prove that if $c$ is in $I^\circ$, then there exists a real number $\alpha$ such that $\Phi(u) \ge \alpha(u - c) + \Phi(c)$ for all $u \in I$.

(d) Prove the following generalization of Jensen's inequality. Let $(X, \mathcal{A}, \mu)$ be a finite measure space. If $f \in \mathfrak{L}_1^r(X, \mathcal{A}, \mu)$, if $f(X) \subset I$, and if $\Phi \circ f \in \mathfrak{L}_1^r$, then
$$\Phi\left(\frac{1}{\mu(X)} \int_X f d\mu\right) \le \frac{1}{\mu(X)} \int_X \Phi \circ f d\mu.$$