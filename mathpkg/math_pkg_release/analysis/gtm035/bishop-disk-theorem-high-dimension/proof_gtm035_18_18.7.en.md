---
role: proof
locale: en
of_concept: bishop-disk-theorem-high-dimension
source_book: gtm035
source_chapter: "18"
source_section: "18.7"
---
# Proof of Bishop Disk Theorem in High Dimension

**Theorem 18.7.** Let $\Sigma^k$ be a $k$-dimensional submanifold of $\mathbb{C}^n$ of class $C^e$ ($e \geq 2$) with $n < k < 2n$, satisfying the nondegeneracy condition (6) at $0 \in \Sigma^k$. Then in every neighborhood of $0$ on $\Sigma^k$ there exists the boundary of an analytic disk.

**Proof (Sketch).** The proof is a direct generalization of the proof of Theorem 18.3, replacing the scalar-valued function $h$ (for hypersurfaces, where $\dim \Sigma = 2n-1$, so $k = 2n-1$) by a vector-valued function.

**Step 1: Parametric representation.** By Lemma 18.8, after a complex-linear change of coordinates, $\Sigma^k$ can be described parametrically near $0$ by the system

$$\begin{cases}
z_j = x_j + i h_j(x_1, \ldots, x_{2n-k}, w_1, \ldots, w_{k-n}), & 1 \leq j \leq 2n - k, \\
z_{2n-k+j} = w_j, & 1 \leq j \leq k - n,
\end{cases}$$

where each $h_j$ is a smooth real-valued function vanishing at $0$ of order $\geq 2$. Define the vector-valued function

$$h(x, w) = (h_1(x, w), \ldots, h_{2n-k}(x, w)),$$

which maps a neighborhood of $0$ in $\mathbb{R}^k$ into $\mathbb{R}^{2n-k}$. This vector-valued $h$ plays the same role as the scalar-valued $h$ in the proof of Theorem 18.3.

**Step 2: Boundary functions and the operator equation.** Fix smooth boundary functions $w_1, \ldots, w_{k-n}$ on $\Gamma = \{|\zeta| = 1\}$ such that $w_1$ is schlicht (univalent), and put $w = (w_1, \ldots, w_{k-n})$ as a map $\Gamma \to \mathbb{C}^{k-n}$.

We seek a map $x^* = (x_1^*, \ldots, x_{2n-k}^*): \Gamma \to \mathbb{R}^{2n-k}$ such that each component $x_j^* \in H_1$ and

$$x^* + i h(x^*, w)$$

admits an analytic extension $\psi = (\psi_1, \ldots, \psi_{2n-k})$ to $|\zeta| < 1$ taking values in $\mathbb{C}^{2n-k}$.

**Step 3: Contraction mapping.** By the characterization of boundary functions of analytic maps, the condition that $x^* + i h(x^*, w)$ extends analytically is equivalent to the fixed-point equation

$$x^* = -T\{h(x^*, w)\},$$

where $T$ acts componentwise and the operator on the right is defined analogously to Definition 18.4. The same estimates as in Theorem 18.3 (Exercises 18.2 and 18.3, generalized to vector-valued maps) show that for sufficiently small $M$ and $\|w\|_1 < M$, the operator

$$A_w x = -T\{h(x, w)\}$$

is a contraction on the ball $B_M = \{x \in H_1(\Gamma, \mathbb{R}^{2n-k}) : \|x\|_1 \leq M\}$. Hence by the Banach fixed point theorem, there exists a unique fixed point $x^* \in B_M$.

**Step 4: The analytic disk.** Let $\psi = (\psi_1, \ldots, \psi_{2n-k})$ be the analytic extension of $x^* + i h(x^*, w)$ to $|\zeta| < 1$. Then the subset of $\mathbb{C}^n$ defined for $|\zeta| \leq 1$ by

$$z_1 = \psi_1(\zeta), \ldots, z_{2n-k} = \psi_{2n-k}(\zeta), \; z_{2n-k+1} = w_1(\zeta), \ldots, z_n = w_{k-n}(\zeta)$$

is an analytic disk $E$ in $\mathbb{C}^n$. Its boundary $\partial E$ corresponds to $|\zeta| = 1$, and for $|\zeta| = 1$ we have

$$(z_1, \ldots, z_n) = (x^*(\zeta) + i h(x^*(\zeta), w(\zeta)), w(\zeta)),$$

which by the parametric representation lies on $\Sigma^k$. By choosing $w$ sufficiently small, $\partial E$ lies in any prescribed neighborhood of $0$ on $\Sigma^k$. ∎

**Remark.** The main theorem of this section asserts that under the above conditions, $\Sigma^k$ contains at least two points $p$ such that every neighborhood of $p$ on $\Sigma$ contains the boundary of some analytic disk. This is a consequence of applying the construction at points where the $(2n-k)$-dimensional measure of the set of complex tangents is non-empty (specifically, at points satisfying condition (6)).

This section is due to E. Bishop, *Differentiable manifolds in complex Euclidean space*, Duke Math. Jour. 32 (1965).
