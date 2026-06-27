---
role: proof
locale: en
of_concept: adjoint-action-chevalley-lattice
source_book: gtm009
source_chapter: "VII"
source_section: "25.5"
---

**Proof.** The proof proceeds by induction on $m$, using the commutation relations of the Chevalley basis given in Theorem 25.2. Recall that $[x_{\alpha}, x_{\beta}] = c_{\alpha\beta} x_{\alpha+\beta}$ when $\alpha+\beta \in \Phi$, with $c_{\alpha\beta} = \pm(r+1)$ and $r$ the largest integer such that $\beta-r\alpha \in \Phi$.

For $m=1$, we have $\operatorname{ad} x_{\alpha}(x_{\beta}) = c_{\alpha\beta} x_{\alpha+\beta} = \pm(r+1) x_{\alpha+\beta} = \pm \binom{r+1}{1} x_{\alpha+\beta}$, which matches the formula.

Assume the formula holds for $m$. Then:

$$\frac{(\operatorname{ad} x_{\alpha})^{m+1}}{(m+1)!}(x_{\beta}) = \frac{1}{m+1} \operatorname{ad} x_{\alpha} \left( \frac{(\operatorname{ad} x_{\alpha})^{m}}{m!}(x_{\beta}) \right)$$

$$= \frac{1}{m+1} \operatorname{ad} x_{\alpha} \left( \pm \binom{r+m}{m} x_{\beta+m\alpha} \right)$$

$$= \pm \frac{1}{m+1} \binom{r+m}{m} c_{\alpha, \beta+m\alpha} \, x_{\beta+(m+1)\alpha}.$$

If $\beta+(m+1)\alpha \in \Phi$, then the $\alpha$-string through $\beta+m\alpha$ starts at $\beta-r\alpha$ (so the new $r' = r+m$) and $c_{\alpha, \beta+m\alpha} = \pm (r+m+1)$. Thus:

$$\frac{(\operatorname{ad} x_{\alpha})^{m+1}}{(m+1)!}(x_{\beta}) = \pm \frac{1}{m+1} \binom{r+m}{m} (r+m+1) \, x_{\beta+(m+1)\alpha}$$

$$= \pm \binom{r+m+1}{m+1} x_{\beta+(m+1)\alpha},$$

since $\frac{1}{m+1} \binom{r+m}{m}(r+m+1) = \binom{r+m+1}{m+1}$.

If $\beta+(m+1)\alpha \notin \Phi$, then $c_{\alpha, \beta+m\alpha} = 0$ and the expression vanishes.

Since $\binom{r+m}{m}$ is always an integer, the divided power $\frac{(\operatorname{ad} x_{\alpha})^{m}}{m!}$ maps the Chevalley basis elements $x_{\beta}$ to integer multiples of other basis elements (or zero), hence preserves the $\mathbb{Z}$-span $L(\mathbb{Z})$.
