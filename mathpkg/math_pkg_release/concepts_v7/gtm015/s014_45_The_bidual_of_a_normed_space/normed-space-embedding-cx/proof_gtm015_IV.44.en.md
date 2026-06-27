---
role: proof
locale: en
of_concept: normed-space-embedding-cx
source_book: gtm015
source_chapter: "IV"
source_section: "44"
---

# Proof that Every Normed Space Embeds Isometrically into C(X)

Let $E$ be a normed space over $\mathbb{K}$. Let $B = \{f \in E' : \|f\| \leq 1\}$ be the closed unit ball of the dual space $E'$. By the Banach-Alaoglu theorem (44.12), $B$ is compact in the weak* topology $\sigma(E', E)$. Set $\mathcal{X} = B$ with the weak* topology; then $\mathcal{X}$ is a compact Hausdorff space.

Define the evaluation map $\Phi: E \to \mathcal{C}(\mathcal{X})$ by
$$(\Phi(x))(f) = f(x) \quad (x \in E,\; f \in \mathcal{X} = B).$$

For each $x \in E$, the function $\Phi(x): \mathcal{X} \to \mathbb{K}$ is continuous (by definition of the weak* topology: evaluation at $x$ is a weak* continuous linear functional on $E'$, hence its restriction to $B$ is continuous). Thus $\Phi(x) \in \mathcal{C}(\mathcal{X})$.

**Linearity:** $\Phi(\alpha x + \beta y)(f) = f(\alpha x + \beta y) = \alpha f(x) + \beta f(y) = (\alpha \Phi(x) + \beta \Phi(y))(f)$.

**Isometry:** For any $x \in E$,
$$\|\Phi(x)\|_{\infty} = \sup_{f \in B} |f(x)| = \|x\|,$$
by the Hahn-Banach theorem (corollary: $\|x\| = \sup\{|f(x)| : f \in E', \|f\| \leq 1\}$). Thus $\Phi$ is a linear isometry of $E$ into $\mathcal{C}(\mathcal{X})$. $\square$
