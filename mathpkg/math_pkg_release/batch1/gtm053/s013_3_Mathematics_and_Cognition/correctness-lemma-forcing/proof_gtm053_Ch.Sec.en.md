---
role: proof
locale: en
of_concept: correctness-lemma-forcing
source_book: gtm053
source_chapter: "III"
source_section: "3"
---

Part (a) follows from the definition of $\bar{h}$ and the completeness of $B$. For part (b), by definition $\|\bar{h}(\bar{x}) = 0\| = \Omega(\bar{x}) = \bigvee_{j \in \mathcal{J}} \|\bar{x} = \bar{x}_j\|$. The extensionality inequality is proved by:
$$\|\bar{x} = \bar{y}\| \wedge \bigvee_{j \in \mathcal{J}} \|\bar{x} = \bar{x}_j\| \leqslant \bigvee_{j \in \mathcal{J}} \|\bar{y} = \bar{x}_j\| = \|\bar{h}(\bar{y}) = 0\|,$$
using Boolean distributivity and $\|\bar{x} = \bar{y}\| \wedge \|\bar{x} = \bar{x}_j\| \leqslant \|\bar{y} = \bar{x}_j\|$.
