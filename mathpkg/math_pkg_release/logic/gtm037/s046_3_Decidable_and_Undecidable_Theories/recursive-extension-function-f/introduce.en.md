---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The recursive extension function $f$ is the core constructive mechanism in the effective Lindenbaum extension. Given a recursive enumeration $h$ of all sentences, $f$ builds a theory extension incrementally: at each step $m+1$, it adds the $m$-th sentence $h(m)$ to the range of $f$ if and only if adding that sentence does not contradict the sentences accumulated so far, relative to the original theory $\Gamma$. The resulting set $\Delta = g^{+-1}\text{Rng}\,f$ is a complete consistent extension of $\Gamma$.
