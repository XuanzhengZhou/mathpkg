---
role: proof
locale: en
of_concept: removable-singularity-criterion
source_book: gtm011
source_chapter: "V"
source_section: "1.2"
---

($\Rightarrow$) If $a$ is a removable singularity, there exists an analytic extension $g$ on $B(a; R)$. Then $\lim_{z \to a} (z-a)f(z) = \lim_{z \to a} (z-a)g(z) = 0 \cdot g(a) = 0$.

($\Leftarrow$) Suppose $f$ is analytic in $\{z: 0 < |z-a| < R\}$ and $\lim_{z \to a} (z-a)f(z) = 0$. Define

$$g(z) = \begin{cases} (z-a)f(z) & \text{if } z \neq a \\ 0 & \text{if } z = a. \end{cases}$$

We show $g$ is analytic on $B(a; R)$ using Morera's Theorem. Let $T$ be a triangle in $B(a; R)$ and let $\Delta$ be the inside of $T$ together with $T$.

Case 1: $a \notin \Delta$. Then $T \sim 0$ in the punctured disk $\{z: 0 < |z-a| < R\}$, so $\int_T g = 0$ by Cauchy's Theorem.

Case 2: $a$ is a vertex of $T$, say $T = [a, b, c, a]$. Let $x \in [a, b]$ and $y \in [c, a]$, and form $T_1 = [a, x, y, a]$ and the polygon $P = [x, b, c, y, x]$. Then $\int_T g = \int_{T_1} g + \int_P g = \int_{T_1} g$ since $P \sim 0$ in the punctured disk. Since $g$ is continuous and $g(a) = 0$, for any $\epsilon > 0$, $x$ and $y$ can be chosen so that $|g(z)| \leq \epsilon/\ell$ for $z$ on $T_1$, where $\ell$ is the length of $T$. Hence $|\int_T g| = |\int_{T_1} g| \leq \epsilon$. Since $\epsilon$ is arbitrary, $\int_T g = 0$.

Case 3: $a \in \Delta$ and $T = [x, y, z, x]$. Consider $T_1 = [x, y, a, x]$, $T_2 = [y, z, a, y]$, $T_3 = [z, x, a, z]$. From Case 2, $\int_{T_j} g = 0$ for $j = 1, 2, 3$, so $\int_T g = \sum \int_{T_j} g = 0$.

By Morera's Theorem, $g$ is analytic on $B(a; R)$. Since $g(a) = 0$, we can write $g(z) = (z-a)h(z)$ where $h$ is analytic on $B(a; R)$. For $z \neq a$, $h(z) = \frac{g(z)}{z-a} = f(z)$, so $h$ is the required analytic extension of $f$ to $a$. Thus $a$ is a removable singularity.
