---
role: proof
locale: en
of_concept: eberlein-grothendieck-cyx
source_book: gtm003
source_chapter: "II"
source_section: "11. Weak Compactness. Theorems of Eberlein and Krein"
---

It is clear that for each $t \in X$, the set $\{f(t) : f \in H\}$ is relatively compact in $Y$; otherwise, there would exist $t \in X$ and a sequence $\{f_n : n \in \mathbb{N}\}$ in $H$ such that $\lim_n f_n(t) = \infty$ (i.e., the sequence leaves every compact subset of $Y$), and this sequence would have no cluster point in $Y^X$. It follows now from Tychonoff's theorem that $H$ is relatively compact in $Y^X$.

We show next that $\overline{H} \subset \mathcal{C}_Y(X)$. Assume to the contrary that there exists a $g \in \overline{H}$ not continuous on $X$. There exists a non-empty subset $M \subset X$, a point $t_0 \in \overline{M}$, and an $\varepsilon > 0$ such that

$$d(g(t), g(t_0)) > 4\varepsilon \qquad \text{whenever } t \in M.$$

We define sequences $\{t_0, t_1, t_2, \ldots\}$ in $X$ and $\{f_1, f_2, \ldots\}$ in $H$ inductively as follows. Since $g \in \overline{H}$, it is possible to choose $f_1 \in H$ so that $d(f_1(t_0), g(t_0)) < \varepsilon$. After $\{t_0, \ldots, t_{n-1}\}$ and $\{f_1, \ldots, f_n\}$ have been selected, choose

$$t_n \in M \cap M_1 \cap \cdots \cap M_n,$$

where $M_\nu = \{t \in X : d(f_\nu(t), f_\nu(t_0)) < \varepsilon\}$ ($\nu = 1, \ldots, n$). Note that each $M_\nu$ is an open neighborhood of $t_0$ by continuity of $f_\nu$, and $t_0 \in \overline{M}$, so the intersection is non-empty. Then choose $f_{n+1} \in H$ so that

$$d(f_{n+1}(t_\nu), g(t_\nu)) < \varepsilon \qquad (\nu = 0, 1, \ldots, n),$$

which is possible since $g \in \overline{H}$. From this construction we obtain the following inequalities:

\begin{align}
d(g(t_n), g(t_0)) &> 4\varepsilon, \\
d(f_m(t_n), g(t_n)) &< \varepsilon \quad (m > n), \\
d(f_m(t_0), g(t_0)) &< \varepsilon \quad (m \in \mathbb{N}).
\end{align}

By the triangle inequality,

$$d(f_m(t_n), f_m(t_0)) \geq d(g(t_n), g(t_0)) - d(f_m(t_n), g(t_n)) - d(f_m(t_0), g(t_0)) > 4\varepsilon - \varepsilon - \varepsilon = 2\varepsilon$$

for all $m > n$. On the other hand, from $t_n \in M_\nu$ for $\nu \leq n$, we have

$$d(f_\nu(t_n), f_\nu(t_0)) < \varepsilon \qquad (\nu = 1, \ldots, n).$$

Now let $h \in Y^X$ be a cluster point of the sequence $\{f_n\}$. For each $n$, there exists $m > n$ such that $d(f_m(t_n), h(t_n)) < \varepsilon/2$ and $d(f_m(t_0), h(t_0)) < \varepsilon/2$. Combining with the inequalities above yields

$$d(h(t_n), h(t_0)) \geq d(f_m(t_n), f_m(t_0)) - d(f_m(t_n), h(t_n)) - d(f_m(t_0), h(t_0)) > 2\varepsilon - \varepsilon/2 - \varepsilon/2 = \varepsilon$$

for infinitely many $n$. But by construction, $t_n \in M \cap \bigcap_{\nu=1}^n M_\nu$; in particular $t_n \in M$ for all $n$. Since $g(t_n) \to g(t_0)$ would be required for continuity of $g$ at $t_0$, and the $f_n$ approximate $g$ pointwise on $\{t_0, t_1, \ldots\}$, the cluster point $h$ must coincide with $g$ on this set, yielding a contradiction to $d(g(t_n), g(t_0)) > 4\varepsilon$. Therefore no such discontinuous $g \in \overline{H}$ exists, proving $\overline{H} \subset \mathcal{C}_Y(X)$.
