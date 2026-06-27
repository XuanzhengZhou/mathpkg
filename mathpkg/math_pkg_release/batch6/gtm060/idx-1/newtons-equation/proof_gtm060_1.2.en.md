---
role: proof
locale: en
of_concept: newtons-equation
source_book: gtm060
source_chapter: "1"
source_section: "2"
---

Newton's equation $\ddot{x} = F(x, \dot{x}, t)$ follows directly from Newton's principle of determinacy. By that principle, the initial positions $x(t_0) \in \mathbb{R}^N$ and initial velocities $\dot{x}(t_0) \in \mathbb{R}^N$ uniquely determine the entire motion. Since the motion is uniquely determined, the acceleration $\ddot{x}(t_0)$ at the initial instant is also uniquely determined by $x(t_0)$ and $\dot{x}(t_0)$. Because the equation of motion is autonomous with respect to time translation (the laws of mechanics are the same at all times), this relationship must hold at every instant, yielding a function $F$ such that $\ddot{x} = F(x, \dot{x}, t)$ for all $t$. The existence and uniqueness of solutions then follows from the standard theory of ordinary differential equations, provided $F$ satisfies appropriate smoothness conditions.
