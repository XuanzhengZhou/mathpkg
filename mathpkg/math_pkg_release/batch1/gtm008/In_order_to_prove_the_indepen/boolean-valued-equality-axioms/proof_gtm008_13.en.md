---
role: proof
locale: en
of_concept: boolean-valued-equality-axioms
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The proof proceeds by induction on $\alpha$ simultaneously for all three parts.

**Part 1.** Assume $\operatorname{rank}(u) < \alpha$, $\operatorname{rank}(u') < \alpha$, and $\operatorname{rank}(v) \leq \alpha$. Then:
$$[\![u = u']\!] \cdot [\![u \in v]\!] = [\![u = u']\!] \cdot \sum_{y \in \mathcal{D}(v)} v(y) \cdot [\![y = u]\!]$$
$$= \sum_{y \in \mathcal{D}(v)} v(y) \cdot [\![y = u]\!] \cdot [\![u = u']\!]$$
$$\leq \sum_{y \in \mathcal{D}(v)} v(y) \cdot [\![y = u']\!]$$
by the induction hypothesis for part 3 applied to $y, u, u'$
$$= [\![u' \in v]\!].$$

**Part 2.** Assume $\operatorname{rank}(u) < \alpha$, $\operatorname{rank}(v) \leq \alpha$, $\operatorname{rank}(v') \leq \alpha$. For $y \in \mathcal{D}(v)$:
$$[\![u = y]\!] \cdot v(y) \cdot [\![v = v']\!] \leq [\![u = y]\!] \cdot v(y) \cdot (v(y) \Rightarrow [\![y \in v']\!])$$
$$\leq [\![u = y]\!] \cdot [\![y \in v']\!]$$
$$= [\![u = y]\!] \cdot \sum_{z \in \mathcal{D}(v')} v'(z) \cdot [\![y = z]\!]$$
$$= \sum_{z \in \mathcal{D}(v')} v'(z) \cdot [\![u = y]\!] \cdot [\![y = z]\!]$$
$$\leq \sum_{z \in \mathcal{D}(v')} v'(z) \cdot [\![u = z]\!] = [\![u \in v']\!]$$
by the induction hypothesis for part 3. Summing over $y \in \mathcal{D}(v)$ yields the result.

**Part 3.** Assume $\operatorname{rank}(u), \operatorname{rank}(v), \operatorname{rank}(w) \leq \alpha$. Using the definition of equality:
$$[\![u = v]\!] \cdot [\![v = w]\!] = \prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow [\![x \in v]\!]) \cdot \prod_{y \in \mathcal{D}(v)} (v(y) \Rightarrow [\![y \in u]\!])$$
$$\quad \cdot \prod_{y' \in \mathcal{D}(v)} (v(y') \Rightarrow [\![y' \in w]\!]) \cdot \prod_{z \in \mathcal{D}(w)} (w(z) \Rightarrow [\![z \in v]\!]).$$
For each $x \in \mathcal{D}(u)$, we have $u(x) \Rightarrow [\![x \in v]\!]$ and $v(x) \Rightarrow [\![x \in w]\!]$ (if $x \in \mathcal{D}(v)$). By Boolean algebra properties and the induction hypothesis, $u(x) \Rightarrow [\![x \in w]\!]$. A symmetric argument for $\mathcal{D}(w)$ yields $w(z) \Rightarrow [\![z \in u]\!]$. Therefore:
$$[\![u = v]\!] \cdot [\![v = w]\!] \leq \prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow [\![x \in w]\!]) \cdot \prod_{z \in \mathcal{D}(w)} (w(z) \Rightarrow [\![z \in u]\!]) = [\![u = w]\!].$$
