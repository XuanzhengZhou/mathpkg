---
role: proof
locale: en
of_concept: wiener-process-karhunen-loeve
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

For the Wiener process, $r(t,\tau) = \min(t,\tau)$. The eigenvalue equation gives
$$\varphi(t) = \lambda\left[\int_0^t \tau\varphi(\tau)d\tau + t\int_t^1 \varphi(\tau)d\tau\right].$$
Evaluating at $t=0$ gives $\varphi(0)=0$. Differentiating: $\varphi'(t) = \lambda\int_t^1 \varphi(\tau)d\tau$, so $\varphi'(1)=0$. Differentiating again: $\varphi''(t) + \lambda\varphi(t) = 0$.

The general solution is $\varphi(t) = A\sin(\sqrt{\lambda}t) + B\cos(\sqrt{\lambda}t)$. The condition $\varphi(0)=0$ forces $B=0$. The condition $\varphi'(1)=0$ gives $\cos(\sqrt{\lambda})=0$, so $\sqrt{\lambda} = (k+1/2)\pi$ for $k=1,2,\ldots$. Thus $\lambda_k = (k+1/2)^2\pi^2$ and $\varphi_k(t) = A_k\sin((k+1/2)\pi t)$. Normalizing gives $A_k = \sqrt{2}$.
