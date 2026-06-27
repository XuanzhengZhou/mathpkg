---
role: proof
locale: en
of_concept: compact-exhaustion-of-open-sets-in-complex-plane
source_book: gtm011
source_chapter: "VII"
source_section: "1.2"
---

For each positive integer $n$ let

$$K_n = \{z : |z| \leq n\} \cap \left\{z : d(z, \mathbb{C} - G) \geq \frac{1}{n}\right\};$$

since $K_n$ is clearly bounded and it is the intersection of two closed subsets of $\mathbb{C}$, $K_n$ is compact. Also, the set

$$\{z : |z| < n + 1\} \cap \left\{z : d(z, \mathbb{C} - G) > \frac{1}{n + 1}\right\}$$

is open, contains $K_n$, and is contained in $K_{n+1}$. This gives that (a) is satisfied. Since it easily follows that $G = \bigcup_{n=1}^{\infty} K_n$ we also get that $G = \bigcup_{n=1}^{\infty} \operatorname{int} K_n$; so if $K$ is a compact subset of $G$ the sets $\{\operatorname{int} K_n\}$ form an open cover of $K$. This gives part (b).

To see part (c) note that the unbounded component of $\mathbb{C}_\infty - K_n$ (which contains $\mathbb{C}_\infty - G$) must contain $\infty$ and must therefore contain the component of $\mathbb{C}_\infty - G$ which contains $\infty$. Also the unbounded component contains $\{z : |z| > n\}$. So if $D$ is a bounded component of $\mathbb{C}_\infty - K_n$ it contains a point $z$ with $d(z, \mathbb{C} - G) < \frac{1}{n}$. But by definition this gives a point $w$ in $\mathbb{C} - G$ with $|w - z| < \frac{1}{n}$. But then $z \in B\left(w; \frac{1}{n}\right) \subset \mathbb{C}_\infty - K_n$; since disks are connected and $z$ is in the component $D$ of $\mathbb{C}_\infty - K_n$, $B\left(w; \frac{1}{n}\right) \subset D$. But $w \in \mathbb{C} - G \subset \mathbb{C}_\infty - G$. Hence $D$ contains a point of $\mathbb{C}_\infty - G$ and must therefore contain the component of $\mathbb{C}_\infty - G$ which contains $w$.
