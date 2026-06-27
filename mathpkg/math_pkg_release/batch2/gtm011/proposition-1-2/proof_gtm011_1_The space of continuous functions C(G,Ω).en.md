---
role: proof
locale: en
of_concept: proposition-1-2
source_book: gtm011
source_chapter: "Compactness and Convergence in the Space of Analytic Functions"
source_section: "1. The space of continuous functions C(G,Ω)"
---

Proof. For each positive integer $n$ let

$$K_n = \{z : |z| \leq n\} \cap \left\{z : d(z, \mathbb{C} - G) \geq \frac{1}{n}\right\};$$

since $K_n$ is clearly bounded and it is the intersection of two closed subsets of $\mathbb{C}$, $K_n$ is compact. Also, the set

$$\{z : |z| < n + 1\} \cap \left\{z : d(z, \mathbb{C} - G) > \frac{1}{n + 1}\right\}$$

is open, contains $K_n$, and is contained in $K_{n+1}$. This gives that (a) is satisfied. Since it easily follows that $G = \bigcup_{n=1}^{\infty} K_n$ we also get that $G = \bigcup_{n=1}^{\infty} \text{int} K_n$; so if $K$ is a compact subset of $G$ the sets $\{\text{int} K_n\}$ form an open cover of $K$. This gives part (b).

To see part (c) note that the unbounded component of $\mathbb{C}_\infty - K_n$ ($\supset \mathbb{C}_\infty - G$) must contain $\infty$ and must therefore contain the component of $\mathbb{C}_\infty - G$ which contains $\infty$. Also the unbounded component contains $\{z : |z| > n\}$. So if $D$ is a bounded component of $\mathbb{C}_\infty - K_n$ it contains a point $z$ with $d(z, \mathbb{C} - G) < \frac{1}{n}$. But by definition this gives a point $w$ in $\mathbb{C} - G$ with $|w - z| < \frac{1}{n}$. But then $z \in B\left(w; \frac{1}{n}\right) \subset \mathbb{C}_\infty - K_n$; since disks are connected and $z$ is in the component $D$ of $\mathbb{C}_\infty - K_n$, $B\left(w; \frac{1}{n}\right)

Proof. It is clear that $\rho(f, g) = \rho(g, f)$. Also, since each $\rho_n$ satisfies the triangle inequality, the preceding lemma can be used to show that $\rho$ satisfies the triangle inequality. Finally, the fact that $G = \bigcup_{n=1}^{\infty} K_n$ gives that $f = g$ whenever $\rho(f, g) = 0$.

The next lemma concerns subsets of $C(G, \Omega) \times C(G, \Omega)$ and is very useful because it gives insight into the behavior of the metric $\rho$. Those who know the appropriate definitions will recognize that this lemma says that two uniformities are equivalent.
