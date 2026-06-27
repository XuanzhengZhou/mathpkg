---
role: proof
locale: en
of_concept: metric-spaces-no-left-adjoint
source_book: gtm026
source_chapter: "2"
source_section: "2.27"
---

An easy way to see this is to know that it is rare for an uncountable product of metrizable topological spaces to be metrizable. For a specific example, we may cite [Hewitt and Ross '62, Theorem 8.11] which asserts that if $I$ is an uncountable set and if $K$ is a denumerably infinite discrete space, then $K^I$ is not normal (and hence, not metrizable). But $K$ is metrizable by the discrete metric $d$ which keeps all distinct pairs of points exactly one unit apart. The product $(K, d)^I$ exists in $\mathcal{A}$ (the category of metric spaces and distance-decreasing maps) but is not preserved by $U$, so we invoke Theorem 2.22 (which states that a left adjoint must preserve all limits that exist in the domain). Since $U$ fails to preserve this product, $U$ cannot have a left adjoint.
