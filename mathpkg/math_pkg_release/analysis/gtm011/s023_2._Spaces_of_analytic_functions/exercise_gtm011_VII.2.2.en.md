---
role: exercise
locale: en
chapter: "VII"
section: "2"
exercise_number: 2
---

Let $G$ be a region, let $a \in \mathbb{R}$, and suppose that $f: [a, \infty) \times G \to \mathbb{C}$ is a continuous function. Define the integral

$$F(z) = \int_a^\infty f(t, z) \, dt$$

to be uniformly convergent on compact subsets of $G$ if $\lim_{b \to \infty} \int_a^b f(t, z) \, dt$ exists uniformly for $z$ in any compact subset of $G$. Suppose that this integral does converge uniformly on compact subsets of $G$ and that for each $t \in (a, \infty)$, $f(t, \cdot)$ is analytic on $G$. Prove that $F$ is analytic on $G$ and

$$F^{(k)}(z) = \int_a^\infty \frac{\partial^k f(t, z)}{\partial z^k} \, dt$$

for all $k \geq 1$, where the differentiated integrals converge uniformly on compact subsets of $G$.
