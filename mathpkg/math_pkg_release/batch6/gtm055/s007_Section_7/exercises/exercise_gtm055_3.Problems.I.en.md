---
role: exercise
locale: en
chapter: "3"
section: "Problems"
exercise_number: I
---
Let $\mathcal{G}_m$ denote the grid of lines parallel to the real axis and to the imaginary axis by amounts $km$, $k \in \mathbb{Z}$. The closed strip bounded by two adjacent horizontal lines, $\mathbb{R} + kmi$ and $\mathbb{R} + (k + 1)mi$, in the grid is a horizontal strip of $\mathcal{G}_m$. Likewise, a vertical strip of $\mathcal{G}_m$ is a closed strip bounded by two adjacent vertical lines in $\mathcal{G}_m$. Finally, a square region $Q$ is a square region of $\mathcal{G}_m$ if it is the intersection of a horizontal strip of $\mathcal{G}_m$ and a vertical strip of $\mathcal{G}_m$, and a complex number $\lambda_0$ is a vertex of $\mathcal{G}_m$ if it is a vertex of some square region of $\mathcal{G}_m$.

Now let $\{Q_1, \ldots, Q_n\}$ be an arbitrary finite, nonempty collection of square regions of a grid $\mathcal{G}_m$, and set $L = Q_1 \cup \cdots \cup Q_n$. Show that the boundary $\partial L$ can be parametrized as a formal sum $\pi = \pi_1 + \cdots + \pi_m$ of closed polygonal arcs in such a way that the winding number of $\pi$ is one at each point of $L^\circ$ and zero on the complement of $L$.

(Hint: Let $\gamma_i$ denote a standard parametrization of $\partial Q_i$, $i = 1, \ldots, n$, set $\gamma = \sum_{i=1}^{n} \gamma_i$, and verify that the winding number of $\gamma$ is one in the interior of each $Q_i$ and zero outside $L$. Then write $\gamma$ as a formal sum of all of the edges of all of the squares $\partial Q_i$, and thus as a formal sum of directed line segments. Remove all matched pairs of oppositely directed line segments, and show that this removes all line segments that meet $L^\circ$, so that what is left is really a parametrization of $\partial L$ given as a formal sum of directed line segments. Then apply Problem I.)
