---
role: proof
locale: en
of_concept: taylor-remainder-bound
source_book: gtm014
source_chapter: "III"
source_section: "2. Stability Under Deformations"
---

**Proof.** Without loss of generality, assume $p = 0$. Proceed by induction on $r$.

*Base case $r = 0$.* Write
\[
g(x) = g(0) + \sum_{i=1}^{n} x_i g_i(x),
\]
where $g_i(x) = \int_0^1 \frac{\partial g}{\partial x_i}(tx) \, dt$ (see Chapter II, Lemma 6.10). Then for any multi-index $\alpha$ with $|\alpha| \leq s - 1$,
\[
\left| \frac{\partial^{|\alpha|} g_i}{\partial x^\alpha}(x) \right|
\leq \int_0^1 \left| \frac{\partial^{|\alpha|}}{\partial x^\alpha} \frac{\partial g}{\partial x_i}(tx) \right| dt
< \varepsilon,
\]
since $|\alpha| + 1 \leq s$ and $\|g\|_s^K < \varepsilon$. The point $tx$ lies in $K$ because $K$ is convex. Hence $\|g_i\|_{s-1}^K < \varepsilon$, which establishes the case $r = 0$.

*Inductive step.* For general $r$, suppose
\[
g(x) = \sum_{0 \leq |\alpha| \leq r-1} a_\alpha x^\alpha + \sum_{|\beta| = r} h_\beta(x) x^\beta.
\]
Expanding each coefficient function $h_\beta$ as in the base case,
\[
h_\beta(x) = h_\beta(0) + \sum_{i=1}^{n} x_i h_{\beta,i}(x),
\]
and substituting back yields an expression of $g$ with remainder terms of order $r + 1$. Applying the induction hypothesis to the $h_\beta$ (which are partial derivatives of order $r$ of $g$, hence have $C^{s-r}$-norm bounded by $\varepsilon$) gives the desired bounds on the new remainder coefficients $h_{\beta,i}$, which are precisely the $g_\beta$ for $|\beta| = r + 1$. $\square$
