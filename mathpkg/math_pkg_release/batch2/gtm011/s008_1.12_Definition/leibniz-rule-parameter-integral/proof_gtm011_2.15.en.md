---
role: proof
locale: en
of_concept: leibniz-rule-parameter-integral
source_book: gtm011
source_chapter: "2"
source_section: "2.15"
---

**Continuity of $g$.** Fix $z_0 \in G$ and let $\epsilon > 0$. Since $\{\gamma\} \times \{z_0\}$ is compact, $\varphi$ is uniformly continuous in a neighborhood. Choose a compact neighborhood $K$ of $z_0$ in $G$. Then $\varphi$ is uniformly continuous on the compact set $\{\gamma\} \times K$. Hence there exists $\delta > 0$ such that $|\varphi(w, z) - \varphi(w, z_0)| < \epsilon / V(\gamma)$ whenever $|z - z_0| < \delta$ and $w \in \{\gamma\}$. Then for $|z - z_0| < \delta$,

$$|g(z) - g(z_0)| \leq \int_{\gamma} |\varphi(w, z) - \varphi(w, z_0)| |dw| \leq V(\gamma) \cdot \frac{\epsilon}{V(\gamma)} = \epsilon.$$

Hence $g$ is continuous at $z_0$.

**Analyticity and derivative formula.** Fix $z_0 \in G$. For $z \neq z_0$,

$$\frac{g(z) - g(z_0)}{z - z_0} = \int_{\gamma} \frac{\varphi(w, z) - \varphi(w, z_0)}{z - z_0} dw.$$

By the uniform continuity of $\frac{\partial \varphi}{\partial z}$ on $\{\gamma\} \times K$, the difference quotient converges uniformly on $\{\gamma\}$ to $\frac{\partial \varphi}{\partial z}(w, z_0)$. By the lemma on uniform convergence and line integrals, we can pass the limit through the integral:

$$g'(z_0) = \int_{\gamma} \frac{\partial \varphi}{\partial z}(w, z_0) \, dw.$$

Since the right side is continuous in $z_0$ (as shown in the first part of the proof), $g'$ is continuous, hence $g$ is analytic.
