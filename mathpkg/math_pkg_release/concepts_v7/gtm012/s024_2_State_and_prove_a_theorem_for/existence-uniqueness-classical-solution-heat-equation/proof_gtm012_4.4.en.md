---
role: proof
locale: en
of_concept: existence-uniqueness-classical-solution-heat-equation
source_book: gtm012
source_chapter: "4"
source_section: "The heat equation: classical solutions; derivation"
---

# Proof of Existence and uniqueness of classical solution to the heat equation (Theorem 4.2)

**Theorem 4.2.** For each continuous function $g$ on $[0, \pi]$ with $g(0) = g(\pi) = 0$, there is a unique classical solution $u(x, t)$ of the problem

$$\frac{\partial}{\partial t} u(x, t) = \left( \frac{\partial}{\partial x} \right)^2 u(x, t), \quad x \in (0, \pi), \quad t > 0, \tag{1}$$

$$u(x, 0) = g(x), \quad x \in [0, \pi], \tag{2}$$

$$u(0, t) = u(\pi, t) = 0, \quad t \geq 0. \tag{3}$$

**Proof.**

Note that $u$ is a classical solution with initial values given by $g$ if and only if the real and imaginary parts of $u$ are classical solutions with initial values given by the real and imaginary parts of $g$, respectively. Therefore we may assume that $g$ and $u$ are real-valued.

**Uniqueness.** Suppose $u_1$ and $u_2$ are two classical solutions of (1), (2), (3) with the same initial data $g$. Then $w = u_1 - u_2$ is a classical solution with initial data $w(x, 0) \equiv 0$ and boundary data $w(0, t) = w(\pi, t) \equiv 0$. By Theorem 4.1 (the maximum principle), applied on any rectangle $[0, \pi] \times [0, T]$, the maximum of $w$ on the rectangle is attained on the parabolic boundary. On the parabolic boundary, $w$ is identically zero. Therefore $w(x, t) \leq 0$ for all $(x, t)$.

Applying Theorem 4.1 to $-w$, which is also a classical solution with zero initial and boundary data, we obtain $-w(x, t) \leq 0$, i.e., $w(x, t) \geq 0$ for all $(x, t)$.

Thus $w \equiv 0$, which proves $u_1 = u_2$. This establishes uniqueness.

**Existence.** Given $g \in C[0, \pi]$ with $g(0) = g(\pi) = 0$, extend $g$ to be an odd periodic function on $\mathbb{R}$ as follows. First define $g(-x) = -g(x)$ for $x \in (-\pi, 0)$, so that $g$ is odd on $[-\pi, \pi]$. The condition $g(0) = g(\pi) = 0$ guarantees that the resulting extension is continuous on $[-\pi, \pi]$ (and indeed, the oddness forces $g(0) = 0$ and $g(\pi) = 0 = -g(-\pi)$). Then extend $g$ periodically with period $2\pi$ to all of $\mathbb{R}$. The extended function belongs to $\mathcal{C}$ (the space of continuous periodic functions).

Let $G = F_g \in \mathcal{P}'$ be the periodic distribution defined by this extended $g$. Apply Theorem 3.1 to $G$: there exists a unique family $(F_t)_{t > 0} \subset \mathcal{P}'$ satisfying (7) and (8) of §3, and for each $t > 0$, $F_t$ is given by a smooth function $u(x, t)$ (infinitely differentiable in both $x$ and $t$ for $t > 0$) satisfying the heat equation for all $x \in \mathbb{R}$, $t > 0$. Moreover, $F_t \to G$ in $\mathcal{P}'$ as $t \to 0$.

By Exercise 1 of §3, since $G$ is odd (as a distribution defined by an odd function), each $F_t$ is odd as a function of $x$. In particular, $u(0, t) = 0$ for all $t > 0$. By periodicity, $u(\pi, t) = u(-\pi, t) = -u(\pi, t)$ (by oddness and periodicity), so $u(\pi, t) = 0$ as well. Thus $u$ satisfies the boundary conditions (3).

By Exercise 4 of §3, since $G = F_g$ with $g \in \mathcal{P}$, the functions $u_t = u(\cdot, t)$ converge to $g$ in $\mathcal{P}$ (and hence uniformly) as $t \to 0$. Therefore, setting $u(x, 0) = g(x)$ yields a continuous extension of $u$ to $[0, \pi] \times [0, \infty)$.

Restricting $u$ to $x \in [0, \pi]$, $t \geq 0$, we obtain a classical solution of problem (1), (2), (3). $\square$
