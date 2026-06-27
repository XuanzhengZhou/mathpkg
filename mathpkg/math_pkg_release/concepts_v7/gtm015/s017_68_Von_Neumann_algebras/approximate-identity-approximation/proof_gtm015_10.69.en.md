---
role: proof
locale: en
of_concept: approximate-identity-approximation
source_book: gtm015
source_chapter: "10"
source_section: "69"
---

# Proof of Convolution approximation by approximate identities

Proof. Let $g \in \mathcal{F}$. It is straightforward to check that $f * g$ is everywhere defined on $G$, hence $f * g \in \mathcal{L}^1(G)$. {Also $|(f * g)(t)| \leq \|f\|_1 \|g\|_\infty$ and $|(f * g)(s) - (f * g)(t)| \leq \|f_{ts^{-1}} - f\|_1 \|g\|_\infty$ for all $s, t \in G$, thus $f * g$ is bounded and continuous.} Since $\int \tilde{g}(t) dt = \left(\int g(t) dt\right)^* = 1,$

$$(f * g)(s) - f(s) = \int f(st)g(t^{-1}) dt - f(s) \int \tilde{g}(t) dt = \int [f(st) - \Delta(t)f(s)]g(t^{-1}) dt$$

for all $s \in G$; writing $F(s, t)$ for the integrand in the last integral, elementary algebra yields

$$F(s, t) = f(st)[1 - \Delta(t)]g(t^{-1}) + [f(st) - f(s)]\tilde{g}(t).$$

It follows from (i) that, for each fixed $t \in G,$

$$\int |F(s, t)| ds \leq \|f^t\|_1 |1 - \Delta(t)| g(t^{-1}) + \|f^t - f\|_1 \tilde{g}(t).$$

Choose the neighborhood $V$ of $e$ so small that $|1 - \Delta(t)| \leq \varepsilon/(2\|f\|_1)$ and $\|f^t - f\|_1 \leq \varepsilon/2$ for all $t \in V$ (using continuity of $\Delta$ at $e$ and continuity of translations (69.9)). Then for $g \in \mathcal{F}_V$,

$$\int |F(s, t)| ds \leq \frac{\varepsilon}{2} g(t^{-1}) + \frac{\varepsilon}{2} \tilde{g}(t)$$

for all $t$. Integrating with respect to $t$ and applying the Fubini-Tonelli theorems,

$$\int \left| \int F(s, t) \, dt \right| \, ds \leq \varepsilon.$$

Since $\int F(s, t) \, dt = (f * g)(s) - f(s)$, we thus have $\| f * g - f \|_1 \leq \varepsilon$.
