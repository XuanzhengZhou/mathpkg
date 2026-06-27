---
role: proof
locale: en
of_concept: limit-ordinal-multiplication-with-natural
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By induction on $\gamma + n$). If $\gamma + n = \omega$, then $m \cdot \omega = \bigcup_{k < \omega} m \cdot k$. Since $m \cdot k < \omega$ for each $k \in \omega$, we have $\bigcup_{k < \omega} m \cdot k \le \omega$. Furthermore, for any $p < \omega$, by Proposition 8.27 there exist $q, r$ such that $p = m \cdot q + r$ with $r < m$. Then $p = m \cdot q + r \le m \cdot q + m = m \cdot (q + 1)$, so $p \in \bigcup_{k < \omega} m \cdot k$. Hence $\bigcup_{k < \omega} m \cdot k = \omega$. This proves the base case.

If $m \cdot (\gamma + n) = \gamma + m \cdot n$, then

$$m \cdot (\gamma + n + 1) = m \cdot (\gamma + n) + m = (\gamma + m \cdot n) + m = \gamma + (m \cdot n + m) = \gamma + m \cdot (n + 1).$$

If $\gamma + n \in K_{\mathrm{II}}$, then $n = 0$ and $\gamma \in K_{\mathrm{II}}$. Then $m \cdot \gamma = \bigcup_{\delta < \gamma} m \cdot \delta$. If $\delta < \gamma$, then either $\delta < \omega$ or $\omega \le \delta$. If $\delta < \omega$, then $m \cdot \delta < \omega < \gamma$. If $\omega \le \delta$, then $\delta = \beta + k$ for some $\beta \in K_{\mathrm{II}}$ and $k \in \omega$, and by the induction hypothesis $m \cdot \delta = \beta + m \cdot k$. In both cases, $m \cdot \delta$ is bounded by elements approaching $\gamma$, so the supremum is $\gamma$.
