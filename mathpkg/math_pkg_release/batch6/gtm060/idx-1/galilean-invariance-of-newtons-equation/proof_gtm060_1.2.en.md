---
role: proof
locale: en
of_concept: galilean-invariance-of-newtons-equation
source_book: gtm060
source_chapter: "1"
source_section: "2"
---

Galileo's principle of relativity states that in physical space-time there is a selected galilean structure having the following property: if we subject the world lines of all the points of any mechanical system to one and the same galilean transformation, we obtain world lines of the same system (with new initial conditions).

This imposes conditions on the form of the right-hand side of Newton's equation in an inertial coordinate system. The equation $\ddot{x} = F(x, \dot{x}, t)$ must be invariant with respect to the group of galilean transformations.

\textbf{Time translation invariance:} If $x = \varphi(t)$ is a solution, then $x = \varphi(t + s)$ is also a solution for any $s \in \mathbb{R}$. This implies $F$ cannot depend explicitly on $t$, yielding $\ddot{x} = \Phi(x, \dot{x})$.

\textbf{Space translation invariance:} If $x_i = \varphi_i(t)$ is a motion of $n$ points, then $\varphi_i(t) + r$ ($r \in \mathbb{R}^3$) also satisfies the equation. This implies $F$ depends only on relative coordinates $x_j - x_k$.

\textbf{Galilean boost invariance:} Passage to a uniformly moving coordinate system adds a constant $v$ to each $\dot{x}_j$ without changing $\ddot{x}_i$ or $x_j - x_k$. Hence $F$ can depend only on relative velocities $\dot{x}_j - \dot{x}_k$.

\textbf{Rotational invariance:} For any orthogonal transformation $G: \mathbb{R}^3 \rightarrow \mathbb{R}^3$, if $\varphi_i$ is a motion then $G\varphi_i$ is also a motion, giving the equivariance condition $\mathbf{F}(G\mathbf{x}, G\dot{\mathbf{x}}) = G\mathbf{F}(\mathbf{x}, \dot{\mathbf{x}})$.
