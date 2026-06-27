---
role: proof
locale: en
of_concept: moore-graphs-type-rho-2-strongly-isovalent
source_book: gtm054
source_chapter: "IX"
source_section: "46"
---

Let $\Gamma$ be a Moore graph of type $(\rho, 2)$. Thus $\rho = n_1$ and by Theorem E15 it suffices to prove that $p_{11}^1$ and $p_{11}^2$ are constant. Let $x_0 \in V$ and let $V_0, V_1$, and $V_2$ be the distance partition with respect to $x_0$ (so $V_i = \{v \in V : d(x_0, v) = i\}$). Let $y \in V_1$ and $z \in V_2$. Due to the structure of a Moore graph (each vertex in $V_i$ is incident with exactly one vertex in $V_{i-1}$ and $\rho - 1$ vertices in $V_{i+1}$, while vertices in $V_\delta$ are adjacent only within $V_\delta$ and to $V_{\delta-1}$), we have $p_{11}^1(x_0, y) = 0$ and $p_{11}^2(x_0, z) = 1$. The result follows since $x_0$ was chosen arbitrarily, $y$ was an arbitrary first associate of $x_0$, and $z$ was an arbitrary second associate of $x_0$.
