---
role: proof
locale: en
of_concept: w-star-group-algebra-finite
source_book: gtm003
source_chapter: "VI"
source_section: "11"
---

\textit{Proof sketch (Exercise).} The functional $\tau(x) = [x\delta_e, \delta_e]$ is clearly a normal positive linear form. To show it is a trace, one verifies $\tau(xy) = \tau(yx)$ for all $x, y \in W(G)$. It suffices to check this on generators $u_g$, yielding $\tau(u_g x) = \tau(x u_g)$.

For faithfulness: suppose $\tau(x) = 0$ and $x \geq 0$. By the Cauchy--Schwarz inequality, $|\tau(x u_g)|^2 \leq \tau(x) \tau(u_g^* x u_g) = 0$ for all $g \in G$. Since the $u_g$ span a weakly dense subspace, this forces $x = 0$. Hence $\tau$ is strictly positive (faithful). The existence of a faithful normal trace implies $W(G)$ is finite.
