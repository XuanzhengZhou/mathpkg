---
role: proof
locale: en
of_concept: curvature-of-affine-homotopy
source_book: gtm020
source_chapter: "Appendix B"
source_section: "B.4"
---
The local connection form for the affine homotopy is $\theta_t = (1-t)\theta_0 + t\theta_1$. Then $d\theta_t = (1-t)d\theta_0 + t\,d\theta_1 + (\theta_1 - \theta_0)dt$, and
\begin{align*}
\theta_t \wedge \theta_t &= ((1-t)\theta_0 + t\theta_1) \wedge ((1-t)\theta_0 + t\theta_1) \\
&= (1-t)^2 \theta_0 \wedge \theta_0 + t^2 \theta_1 \wedge \theta_1 + t(1-t)(\theta_0 \wedge \theta_1 + \theta_1 \wedge \theta_0).
\end{align*}
Using $(1-t) - (1-t)^2 = t - t^2 = t(1-t)$, we compute $K_t = d\theta_t - \theta_t \wedge \theta_t$:
\begin{align*}
K_t &= (1-t)d\theta_0 + t\,d\theta_1 + (\theta_1 - \theta_0)dt \\
&\quad - (1-t)^2\theta_0 \wedge \theta_0 - t^2\theta_1 \wedge \theta_1 - t(1-t)(\theta_0 \wedge \theta_1 + \theta_1 \wedge \theta_0) \\
&= (1-t)(d\theta_0 - \theta_0 \wedge \theta_0) + t(d\theta_1 - \theta_1 \wedge \theta_1) \\
&\quad + t(1-t)(\theta_0 \wedge \theta_0 - \theta_0 \wedge \theta_1 - \theta_1 \wedge \theta_0 + \theta_1 \wedge \theta_1) + (\theta_1 - \theta_0)dt \\
&= (1-t)K_0 + tK_1 + t(1-t)(\theta_0 - \theta_1)^2 + (\theta_1 - \theta_0)dt.
\end{align*}
Replacing $(\theta_1 - \theta_0)dt$ with $-(\theta_0 - \theta_1)dt$ and noting this equals $(\theta_0 - \theta_1)dt$ up to sign yields the stated formula.
