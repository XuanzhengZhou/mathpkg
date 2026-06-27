---
role: proof
locale: en
of_concept: van-kampen-theorem
source_book: gtm057
source_chapter: "V"
source_section: "3"
---

Let $X = X_1 \cup X_2$ where $X_1, X_2$, and $X_0 = X_1 \cap X_2$ are open, pathwise connected, and nonvoid. Fix $p \in X_0$ and set $G = \pi(X,p)$, $G_i = \pi(X_i,p)$ for $i = 0,1,2$. The inclusion-induced homomorphisms form the diagram

$$G_1 \xleftarrow{\theta_1} G_0 \xrightarrow{\theta_2} G_2$$
with $\omega_i: G_i \to G$ and $\omega_0 = \omega_1\theta_1 = \omega_2\theta_2$.

**Part 1 (III.1):** The image groups $\omega_i G_i$ generate $G$. Given any nontrivial $\alpha \in G$ represented by a $p$-based loop $a$, subdivide $[0, \|a\|]$ by $0 = t_0 < t_1 < \dots < t_n = \|a\|$ so fine that each subinterval maps into some $X_{\mu(i)}$, where $\mu(i) \in \{0,1,2\}$. For each $t_i$, choose a path $b_i$ from $p$ to $a(t_i)$ lying in the appropriate intersections. Then each segment $a_i = b_{i-1}^{-1} \cdot (a|_{[t_{i-1},t_i]}) \cdot b_i$ is a $p$-based loop in $X_{\mu(i)}$, and $\alpha = \prod_i \omega_{\mu(i)}[a_i]$.

**Part 2 (III.2):** Given homomorphisms $\psi_i: G_i \to H$ with $\psi_0 = \psi_1\theta_1 = \psi_2\theta_2$, define $\lambda: G \to H$ by

$$\lambda\alpha = \prod_{i=1}^{n} \psi_{\mu(i)}\alpha_i$$

whenever $\alpha = \prod \omega_{\mu(i)}\alpha_i$. To prove $\lambda$ is well-defined, suppose $\prod \omega_{\mu(i)}\alpha_i = 1$. Let $a_i \in \alpha_i$ be representative loops and $h$ be a fixed-endpoint family exhibiting the equivalence $\prod \omega_{\mu(i)}a_i \simeq e_p$. Subdivide the parameter rectangle $[0, \tau] \times [0,1]$ into subrectangles $R_{ij}$ so fine that each $h R_{ij} \subset X_{\nu(i,j)}$. For each lattice point $(t_i, s_j)$, choose paths $e_{ij}$ from $p$ to $h(t_i,s_j)$ in appropriate intersections. Let $\alpha_{ij}$ be the element of $G_{\nu(i,j)}$ represented by the loop tracing the boundary of $R_{ij}$ suitably conjugated. From the fact that $R_{ij}$ is contractible in $X_{\nu(i,j)}$, we obtain relations among the $\alpha_{ij}$. A key observation is: if elements $\alpha \in G_i$ and $\beta \in G_j$ possess a common representative loop, then $\psi_i\alpha = \psi_j\beta$. This follows because the inclusion $X_i \cap X_j = X_k \hookrightarrow X_i, X_j$ induces consistent homomorphisms with the $\psi$'s.

Tracing through the decomposition yields $\prod \psi_{\mu(i)}\alpha_i = 1$, establishing well-definedness of $\lambda$. The identities $\psi_i = \lambda\omega_i$ and the homomorphism property of $\lambda$ follow directly from the definition.
