---
role: proof
locale: en
of_concept: hellinger-integral
source_book: gtm095
source_chapter: "3"
source_section: "9.2"
---

# Proof of Lemma 3.1 (Independence of Hellinger integral from dominating measure)

**Lemma 3.** 1. The Hellinger integral of order $\alpha \in (0, 1)$ (and consequently also $\rho(P, \tilde{P})$) is independent of the choice of the dominating measure $Q$.

2. The function $\rho$ defined in (13) is a metric on the set of probability measures.

**Proof of part 1.** If the measure $Q'$ dominates $P$ and $\tilde{P}$, then $Q'$ also dominates $Q = (P + \tilde{P})/2$. Hence, it is enough to show that if $Q \ll Q'$, we have

$$E_Q(z^\alpha \tilde{z}^{1-\alpha}) = E_{Q'}(z')^\alpha (\tilde{z}')^{1-\alpha},$$

where $z' = dP/dQ'$ and $\tilde{z}' = d\tilde{P}/dQ'$.

Let us set $v = dQ/dQ'$. Then $z' = zv$, $\tilde{z}' = \tilde{z}v$, and

$$E_Q(z^\alpha \tilde{z}^{1-\alpha}) = E_{Q'}(v z^\alpha \tilde{z}^{1-\alpha}) = E_{Q'}(z')^\alpha (\tilde{z}')^{1-\alpha},$$

which establishes the first assertion.

**Proof of part 2.** If $\rho(P, \tilde{P}) = 0$ we have $z = \tilde{z}$ ($Q$-a.e.) and hence, $P = \tilde{P}$. By symmetry, we evidently have $\rho(P, \tilde{P}) = \rho(\tilde{P}, P)$. Finally, let $P, P'$, and $P''$ be three measures, $P \ll Q$, $P' \ll Q$, and $P'' \ll Q$, with $z = dP/dQ$, $z' = dP'/dQ$, and $z'' = dP''/dQ$. By using the Cauchy–Schwarz inequality,

$$\sqrt{z} - \sqrt{z''} = (\sqrt{z} - \sqrt{z'}) + (\sqrt{z'} - \sqrt{z''}),$$

we obtain

$$\rho(P, P'') \leq \rho(P, P') + \rho(P', P''),$$

so $\rho$ satisfies the triangle inequality. Together with the previous properties, this shows that $\rho$ is a metric.
