---
role: proof
locale: en
of_concept: inner-automorphism-of-lie-algebra
source_book: gtm009
source_chapter: "I"
source_section: "2.3"
---
Suppose $\delta^k = 0$. Then calculate:
$$\exp \delta(x) \exp \delta(y) = \left( \sum_{i=0}^{k-1} \frac{\delta^i x}{i!} \right) \left( \sum_{j=0}^{k-1} \frac{\delta^j y}{j!} \right)$$
$$= \sum_{n=0}^{2k-2} \left( \sum_{i=0}^{n} \frac{\delta^i x}{i!} \frac{\delta^{n-i} y}{(n-i)!} \right)$$
$$= \sum_{n=0}^{2k-2} \frac{\delta^n(xy)}{n!} \quad \text{(Leibniz rule for } \delta^n \text{)}$$
$$= \sum_{n=0}^{k-1} \frac{\delta^n(xy)}{n!} \quad \text{(since } \delta^k = 0 \text{)}$$
$$= \exp \delta(xy).$$

The Leibniz rule $\delta^n(xy) = \sum_{i=0}^{n} \binom{n}{i} (\delta^i x)(\delta^{n-i} y)$ follows by induction on $n$, using the ordinary Leibniz rule $\delta(xy) = (\delta x)y + x(\delta y)$ for derivations.

The inverse is given by the formal series $1 - \eta + \eta^2 - \cdots \pm \eta^{k-1}$ where $\exp \delta = 1 + \eta$ and $\eta$ is nilpotent (since $\delta$ is nilpotent), so the Neumann series terminates.
