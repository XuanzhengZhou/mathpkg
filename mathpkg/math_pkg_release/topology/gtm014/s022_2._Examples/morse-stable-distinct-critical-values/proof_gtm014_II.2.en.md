---
role: proof
locale: en
of_concept: morse-stable-distinct-critical-values
source_book: gtm014
source_chapter: "II"
source_section: "2. Examples"
---

**($\Rightarrow$) Stable implies Morse with distinct critical values.** Let $f$ be stable. Then there is a neighborhood $W_f$ of $f$ in $C^\infty(X, \mathbb{R})$ in which each function is equivalent to $f$. By II, Proposition 6.13, Morse functions $g$ whose critical values are distinct form a dense subset of $C^\infty(X, \mathbb{R})$, so $W_f$ must contain such a function $g$. Hence $f$ is equivalent to $g$. Any function equivalent to a Morse function with distinct critical values is itself a Morse function with distinct critical values.

**($\Leftarrow$) Morse with distinct critical values implies stable.** Suppose $f$ is a Morse function all of whose critical values are distinct. Around each point $p$ in $X$, choose an open neighborhood $U_p$ as follows:

(a) If $p$ is a regular point, choose $U_p$ so small that $(df)_q \neq 0$ for every $q$ in $U_p$. Choose a vector field $s^p$ on $U_p$ such that $(df)(s^p) \neq 0$ on $U_p$.

(b) If $p$ is a critical point, then choose $U_p$ to be a coordinate neighborhood with coordinates $x_1, \ldots, x_n$ so that $f|_{U_p}$ is given by $c + \varepsilon_1 x_1^2 + \cdots + \varepsilon_n x_n^2$ where $\varepsilon_i = \pm 1$ for $i = 1, \ldots, n$. (See II, Theorem 6.9.)

The collection $\{U_p\}_{p \in X}$ forms an open covering of $X$. Since $X$ is compact, there exists a finite subcovering $U_1, \ldots, U_m$ corresponding to $p_1, \ldots, p_m$. Let $\rho_1, \ldots, \rho_m$ be a partition of unity subordinate to this covering. Choose vector fields $s_i$ on $X$ ($1 \leq i \leq m$) as follows:

(a) If $p_i$ is a regular point, then let
$$s_i(x) = \begin{cases} \frac{w(x)\rho_i(x) s^p_i(x)}{s^p_i[f](x)} & \text{on } U_{p_i} \\ 0 & \text{off } U_{p_i} \end{cases}$$

(b) If $p_i$ is a critical point, then $w(p_i) = 0$ and $\rho_i w = \sum_{j=1}^{n} h_j x_j$ for suitably chosen smooth functions $h_j$ in the coordinates on $U_i$ given above. (See II, Lemma 6.10.) Moreover, the $h_j$ are compactly supported functions in $U_i$ since $\rho_i w$ is.

Let $s_i = \sum_{j=1}^{n} h_j \frac{\partial}{\partial x_j}$ on $U_i$ (and extended by zero off $U_i$). Then one verifies that $\sum_i (df)(s_i) = w$, establishing infinitesimal stability.
