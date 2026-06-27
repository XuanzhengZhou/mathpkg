---
role: proof
locale: en
of_concept: diagram-lemmas-in-abelian-categories
source_book: gtm005
source_chapter: "VIII"
source_section: "2"
---

The classical diagram lemmas (Five Lemma, Snake Lemma, $3 \times 3$ Lemma) hold in any abelian category. Two approaches:

**Freyd-Mitchell embedding**: Every small abelian category admits an exact, fully faithful embedding into $R\text{-}\mathbf{Mod}$ for some ring $R$. Since the diagram lemmas involve only finite limits and colimits and exactness properties, and the embedding preserves and reflects these, the truth in module categories implies truth in all abelian categories.

**Calculus of members**: Mac Lane introduces "members" in an abelian category as equivalence classes of morphisms with codomain the given object. A member $x \in_m A$ is represented by a morphism $f: X \to A$. Using this calculus, one can reason "element-wise" in any abelian category:
- $f$ is monic iff $f(x) \equiv 0 \Rightarrow x \equiv 0$.
- $f$ is epi iff every member of the codomain comes from a member of the domain.
- Kernels, cokernels, and exactness have characterizations via members, reducing diagram lemmas to element-wise arguments.
