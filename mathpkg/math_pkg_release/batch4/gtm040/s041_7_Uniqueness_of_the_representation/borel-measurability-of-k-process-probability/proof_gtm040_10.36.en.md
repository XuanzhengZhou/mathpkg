---
role: proof
locale: en
of_concept: borel-measurability-of-k-process-probability
source_book: gtm040
source_chapter: "10"
source_section: "7. Uniqueness of the representation"
---
By Definition 10-23,

$$\Pr^{K(\cdot, x)}[x_0 = i \land x_1 = j \land x_2 = k] = \pi_i P_{ij} P_{jk} K(k, x),$$

and the right side is continuous even for $x$ in $S^*$. Since any cylinder set is the countable disjoint union of basic cylinder sets, the function $\Pr^{K(\cdot, x)}[\omega \in A]$ for $A \in \mathcal{F}$ is a denumerable sum of such functions and hence is Borel measurable.

Let $\mathcal{C}$ be the class of all sets in $\Omega$ for which $\Pr^{K(\cdot, x)}[\omega \in A]$ is Borel measurable. If $\{A_n\}$ and $\{B_n\}$ are, respectively, increasing and decreasing sequences of such sets, then

$$\Pr^{K(\cdot, x)}[\bigcup A_n] = \lim_n \Pr^{K(\cdot, x)}[A_n],$$

$$\Pr^{K(\cdot, x)}[\bigcap B_n] = \lim_n \Pr^{K(\cdot, x)}[B_n],$$

and so the limits are Borel measurable. Hence $\mathcal{C}$ is a monotone class containing the field $\mathcal{F}$, so $\mathcal{C}$ contains $\mathcal{G}$ by the Monotone Class Theorem (Theorem 1-19).
