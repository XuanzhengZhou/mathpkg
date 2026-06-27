---
role: proof
locale: en
of_concept: barrier-implies-boundary-limit
source_book: gtm011
source_chapter: "X"
source_section: "4"
---

*Proof.* Let $\{\psi_r : r > 0\}$ be a barrier for $G$ at $a$ and for convenience assume $a \neq \infty$; also assume that $f(a) = 0$ (otherwise consider the function $f - f(a)$). Let $\epsilon > 0$ and choose $\delta > 0$ such that $|f(w)| < \epsilon$ whenever $w \in \partial_\infty G$ and $|w - a| < 2\delta$; let $\psi = \psi_\delta$. Let $\hat{\psi} : G \to \mathbb{R}$ be defined by $\hat{\psi}(z) = \psi(z)$ for $z$ in $G(a; \delta)$ and $\hat{\psi}(z) = 1$ for $z$ in $G - B(a; \delta)$. Then $\hat{\psi}$ is superharmonic. If $|f(w)| \leq M$ for all $w$ in $\partial_\infty G$, then $-M\hat{\psi} - \epsilon$ is subharmonic.

**Claim.** $-M\hat{\psi} - \epsilon$ is in $\mathcal{P}(f, G)$.

If $w \in \partial_\infty G - B(a; \delta)$ then $\limsup_{z \to w} [-M\hat{\psi}(z) - \epsilon] = -M - \epsilon < f(w)$. Because $\hat{\psi}(z) \geq 0$, it follows that $\limsup_{z \to w} [-M\hat{\psi}(z) - \epsilon] \leq -\epsilon$ for all $w$ in $\partial_\infty G$. In particular, if $w \in \partial_\infty G \cap B(a; \delta)$ then $\limsup_{z \to w} [-M\hat{\psi}(z) - \epsilon] \leq -\epsilon < f(w)$ by the choice of $\delta$. This substantiates the Claim. Hence

$$-M\hat{\psi}(z) - \epsilon \leq u(z)$$

for all $z$ in $G$. By symmetry, an analogous argument with $+M\hat{\psi} + \epsilon$ gives an upper bound, so

$$|u(z)| \leq M\hat{\psi}(z) + \epsilon$$

for all $z \in G$. Since $\hat{\psi}(z) \to 0$ as $z \to a$ and $\epsilon > 0$ was arbitrary, it follows that $\lim_{z \to a} u(z) = 0 = f(a)$. $\square$
