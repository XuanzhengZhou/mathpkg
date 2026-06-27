---
role: proof
locale: en
of_concept: boolean-valued-equality-axioms
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

(By induction on $\alpha$.)

1. If $\text{rank}(u) < \alpha$, $\text{rank}(u') < \alpha$, and $\text{rank}(v) \leq \alpha$, then
$$[\![u = u']\!] \cdot [\![u \in v]\!] = \sum_{y \in \mathcal{D}(v)} v(y) \cdot [\![y = u]\!] \cdot [\![u = u']\!]$$
$$\leq \sum_{y \in \mathcal{D}(v)} v(y) \cdot [\![y = u']\!] = [\![u' \in v]\!],$$
where the inequality follows from the induction hypothesis for part 3 (transitivity) applied to $y$, $u$, $u'$, which have ranks $< \alpha$.

2. For $y \in \mathcal{D}(v)$, using the definition of equality,
$$[\![u = y]\!] \cdot v(y) \cdot [\![v = v']\!] \leq [\![u = y]\!] \cdot v(y) \cdot (v(y) \Rightarrow [\![y \in v']\!]) \leq [\![u = y]\!] \cdot [\![y \in v']\!] \leq [\![u \in v']\!].$$
Summing over $y \in \mathcal{D}(v)$ yields $[\![u \in v]\!] \cdot [\![v = v']\!] \leq [\![u \in v']\!]$.

3. The transitivity of equality is established by expanding the definition of $[\![u = v]\!] \cdot [\![v = w]\!]$ and applying the induction hypothesis.
