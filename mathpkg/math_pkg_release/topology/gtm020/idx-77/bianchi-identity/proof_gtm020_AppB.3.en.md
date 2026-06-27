---
role: proof
locale: en
of_concept: bianchi-identity
source_book: gtm020
source_chapter: "Appendix B"
source_section: "B.3"
---
Starting from the definition $K = d\theta - \theta \wedge \theta$, we compute $dK$:
$$
dK = d(d\theta) - d(\theta \wedge \theta) = 0 - (d\theta \wedge \theta - \theta \wedge d\theta)
$$
using $d^2 = 0$ and the graded Leibniz rule. Substituting $d\theta = K + \theta \wedge \theta$:
\begin{align*}
dK &= -(K + \theta \wedge \theta) \wedge \theta + \theta \wedge (K + \theta \wedge \theta) \\
&= -K \wedge \theta - \theta \wedge \theta \wedge \theta + \theta \wedge K + \theta \wedge \theta \wedge \theta \\
&= \theta \wedge K - K \wedge \theta \\
&= [\theta, K].
\end{align*}
This proves the Bianchi identity.
