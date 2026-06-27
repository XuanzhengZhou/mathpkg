---
role: proof
locale: en
of_concept: "let-be-a-locally-compact-hausdorff-space-let-2"
source_book: gtm025
source_chapter: "Integration Theory Continued"
source_section: "20.45"
---

Each $f \in \mathfrak{C}_0$ is a bounded continuous function and so, since $|\mu|$ is a finite measure (19.13.v), $f$ is in $\mathfrak{L}_1(X, \mathcal{B}(X), |\mu|)$. Thus $L_\mu$ is a linear functional on $\mathfrak{C}_0$. Also (19.38.iv) shows that if $f \in \mathfrak{C}_0$, then

$$|L_\mu(f)| \leq \int_X |f| d|\mu| \leq \|f\|_u \|\mu\|.$$

Thus $L_\mu \in \mathfrak{C}_0^*$ and

$$\|L_\mu\| \leq \|\mu\|.$$

To prove the reverse of inequality (1), use (19.38) to obtain a complex-valued Borel measurable function $f_0$ on $X$ such that $|f_0(x)| = 1$ for all $x \in X$ and

$$\int_X f d\mu = \int_X f f_0 d|\mu|$$

for all $f \in \mathfrak{L}_1(X, \mathcal{B}(X), |\mu|)$. Let $\varepsilon > 0$ be arbitrary. By (13.21), there exists a function $g \in \mathfrak{C}_{00}$ such that $\|

Proof. Obviously if $f \in \mathfrak{C}_0^+$, then

$$I(f) \leq \sup \{ \|L\| \cdot \|g\|_u : g \in \mathfrak{C}_0, |g| \leq f \} = \|L\| \cdot \|f\|_u < \infty.$$ (1)

Thus $I$ is real-valued on $\mathfrak{C}_0^+$. It is also clear that

$$I(\alpha f) = \alpha I(f)$$ (2)

for $f \in \mathfrak{C}_0^+$ and $\alpha \geq 0$. Let us show that $I$ is additive on $\mathfrak{C}_0^+$. Let $f_1, f_2$ be in $\mathfrak{C}_0^+$. If $\varepsilon > 0$ is given, choose $g_1, g_2 \in \mathfrak{C}_0$ such that $|g_j| \leq f_j$ and $|L(g_j)| > I(f_j) - \frac{\varepsilon}{2}$ ($j = 1, 2$). Now write $L(g_j) = \beta_j |L(g_j)|$, where $\beta_j \in K$ and $|\beta_j| = 1$ ($j = 1, 2$), and let $\beta = \beta_2 \bar{\beta}_1$. Then $|\beta| = 1$ and we have

$$I(f_1) + I(f_2) < |L(g_1)| + |L(g_2)| + \varepsilon = \bar{\beta}_1 L(g_1) + \bar{\beta}_2 L(g_2) + \varepsilon$$

$$= |\beta L(g_1) + L(g_2)| + \varepsilon = |L(\beta g_1 + g_2)| + \varepsilon \leq I(f_1 + f_2) + \varepsilon$$

[note that $|\beta g_1 + g_2| \leq |g_1| + |g_2| \leq f_1 + f_2$]. Thus

$$I(f_1)

To prove the reversed inequality, let $\varepsilon > 0$ be given and then select $g \in \mathfrak{C}_0$ such that $\|g\|_u \leq 1$ and $|L(g)| > \|L\| - \varepsilon$. From (i) we have

$$\|L\| - \varepsilon < |L(g)| \leq I(|g|) \leq \|L\|.$$

Hence $\|I\| = \|L\|$. $\square$
