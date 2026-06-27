---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Example 2.27 demonstrates a negative case: the forgetful functor from metric spaces (with distance-decreasing maps) to topological spaces does **not** have a left adjoint. The obstruction arises because uncountable products of metrizable spaces need not be metrizable, so the forgetful functor fails to preserve small products — violating condition (1) of the General Adjoint Functor Theorem. A specific instance uses [Hewitt and Ross '62, Theorem 8.11]: if $I$ is uncountable and $K$ is a countably infinite discrete space, then $K^I$ is not normal (hence not metrizable), though $(K, d)^I$ exists in the metric space category with the discrete metric.
