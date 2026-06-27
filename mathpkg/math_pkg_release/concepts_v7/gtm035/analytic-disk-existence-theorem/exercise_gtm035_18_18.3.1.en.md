---
role: exercise
locale: en
chapter: "18"
section: "18.3"
exercise_number: 1
---
# Exercise 18.1

Let $h$ be a smooth real-valued function on $\mathbb{R}^N$ which vanishes at $0$ of order $\geq 2$. Let $H_1$ be the Banach space of real-valued functions on $\Gamma = \{|\zeta| = 1\}$ with norm $\|u\|_1 = (\int_\Gamma |u|^2)^{1/2} + (\int_\Gamma |\dot{u}|^2)^{1/2}$. For $x \in H_1$, define the operator $A_w$ by

$$A_w x = -T\{h(x, w)\},$$

where $T$ is the harmonic conjugate operator and $w$ is a fixed vector of smooth boundary functions. Let $B_M = \{x \in H_1 : \|x\|_1 \leq M\}$.

Show that for $M$ sufficiently small and $\|w\|_1 < M$, there exists a constant $\alpha$ with $0 < \alpha < 1$ such that

1. $A_w(B_M) \subseteq B_M$,
2. $\|A_w x - A_w y\|_1 \leq \alpha \|x - y\|_1$ for all $x, y \in B_M$.

Conclude that $A_w$ has a unique fixed point in $B_M$.

*Hint.* Use Exercises 18.2 and 18.3 for the estimates, and the Banach contraction mapping principle.
