---
role: proof
locale: en
of_concept: homogeneous-potential-orbit-scaling
source_book: gtm060
source_chapter: "2"
source_section: "11"
---

**Proof.** Let $\mathbf{r}(t)$ satisfy $m \ddot{\mathbf{r}} = -\partial U / \partial \mathbf{r}$ with $U(\alpha \mathbf{r}) = \alpha^\nu U(\mathbf{r})$. Introduce scaled variables $t_1 = \alpha t$ and consider $\mathbf{r}_1(t) = \alpha \mathbf{r}(t)$. Then $\partial U / \partial \mathbf{r}_1 = \alpha^{\nu-1} \partial U / \partial \mathbf{r}$. The equation of motion transforms as
$$m \frac{d^2 \mathbf{r}_1}{dt_1^2} = m \alpha \frac{d^2 \mathbf{r}}{d(\alpha t)^2} = \frac{m}{\alpha} \ddot{\mathbf{r}} = -\frac{1}{\alpha} \frac{\partial U}{\partial \mathbf{r}}.$$

On the other hand, $-\partial U(\mathbf{r}_1) / \partial \mathbf{r}_1 = -\alpha^{\nu-1} \partial U(\mathbf{r}) / \partial \mathbf{r}$. Equating gives the scaling condition, and one can choose $\alpha$ so that $\mathbf{r}_1(t_1)$ satisfies the same equation of motion. The ratio of circulation times follows from the scaling of the time variable.

For $\nu = -1$ (Newtonian potential): $U \propto 1/r$, which yields $T^2 \propto a^3$ (Kepler's third law). For $\nu = 2$ (harmonic oscillator): $U \propto r^2$, which yields period independent of amplitude (isochronicity).
