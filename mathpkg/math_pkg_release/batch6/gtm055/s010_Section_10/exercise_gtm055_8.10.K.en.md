---
role: exercise
locale: en
chapter: "8"
section: "10"
exercise_number: "K"
---

Let $f$ be a monotone increasing function defined on a real interval $[a, b]$. If $g$ is a bounded, real-valued function defined on $[a, b]$ and $\mathcal{P} = \{t_i\}_{i=0}^N$ is a partition of $[a, b]$, then the upper Darboux sum (for $g$ with respect to $f$) based on $\mathcal{P}$ is the sum

$$D_{\mathcal{P}} = \sum_{i=1}^{N} M_i [f(t_i) - f(t_{i-1})],$$

where $M_i = \sup \{g(t): t_{i-1} \leq t \leq t_i\}$, $i = 1, \ldots, N$. Similarly, the lower Darboux sum (for $g$ with respect to $f$) based on $\mathcal{P}$ is the sum

$$d_{\mathcal{P}} = \sum_{i=1}^{N} m_i [f(t_i) - f(t_{i-1})],$$

where $m_i = \inf \{g(t): t_{i-1} \leq t \leq t_i\}$, $i = 1, \ldots, N$. Verify that for fixed $f$ and $g$ the nets $\{D_{\mathcal{P}}\}$ and $\{d_{\mathcal{P}}\}$, indexed by the directed set of partitions of $[a, b]$, are monotone decreasing and monotone increasing, respectively.
