---
role: proof
locale: en
of_concept: extinction-probability
source_book: gtm017
source_chapter: "III"
source_section: "a"
---
The probability of extinction by time $t$ is $e_t = \varphi^{(t)}(0)$. Since $e_t$ is nondecreasing and bounded, $e = \lim e_t$ exists and satisfies $e = \varphi(e)$.

Note $\varphi(1)=1$, so $\zeta=1$ is always a solution. If $\mu = \varphi(1) \leq 1$, then $\varphi(s) > s$ for $0 \leq s < 1$ (except $\varphi(s) \equiv s$), forcing $e=1$.

If $\mu > 1$, then $\varphi(s)$ is strictly increasing. By the mean value theorem, $\varphi(\sigma) = (\varphi(1)-\varphi(\zeta))/(1-\zeta) = 1$ for some $\sigma \in (\zeta, 1)$. Since $\varphi(1) > 1$ and $\varphi$ is nondecreasing, there exists a unique $\zeta \in [0,1)$ such that $\zeta = \varphi(\zeta)$ and $\zeta < 1$.
