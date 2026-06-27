---
role: proof
locale: en
of_concept: galilean-invariance-constraints
source_book: gtm060
source_chapter: "1"
source_section: "2"
---

\textbf{Time translation:} If $x = \varphi(t)$ is a solution, then $x = \varphi(t + s)$ is also a solution for any $s \in \mathbb{R}$. This means $F(x, \dot{x}, t + s) = F(x, \dot{x}, t)$ for all $s$, so $F$ is independent of $t$. Hence $\ddot{x} = \Phi(x, \dot{x})$.

\textbf{Space translation:} If $x_i = \varphi_i(t)$ is a motion, then for any $r \in \mathbb{R}^3$, $\varphi_i(t) + r$ is also a motion. Applying Newton's equation, $\ddot{\varphi}_i = F_i(\{\varphi_j\}, \{\dot{\varphi}_j\})$ and also $\ddot{\varphi}_i = F_i(\{\varphi_j + r\}, \{\dot{\varphi}_j\})$. Since the left side is unchanged (the added constant $r$ has zero derivative), $F_i$ must depend only on differences $x_j - x_k$.

\textbf{Boost invariance:} Under a transformation to a uniformly moving frame, $\ddot{x}_i$ and $x_j - x_k$ are unchanged, but each $\dot{x}_j$ gets a fixed vector $v$ added. The equality of left and right sides for all $v$ forces $F_i$ to depend only on relative velocities $\dot{x}_j - \dot{x}_k$.

\textbf{Rotational invariance:} If $G$ is orthogonal and $\varphi_i$ is a solution, then $G\varphi_i$ must also satisfy the equation: $\ddot{(G\varphi_i)} = G\ddot{\varphi}_i = G F(\varphi, \dot{\varphi})$, while the right-hand side for the transformed motion is $F(G\varphi, G\dot{\varphi})$. Equating gives $F(Gx, G\dot{x}) = G F(x, \dot{x})$.
