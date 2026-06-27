---
role: proof
locale: en
of_concept: osofsky-lemma
source_book: gtm013
source_chapter: "7"
source_section: "24. Morita Dualities"
---

Suppose that ${}_R U_S$ defines a Morita duality and that $(M_\alpha)_{\alpha \in A}$ is an indexed set of non-zero submodules of ${}_R M$ such that $M = \bigoplus_A M_\alpha$ is $U$-reflexive. Let $(p_\alpha)_{\alpha \in A}$ be the projections for this direct sum. Since each $M_\alpha$ is $U$-torsionless, we see at once that there is an $f \in M^*$ such that $(f \mid M_\alpha) \neq 0$ for each $\alpha \in A$. Since $\bigcap_A \operatorname{Ker} p_\alpha = 0$, we have by (24.5) that

$$\sum_A r_{M^*} (\operatorname{Ker} p_\alpha) = M^*.$$

Thus

$$f = g_{\alpha_1} + \cdots + g_{\alpha_n}$$

with

$$g_{\alpha_i} \in r_{M^*} (\operatorname{Ker} p_{\alpha_i}) \quad (i = 1, \ldots, n).$$

If $\alpha \in A \setminus \{\alpha_1, \ldots, \alpha_n\}$, then $M_\alpha \subseteq \operatorname{Ker} p_{\alpha_i}$ for all $i = 1, \ldots, n$ and

$$f(M_\alpha) \subseteq g_{\alpha_1}(M_\alpha) + \cdots + g_{\alpha_n}(M_\alpha) = 0.$$

Thus we have $A = \{\alpha_1, \ldots, \alpha_n\}$, a finite set. Therefore no infinite direct sum can be $U$-reflexive.
