---
role: proof
locale: en
of_concept: r-e-and-effectively-inseparable-implies-creative
source_book: gtm037
source_chapter: "6"
source_section: "Recursive Function Theory"
---

By symmetry it suffices to show that $A$ is creative, i.e. that $\omega \sim A$ is productive. Let $f$ be as in Definition 6.21(iii). Say $A = \mathrm{Dmn}\,arphi_u^1$ and $B = \mathrm{Dmn}\,arphi_s^1$. For any $e, x \in \omega$ let

$$g(x, e) \simeq \mu y\,((e, x, y) \in T_1 	ext{ or } (u, f(e, u), y) \in T_1).$$

Thus $g$ is partial recursive; say $g = arphi_v^2$. Then by the $s$-$m$-$n$ theorem, for any $e \in \omega$ there exists $h(e)$ such that $arphi_{h(e)}^1(x) \simeq g(x, e)$. Now we show that $h$ is a productive function for $\omega \sim A$. 

Suppose $\mathrm{Dmn}\,arphi_e^1 \subseteq \omega \sim A$. Consider $f(e, s)$. If $f(e, s) \in A$, then $f(e, s) \in \mathrm{Dmn}\,arphi_u^1$, so for some $y$, $(u, f(e, s), y) \in T_1$, which would imply $f(e, s) \in \mathrm{Dmn}\,arphi_{h(e)}^1$. But by the definition of $g$ and the effective inseparability condition, this leads to a contradiction. Therefore $f(e, s) 
otin A$, and moreover $f(e, s) 
otin \mathrm{Dmn}\,arphi_e^1$ by the effective inseparability property. Hence $f(e, s) \in (\omega \sim A) \sim \mathrm{Dmn}\,arphi_e^1$, establishing that $\omega \sim A$ is productive.
