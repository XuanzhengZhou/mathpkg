---
role: exercise
locale: en
chapter: "16"
section: "Problems"
exercise_number: "A"
---

If $\{s_n\}_{n=1}^{\infty}$ is an arbitrary sequence of positive real numbers, then $\|s_n e_n\|_p = s_n$ in $(\ell_p)$ for every value of $p$, $1 \leq p < +\infty$. Hence if $\lim_n s_n = +\infty$, then no subsequence of the sequence $\{s_n e_n\}$ can be weakly convergent in $(\ell_p)$ for any value of $p$. Nevertheless, the countable set $S = \{s_n e_n : n \in \mathbb{N}\}$ may have weak accumulation points. Show, for example, that $0$ belongs to the weak closure of $S$ in $(\ell_p)$ if we set $s_n = n^{1/q}$, $n \in \mathbb{N}$, where $p > 1$ and $q$ denotes the H\"older conjugate of $p$.

\textit{Hint:} Show first that for each weak neighborhood $V$ of $0$ in $(\ell_p)$ there exists a single vector $a = \{\alpha_n\}_{n=0}^{\infty}$ in $(\ell_q)$ and a positive number $\varepsilon$ such that $V$ contains the set
$$\left\{x = \{\xi_n\} \in (\ell_p) : \left| \sum_{n=0}^{\infty} \alpha_n \xi_n \right| < \varepsilon \right\}.$$
If $V$ contained no point of $S$ it would follow that $|\alpha_n| s_n \geq \varepsilon > 0$, and hence that $|\alpha_n| \geq \varepsilon/n^{1/q}$ for every $n$ in $\mathbb{N}_0$.
