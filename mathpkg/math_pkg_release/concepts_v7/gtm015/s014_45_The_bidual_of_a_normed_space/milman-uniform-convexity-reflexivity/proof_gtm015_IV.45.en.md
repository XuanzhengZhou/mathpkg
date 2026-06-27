---
role: proof
locale: en
of_concept: milman-uniform-convexity-reflexivity
source_book: gtm015
source_chapter: "IV"
source_section: "45"
---

# Proof of Milman's Theorem on Uniformly Convex Spaces (Sketch)

A Banach space $E$ is uniformly convex if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for all $x, y \in E$ with $\|x\| \leq 1$, $\|y\| \leq 1$, and $\|x - y\| \geq \varepsilon$, we have $\|\frac{x+y}{2}\| \leq 1 - \delta$.

**Proof outline (D.P. Mil'man):**

1. Let $B$ be the closed unit ball of $E$ and $B''$ the closed unit ball of $E''$. By Goldstine's theorem (45.3), $B$ (identified with its canonical image in $E''$) is weak* dense in $B''$.

2. For any $\varphi \in B''$, we must show $\varphi \in B$ (i.e., $\varphi$ is the canonical image of some $x \in B$). Since $B$ is weak* dense in $B''$, there exists a net $(x_\alpha)$ in $B$ such that $x_\alpha \to \varphi$ in the weak* topology $\sigma(E'', E')$.

3. Using uniform convexity, one shows that the net $(x_\alpha)$ is actually Cauchy in the norm topology. The key estimate: for any $f \in E'$ with $\|f\| = 1$ such that $f$ almost exposes $\varphi$, uniform convexity forces the $x_\alpha$ to cluster in norm.

4. More precisely, for any $\varepsilon > 0$, choose $f \in E'$ with $\|f\| = 1$ and $\varphi(f) > 1 - \delta(\varepsilon)$ (where $\delta(\varepsilon)$ is the modulus of convexity). For sufficiently large $\alpha, \beta$, we have $x_\alpha(f) > 1 - \delta$ and $x_\beta(f) > 1 - \delta$. Then
$$1 - \delta < \frac{1}{2}(x_\alpha + x_\beta)(f) \leq \left\|\frac{x_\alpha + x_\beta}{2}\right\|.$$
By uniform convexity, this forces $\|x_\alpha - x_\beta\| < \varepsilon$. Thus $(x_\alpha)$ is norm-Cauchy.

5. Since $E$ is complete, $x_\alpha \to x$ in norm for some $x \in B$. Then $x_\alpha \to x$ also in the weak* topology, so $\varphi = x \in B$. Hence $B'' = B$ and $E$ is reflexive. $\square$
