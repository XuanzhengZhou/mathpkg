---
role: proof
locale: en
of_concept: proposition-4-6
source_book: gtm055
source_chapter: "4-5"
source_section: "Section 06_Section_6"
---

Proof. Let $\varepsilon$ be a positive number. For each point $x$ of $X$ there exists a $\delta_x > 0$ such that $\rho'(f(x'), f(x)) < \varepsilon/2$ whenever $x'$ is a point of $X$ such that $\rho(x', x) < \delta_x$. The open balls $D_{\delta_x/2}(x)$ cover $X$, so there exists a finite set of points $x_1, \ldots, x_n$ in $X$ such that the balls

$$D_i = D_{\delta_x/i/2}(x_i), \quad i = 1, \ldots, n,$$

cover $X$. Let $\delta_i = \delta_x_i$, $i = 1, \ldots, n$, set $\delta = \delta_1 \wedge \cdots \wedge \delta_n$, and suppose $\rho(x', x'') < \delta/2$. Then $x'$ belongs to some $D_i$, and it follows that $x'$ and $x''$ both belong to $D_{\delta_i}(x_i)$. But then $\rho'(f(x'), f(x_i)) < \varepsilon/2$ and $\rho'(f(x''), f(x_i)) < \varepsilon/2$, so that $\rho'(f(x'), f(x'')) < \varepsilon$.

Example B. If $\varphi$ is a continuous complex-valued function on a closed interval $[a, b](a < b)$, then $\varphi$ is uniformly continuous on $[a, b]$ by the preceding proposition. It follows that for every $\varepsilon > 0$ there exists a $\delta_\varepsilon > 0$ with the property that if $\{a = t_0 < \cdots < t_N = b\}$ is any partition of $[a, b]$ having mesh less than $\delta_\varepsilon$ (Prob. 1G), and if $t', t''$ are two real numbers belonging to any one of the subintervals $[t_{i-1}, t_i]$ then $|\

of $\mathcal{Q}_0$ belong to distinct subintervals of $\mathcal{P}_n$. If mesh $\mathcal{P}_n$ is also so small that the oscillation of $\varphi$ over each of the subintervals of $\mathcal{P}_n$ does not exceed $\varepsilon/M$, then $V_n > L(b) - 3\varepsilon$.

We turn now to the topic of Baire categories in metric spaces. No prior knowledge of this topic is assumed on the part of the reader.
