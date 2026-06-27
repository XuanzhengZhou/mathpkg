---
role: proof
locale: en
of_concept: boolean-valued-universe-limit-stage
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

Let $\alpha \in K_{\Pi}$ be a limit ordinal.

($\supseteq$): For each $\xi < \alpha$, $V_{\xi}^{(B)} \subseteq V_{\alpha}^{(B)}$ by definition, since any $u \in V_{\xi}^{(B)}$ has $\mathcal{D}(u) \subseteq V_{\zeta}^{(B)}$ for some $\zeta < \xi < \alpha$. Hence $\bigcup_{\xi < \alpha} V_{\xi}^{(B)} \subseteq V_{\alpha}^{(B)}$.

($\subseteq$): Let $u \in V_{\alpha}^{(B)}$. By definition, there exists $\xi < \alpha$ such that $\mathcal{D}(u) \subseteq V_{\xi}^{(B)}$. Since $u: \mathcal{D}(u) \rightarrow B$, we have $u \in V_{\xi+1}^{(B)}$. As $\alpha$ is a limit ordinal, $\xi + 1 < \alpha$, so $u \in \bigcup_{\zeta < \alpha} V_{\zeta}^{(B)}$.

Thus $V_{\alpha}^{(B)} = \bigcup_{\xi < \alpha} V_{\xi}^{(B)}$.
