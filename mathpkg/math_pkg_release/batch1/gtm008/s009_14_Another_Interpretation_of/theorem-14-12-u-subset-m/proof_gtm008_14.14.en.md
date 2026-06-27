---
role: proof
locale: en
of_concept: theorem-14-12-u-subset-m
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

We compute:

$$[u \subseteq M] \leq \prod_{x \in \mathcal{D}(u)} \left(u(x) \Rightarrow [M(x)]\right)$$

$$\leq \prod_{x \in \mathcal{D}(u)} \left(u(x) \Rightarrow \sum_{y \in V^{(B)}} [u \subseteq \check{y}] \cdot [M(\check{y})]\right)$$

$$\leq \sum_{y \in V^{(B)}} [u \subseteq \check{y}] \cdot [M(\check{y})]$$

$$\leq \sum_{y \in V^{(B)}} [M(y)] \cdot [u \subseteq y]$$

$$= [[(\exists y \in M) \; [u \subseteq y]]].$$

The critical steps use Theorem 14.11 to bound $[M(x)]$ by elements of $\check{y}$ and the definition of the Boolean existential quantifier.
