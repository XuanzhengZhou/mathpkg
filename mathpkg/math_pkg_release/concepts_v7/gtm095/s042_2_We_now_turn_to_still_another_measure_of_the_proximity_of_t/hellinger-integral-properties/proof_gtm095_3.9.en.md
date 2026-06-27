---
role: proof
locale: en
of_concept: hellinger-integral-properties
source_book: gtm095
source_chapter: "3"
source_section: "9.2"
---

# Proof of Lemma 3 (Properties of the Hellinger integral and Kakutani–Hellinger distance)

**Lemma 3.** 1. The Hellinger integral of order $\alpha \in (0, 1)$ (and consequently also $\rho(P, \tilde{P})$) is independent of the choice of the dominating measure $Q$.

2. The function $\rho$ defined by

$$\rho^2(P, \tilde{P}) = \frac{1}{2} E_Q[\sqrt{z} - \sqrt{\tilde{z}}]^2, \quad z = \frac{dP}{dQ},\; \tilde{z} = \frac{d\tilde{P}}{dQ},$$

is a metric on the set of probability measures.

**Proof of 1.** If the measure $Q'$ dominates $P$ and $\tilde{P}$, then $Q'$ also dominates $Q = (P + \tilde{P})/2$. Hence, it suffices to show that if $Q \ll Q'$, then

$$E_Q(z^\alpha \tilde{z}^{1-\alpha}) = E_{Q'}(z')^\alpha (\tilde{z}')^{1-\alpha},$$

where $z' = dP/dQ'$ and $\tilde{z}' = d\tilde{P}/dQ'$.

Let $v = dQ/dQ'$. Then $z' = zv$, $\tilde{z}' = \tilde{z}v$, and

$$E_Q(z^\alpha \tilde{z}^{1-\alpha}) = E_{Q'}(v z^\alpha \tilde{z}^{1-\alpha}) = E_{Q'}(z')^\alpha (\tilde{z}')^{1-\alpha},$$

which establishes independence of the dominating measure.

**Proof of 2.** (i) If $\rho(P, \tilde{P}) = 0$, then $E_Q[\sqrt{z} - \sqrt{\tilde{z}}]^2 = 0$, so $\sqrt{z} = \sqrt{\tilde{z}}$ $Q$-a.e., hence $z = \tilde{z}$ $Q$-a.e., and therefore $P = \tilde{P}$.

(ii) Symmetry: $\rho(P, \tilde{P}) = \rho(\tilde{P}, P)$ is evident from the definition.

(iii) Triangle inequality: Let $P, P'$, and $P''$ be three probability measures, all dominated by $Q$, with densities $z = dP/dQ$, $z' = dP'/dQ$, $z'' = dP''/dQ$. Then

$$\sqrt{2}\,\rho(P, P'') = \|\sqrt{z} - \sqrt{z''}\|_{L^2(Q)} \leq \|\sqrt{z} - \sqrt{z'}\|_{L^2(Q)} + \|\sqrt{z'} - \sqrt{z''}\|_{L^2(Q)} = \sqrt{2}\,\rho(P, P') + \sqrt{2}\,\rho(P', P''),$$

so $\rho(P, P'') \leq \rho(P, P') + \rho(P', P'')$. Thus $\rho$ is a metric.
