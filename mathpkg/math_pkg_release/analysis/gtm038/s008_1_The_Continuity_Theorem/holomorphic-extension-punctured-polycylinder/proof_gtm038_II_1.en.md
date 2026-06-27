---
role: proof
locale: en
of_concept: holomorphic-extension-punctured-polycylinder
source_book: gtm038
source_chapter: "II. Domains of Holomorphy"
source_section: "1. The Continuity Theorem"
---

**1.** First we show that $G$ is a region (connected open set). If $z_\lambda = (z_1^{(\lambda)}, \ldots, z_n^{(\lambda)})$ for $\lambda = 1, 2$ are given, then the points on the distinguished boundary (torus) also lie in $G$. For $\lambda = 1, 2$ we can connect $z_\lambda$ on the torus $T_{z_\lambda} \subset G$ with its torus projection $\tau(z_\lambda)$.

Define $\varphi_\lambda : I \to \mathbb{C}^n$ by $\varphi_\lambda(t) := (z_1^{(\lambda)}(t), \ldots, z_n^{(\lambda)}(t))$ with
$$z_\nu^{(\lambda)}(t) := |z_\nu^{(\lambda)}| + t \cdot \bigl(\max(|z_\nu^{(1)}|, |z_\nu^{(2)}|) - |z_\nu^{(\lambda)}|\bigr)$$
for $\lambda = 1, 2$, $\nu = 1, \ldots, n$. Clearly $|z_\nu^{(\lambda)}(t)| \geq |z_\nu^{(\lambda)}| > r_\nu^0$ for $\nu = 1, \ldots, n$, so $\varphi_\lambda(t) \in G$ for $t \in I$ and $\lambda = 1, 2$.

Define
$$\varphi(t) := \begin{cases} \varphi_1(2t) & 0 \leqslant t \leqslant \tfrac{1}{2}, \\ \varphi_2(2 - 2t) & \tfrac{1}{2} \leqslant t \leqslant 1. \end{cases}$$
Then $\varphi$ joins $\tau(z_1)$ with $\tau(z_2)$. Hence $G$ is connected, and so is a domain.

**2.** For $\nu = 1, \ldots, n$ let $E_{(\nu)} := \{ z_\nu \in \mathbb{C} : |z_\nu| < 1 \}$. Choose $z_n^0 \in \mathbb{C}$ with $r_n^0 < |z_n^0| < 1$ and define the torus cross-section
$$T(z_n) := \{ (z_1, \ldots, z_{n-1}, z_n) \in \mathbb{C}^n : |z_\nu| = r_\nu^0 + \varepsilon \text{ for } \nu = 1, \ldots, n-1 \}.$$

The set $\tilde{P} \cap G$ is connected. The proposition now follows from the Continuity Theorem applied to suitable choices of $B$ and $\tilde{P}$.
