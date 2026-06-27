---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This example applies the abstract uniqueness theorem P3 to aperiodic transient random walk in three dimensions with mean zero and finite second moments. By P26.1, the Green function satisfies $\lim_{|y| \to \infty} G(x,y)/G(0,y) = 1$, so the limit function is the constant $f(x) \equiv 1$, which is trivially $P$-regular. P3 then implies every $P$-regular function is constant. The hypotheses are far stronger than necessary -- the result holds for all transient random walk in three dimensions -- but the proof illustrates the general method: use known Green function asymptotics to identify the Martin kernel, then invoke P3.
