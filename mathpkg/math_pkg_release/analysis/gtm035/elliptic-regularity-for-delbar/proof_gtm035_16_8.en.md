---
role: proof
locale: en
of_concept: elliptic-regularity-for-delbar
source_book: gtm035
source_chapter: "Chapter 16"
source_section: "16.8"
---
# Proof of Elliptic Regularity for the \bar{\partial}-Operator

**Lemma 16.8.** Let $B = \{z \in \mathbb{C}^n \mid |z| < 1\}$. Let $u \in L^2(B)$. Assume that for each $j = 1, \ldots, n$, the distributional derivative $\partial u / \partial \bar{z}_j$ (in the sense of Definition 16.1) is continuous on $B$. Then $u$ is continuous on $B$, and the estimate

$$|u(x)| \leq K \left( \|u\|_{L^2(B)} + \sup_B \max_j \left| \frac{\partial u}{\partial \bar{z}_j} \right| \right)$$

holds for all $x \in B$ with a constant $K$ depending only on the dimension $n$.

**Proof.** We first establish a pointwise estimate using the fundamental solution of the Laplacian in $\mathbb{C}^n$. Let $\Delta = 4 \sum_j \frac{\partial^2}{\partial z_j \partial \bar{z}_j}$ be the Laplacian in $\mathbb{C}^n$, and let $E(x) = C_n / |x|^{2n-2}$ be the fundamental solution, so that $\Delta E = \delta_0$ in the sense of distributions.

Fix a point $x \in B$. Choose a smooth cut-off function $\chi \in C_0^\infty(B)$ with $\chi \equiv 1$ in a neighborhood of $x$. Setting $w = \chi u$, we have the representation formula:

$$w(x) = \int_B \Delta w(\zeta) \cdot \chi(\zeta) E(x - \zeta) dV(\zeta)$$

$$= I_1 + 2 I_2 + I_3,$$

where

$$I_1 = \int_B \Delta \chi \cdot w \cdot E \, dV,$$

$$I_2 = \int_B (\nabla \chi, \nabla w) \cdot E \, dV,$$

$$I_3 = \int_B \Delta w \cdot \chi \cdot E \, dV.$$

Here we have written $\Delta(\chi w) = (\Delta \chi) w + 2 (\nabla \chi, \nabla w) + \chi \Delta w$.

**Estimates for $I_1$ and $I_2$.** Since $\chi$ is smooth with compact support in $B$, and $\Delta \chi$, $\nabla \chi$ vanish in a neighborhood of $x$ (by choosing $\chi \equiv 1$ near $x$), the integrands of $I_1$ and $I_2$ have no singularity at $x$. Moreover, $E \in L^1_{\text{loc}}(\mathbb{C}^n)$, so by the Cauchy-Schwarz inequality:

$$|I_1| \leq K_1 \|w\|_{L^2(B)}, \quad |I_2| \leq K_2 \|w\|_{L^2(B)},$$

for constants $K_1, K_2$ depending only on $\chi$ and $n$.

**Estimate for $I_3$.** The key term is

$$I_3 = \int_B \Delta w(\zeta) \cdot \chi(\zeta) E(x - \zeta) dV(\zeta).$$

Writing $\Delta = 4 \sum_j \frac{\partial^2}{\partial z_j \partial \bar{z}_j}$, we integrate by parts:

$$\int_B \frac{\partial^2 w}{\partial z_j \partial \bar{z}_j} \cdot \chi E \, dV = -\int_B \frac{\partial w}{\partial \bar{z}_j} \frac{\partial}{\partial z_j} (\chi E) \, dV.$$

(The sign follows from the fact that $\frac{\partial^2}{\partial z_j \partial \bar{z}_j} = \frac{\partial}{\partial z_j} \frac{\partial}{\partial \bar{z}_j}$, and $\chi E$ has compact support in $B$, so boundary terms vanish.)

Hence

$$|I_3| \leq 4 \sum_j \int_B \left| \frac{\partial w}{\partial \bar{z}_j} \right| \cdot \left| \frac{\partial}{\partial z_j} (\chi E) \right| dV.$$

Since $\frac{\partial E}{\partial z_j} \in L^1_{\text{loc}}(\mathbb{C}^n)$ (it behaves like $1/|x|^{2n-1}$), and $\chi$ is smooth, the function $\frac{\partial}{\partial z_j} (\chi E)$ is integrable on $B$. Noting that $\frac{\partial w}{\partial \bar{z}_j} = \chi \frac{\partial u}{\partial \bar{z}_j}$ near $x$ (since $\chi \equiv 1$ there), we obtain:

$$|I_3| \leq K_3 \sup_B \left( \max_j \left| \frac{\partial u}{\partial \bar{z}_j} \right| \right),$$

with $K_3$ depending only on $\chi$ and $n$.

**Conclusion.** Combining the estimates, we obtain for $x$ where $\chi(x) = 1$:

$$|u(x)| = |w(x)| \leq K \left( \|u\|_{L^2(B)} + \sup_B \max_j \left| \frac{\partial u}{\partial \bar{z}_j} \right| \right),$$

with $K = \max(K_1, K_2, K_3)$. This proves both the estimate and the continuity of $u$.

**Refined estimate (for scaling).** By a linear change of variable centered at $x$, one obtains the local estimate: for any $x \in \mathbb{C}^n$ and $r > 0$,

$$|u(x)| \leq K \left( r^{-n} \|u\|_{L^2(B(x,r))} + r \sup_{B(x,r)} \max_j \left| \frac{\partial u}{\partial \bar{z}_j} \right| \right). \tag{31}$$

This follows from scaling: if $u_r(\zeta) = u(x + r\zeta)$, then $\frac{\partial u_r}{\partial \bar{z}_j}(\zeta) = r \frac{\partial u}{\partial \bar{z}_j}(x + r\zeta)$ and $\|u_r\|_{L^2(B(0,1))} = r^{-n} \|u\|_{L^2(B(x,r))}$. Applying the estimate on the unit ball yields (31).

**Application to the proof of continuity.** Extend $u$ to all of $\mathbb{C}^n$ by setting $u = 0$ outside $B$. Fix $R < 1$ and $r < 1 - R$. For any $x \in B_R = \{|z| < R\}$, the ball $B(x, r) \subset B$. By hypothesis, $\frac{\partial u}{\partial \bar{z}_j}$ is continuous on the compact set $\overline{B_R}$, hence bounded. The estimate (31) applied with a uniform $r$ then implies that $u$ is uniformly approximated by the $L^2$ norm on small balls, from which continuity follows. $\square$
