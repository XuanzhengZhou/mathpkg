---
role: exercise
locale: en
chapter: "8-9"
section: "Section 10_Section_10"
exercise_number: 11
---

K. Let $f$ be a monotone increasing function defined on a real interval $[a, b]$. If $g$ is a bounded, real-valued function defined on $[a, b]$ and $\mathcal{P} = \{t_i\}_{i=0}^N$ is a partition of $[a, b]$, then the upper Darboux sum (for $g$ with respect to $f$) based on $\mathcal{P}$ is the sum

$$D_{\mathcal{P}} = \sum_{i=1}^{N} M_i [f(t_i) - f(t_{i-1})],$$

where $M_i = \sup \{g(t): t_{i-1} \leq t \leq t_i\}$, $i = 1, \ldots, N$ (see Problem 1G for basic definitions). Similarly, the lower Darboux sum (for $g$ with respect to $f$) based on $\mathcal{P}$ is the sum

$$d_{\mathcal{P}} = \sum_{i=1}^{N} m_i [f(t_i) - f(t_{i-1})],$$

where $m_i = \inf \{g(t): t_{i-1} \leq t \leq t_i\}$, $i = 1, \ldots, N$. Verify that for fixed $f$ and $g$ the nets $\{D_{\mathcal{P}}\}$ and $\{d_{\mathcal{P}}\}$, indexed by the directed set of partitions of $[a, b]$, are monotone decreasing and monotone increasing, respectively. (This is a straightforward generalization of the construction introduced in Problem

where $t_{i-1} \leq \tau_i \leq t_i$, $i = 1, \ldots, N$. The number $J$ is defined to be the Riemann–Stieltjes integral of $\varphi$ over $[a, b]$ with respect to $\alpha$ if for each given positive number $\varepsilon$ there exists a positive number $\delta$ such that $|J - S| < \varepsilon$ for every Riemann–Stieltjes sum $S$ (for $\varphi$ with respect to $\alpha$) based on any partition $\mathcal{P}$ of $[a, b]$ such that the mesh of $\mathcal{P}$ is less than $\delta$. If $J$ is 
...
