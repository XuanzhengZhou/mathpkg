---
role: proof
locale: en
of_concept: morse-unique-critical-point-k-cell
source_book: gtm033
source_chapter: "6"
source_section: "6.3"
---

# Proof of Morse Cell Attachment for a Single Critical Point

Let $f(z) = c$, $a < c < b$. To prove the theorem it suffices to prove it for the restriction of $f$ to $f^{-1}[a',b']$ for any $a', b'$ such that $a < a' < c < b' < b$, by the regular interval Theorem 2.2 applied to $f^{-1}[a,a']$ and $f^{-1}[b,b']$. Moreover, we can assume $c = 0$, replacing $f$ by $f(x) - c$ otherwise.

Let $(\varphi, U)$ be a chart at $z$ as in Morse's lemma. We write $\mathbb{R}^n = \mathbb{R}^k \times \mathbb{R}^{n-k}$; thus $\varphi$ maps $U$ diffeomorphically onto an open set $V \subset \mathbb{R}^k \times \mathbb{R}^{n-k}$, and

$$f \circ \varphi^{-1}(x, y) = -|x|^2 + |y|^2$$

for $(x, y) \in V$, where $x \in \mathbb{R}^k$, $y \in \mathbb{R}^{n-k}$.

Let $g(x,y) = -|x|^2 + |y|^2$. Set

$$B^k = D^k(\sqrt{2\varepsilon}) \times \{0\} \subset g^{-1}(-\varepsilon).$$

The $k$-cell $e^k$ will be $\varphi^{-1}(B^k)$.

A deformation of $f^{-1}[-\varepsilon, \varepsilon]$ to $f^{-1}(-\varepsilon) \cup e^k$ is made by patching together two deformations. First consider the set

$$\Gamma_1 = D^k(\sqrt{2\varepsilon}) \times D^{n-k}(\sqrt{2\varepsilon}).$$

In $\Gamma_1 \cap g^{-1}[-\varepsilon, \varepsilon]$ a deformation is obtained by moving $(x, y)$ at constant speed along the interval joining $(x, y)$ to the point $(x, sy) \in g^{-1}(-\varepsilon) \cup B^k$, $s \in \mathbb{R}$ where

$$s = s(x, y) = \begin{cases} 0 & \text{if } |x|^2 < \varepsilon \\ \sqrt{|x|^2 - \varepsilon}/|y| & \text{if } |x| \geqslant \varepsilon. \end{cases}$$

Note that these intervals are closures of solution curves of the vector field $X(x, y) = (0, -2y)$. This deformation is transported to $\varphi^{-1}(\Gamma_1)$ via conjugation by $\varphi$.

Outside the set

$$\Gamma_2 = D^k(\sqrt{2\varepsilon}) \times D^{n-k}(\sqrt{2\varepsilon})$$

the deformation moves each point at constant speed along the flow line of the vector field $-\operatorname{grad} g$ so that it reaches $g^{-1}(-\varepsilon) \cup B^k$ in unit time. (The speed of each point is the length of its path under the deformation.) This deformation is transported to $U - \varphi^{-1}(\Gamma_2)$ by $\varphi$; it is then extended over $M - \varphi^{-1}(\Gamma_2)$ by following flow lines of $-\operatorname{grad} f$. Each such flow line must eventually reach $f^{-1}(-\varepsilon)$, for it can never enter $\Gamma_2$ because $|x|$ increases and $|y|$ has a positive lower bound in the compact set

$$f^{-1} [-\varepsilon, \varepsilon] - \operatorname{Int} \varphi^{-1} \Gamma_2.$$

To extend the deformation to points of $\Gamma_2 - \Gamma_1$ it suffices to find a vector field on $\Gamma$ which agrees with $X$ in $\Gamma_1$ and with $-\operatorname{grad} g$ in $\Gamma - \Gamma_2$. Such a field is

$$Y(x, y) = 2(\mu(x, y)\, x, -y)$$

where the $C^\infty$ map $\mu: \mathbb{R}^k \times \mathbb{R}^{n-k} \to [0,1]$ vanishes in $\Gamma_1$ and equals $1$ outside $\Gamma_2$. It is easy to see that each flow line of $Y$ which starts at a point of

$$(\Gamma_2 - \Gamma_1) \cap g^{-1} [-\varepsilon, \varepsilon]$$

must reach $g^{-1}(-\varepsilon)$ because $|x|$ is non-decreasing along flow lines.

The global deformation of $f^{-1}[-\varepsilon, \varepsilon]$ into $f^{-1}(-\varepsilon) \cup e^k$ is obtained by moving each point of $\Gamma$ at constant speed along the flow line of $Y$ until it reaches $g^{-1}(-\varepsilon) \cup B^k$ in unit time and transporting this motion to $M$ via $\varphi$; while each point of $M - \varphi^{-1}(\Gamma)$ moves at constant speed along the flow line of $-\operatorname{grad} f$ until it reaches $f^{-1}(-\varepsilon)$ in unit time. Of course points on $f^{-1}(-\varepsilon) \cup e^k$ stay fixed.

Thus $f^{-1}[-\varepsilon, \varepsilon]$ deformation retracts onto $f^{-1}(-\varepsilon) \cup e^k$, and by Theorem 2.2, $M$ deformation retracts onto $f^{-1}(a) \cup e^k$.
