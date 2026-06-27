---
role: proof
locale: en
of_concept: continuous-image-of-compact-space
source_book: gtm055
source_chapter: "3"
source_section: "General topology"
---

For the first statement: Let $\{V_\alpha\}$ be an open cover of $Y$. Then $\{f^{-1}(V_\alpha)\}$ is an open cover of $X$. If $X$ is compact, a finite subcover $f^{-1}(V_{\alpha_1}), \ldots, f^{-1}(V_{\alpha_n})$ exists. Then $V_{\alpha_1}, \ldots, V_{\alpha_n}$ cover $Y$, so $Y$ is compact. The countably compact case follows by the same argument restricted to countable covers.

For the second statement: To show $f^{-1}$ is continuous, let $F \subset X$ be closed. Since $X$ is compact and $F$ is closed, $F$ is compact. By the first statement, $f(F)$ is compact in the Hausdorff space $Y$, hence $f(F)$ is closed in $Y$. But $f(F) = (f^{-1})^{-1}(F)$, so $f^{-1}$ pulls back closed sets to closed sets, hence is continuous.
