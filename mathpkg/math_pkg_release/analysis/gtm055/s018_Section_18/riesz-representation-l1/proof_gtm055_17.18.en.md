---
role: proof
locale: en
of_concept: riesz-representation-l1
source_book: gtm055
source_chapter: "17"
source_section: "18"
---

Clearly if $g$ is essentially bounded and $f$ is integrable, then

$$\left| \int_X f g d\mu \right| \leq \| g \|_\infty \| f \|_1,$$

so that $\|\varphi_g\| \leq \|g\|_\infty$. Hence, as before, it suffices to show that for an arbitrary $\varphi$ in $\mathcal{L}_1(X)^*$ there exists a function $g$ in $\mathcal{L}_\infty(X)$ with $\|g\|_\infty \leq \|\varphi\|$ such that $\varphi = \varphi_g$.

The proof proceeds by taking an increasing sequence $\{X_n\}$ of sets of finite measure whose union is $X$, applying the finite measure case treated in Theorem 17.5 on each $X_n$, and patching the resulting functions together. The $\sigma$-finiteness hypothesis makes such patching possible.
