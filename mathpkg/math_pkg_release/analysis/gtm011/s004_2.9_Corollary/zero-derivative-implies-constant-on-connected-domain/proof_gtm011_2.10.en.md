---
role: proof
locale: en
of_concept: zero-derivative-implies-constant-on-connected-domain
source_book: gtm011
source_chapter: "2"
source_section: "2.10"
---

Fix $z_0$ in $G$ and let $\omega_0 = f(z_0)$. Put

$$A = \{z \in G : f(z) = \omega_0\}.$$

We will show that $A = G$ by proving $A$ is both open and closed in $G$.

**$A$ is closed in $G$:** Let $z \in G$ and let $\{z_n\} \subset A$ be such that $z = \lim z_n$. Since $f(z_n) = \omega_0$ for each $n$ and $f$ is continuous (differentiability implies continuity), we have

$$f(z) = f\left(\lim_{n \to \infty} z_n\right) = \lim_{n \to \infty} f(z_n) = \omega_0.$$

Thus $z \in A$, so $A$ contains all its limit points in $G$ and is therefore closed in $G$.

**$A$ is open in $G$:** Let $z \in A$. Since $G$ is open, there exists $r > 0$ such that $B(z; r) \subset G$. For any $w \in B(z; r)$, define $g(t) = f(z + t(w - z))$ for $t \in [0, 1]$. Then $g$ is differentiable on $[0, 1]$ and

$$g'(t) = f'(z + t(w - z)) \cdot (w - z) = 0$$

for all $t \in [0, 1]$, since $f'(z) = 0$ for all $z \in G$. Hence $g$ is constant on $[0, 1]$, which gives $g(0) = g(1)$, i.e., $f(z) = f(w)$. Therefore $f(w) = \omega_0$ for all $w \in B(z; r)$, so $B(z; r) \subset A$. This shows $A$ is open in $G$.

Since $G$ is connected, $A$ is non-empty ($z_0 \in A$), and $A$ is both open and closed in $G$, we must have $A = G$. Thus $f(z) = \omega_0$ for all $z \in G$, so $f$ is constant.
