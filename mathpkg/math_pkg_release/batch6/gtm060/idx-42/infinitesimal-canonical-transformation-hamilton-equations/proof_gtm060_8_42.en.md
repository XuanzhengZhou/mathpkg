---
role: proof
locale: en
of_concept: infinitesimal-canonical-transformation-hamilton-equations
source_book: gtm060
source_chapter: "8"
source_section: "42"
---

**Proof.** The result follows directly from formula (4). From the generating function

$$\mathbf{P}\mathbf{q} + \varepsilon S(\mathbf{P}, \mathbf{q}; \varepsilon)$$

we have $\mathbf{p} = \mathbf{P} + \varepsilon \frac{\partial S}{\partial \mathbf{q}}$ and $\mathbf{Q} = \mathbf{q} + \varepsilon \frac{\partial S}{\partial \mathbf{P}}$. As $\varepsilon \to 0$, we obtain $\mathbf{P} \to \mathbf{p}$ and $\mathbf{Q} \to \mathbf{q}$. Differentiating with respect to $\varepsilon$ at $\varepsilon = 0$ yields

$$\left. \frac{d\mathbf{P}}{d\varepsilon} \right|_0 = -\frac{\partial S}{\partial \mathbf{q}}\bigg|_{\varepsilon=0} = -\frac{\partial H}{\partial \mathbf{q}}, \qquad \left. \frac{d\mathbf{Q}}{d\varepsilon} \right|_0 = \frac{\partial S}{\partial \mathbf{P}}\bigg|_{\varepsilon=0} = \frac{\partial H}{\partial \mathbf{p}},$$

where $H(\mathbf{p}, \mathbf{q}) = S(\mathbf{p}, \mathbf{q}, 0)$. These are precisely Hamilton's canonical equations.
