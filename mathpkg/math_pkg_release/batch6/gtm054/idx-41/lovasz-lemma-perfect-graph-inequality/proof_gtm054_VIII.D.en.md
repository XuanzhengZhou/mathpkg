---
role: proof
locale: en
of_concept: lovasz-lemma-perfect-graph-inequality
source_book: gtm054
source_chapter: "VIII"
source_section: "D"
---

**Proof.** Let $\Lambda$ be determined by $(\Gamma, W, g)$. We proceed by induction on $|W|$. When $|W| = 1$, the desired inequality reads $1 \leq 1$. Assume as induction hypothesis that $\nu_0(\Lambda_T) \leq \alpha_0(\Lambda_T)\omega(\Lambda_T)$ whenever $T \subset W$.

If $g$ is not surjective, then by an earlier reduction (Lemma D8) the conclusion follows. Otherwise, suppose for contradiction that

$$\nu_0(\Lambda) = \alpha_0(\Lambda)\omega(\Lambda) + 1. \tag{D14}$$

Since $\Lambda_{(C)}$ is the Lovász graph determined by $(\Gamma_{(x)}, W + C, g_{|W+C})$ and since $\Gamma_{(x)}$ is perfect, Lemma D8 yields that $\Lambda_{(C)}$ is color-perfect. Since $\chi_0(\Lambda_{(C)}) = \omega(\Lambda_{(C)}) \leq \omega(\Lambda)$, there exists a vertex coloring $h: W + C \rightarrow \{1, \ldots, \omega(\Lambda)\}$ of $\Lambda_{(C)}$. By D14,

$$\alpha_0(\Lambda)\omega(\Lambda) = \nu_0(\Lambda_{(C)}) + |C| - 1 = \sum_{i=1}^{\omega(\Lambda)} |h^{-1}[i]| + |C| - 1.$$

Since no color class $h^{-1}[i]$ contains more than $\alpha_0(\Lambda)$ vertices, at most $|C| - 1$ color classes fail to be scatterings. Let $T$ denote the union of exactly $\omega(\Lambda) - |C| + 1$ color classes in $W + C$ with respect to $h$ which are scatterings. Thus

$$|T + \{u\}| = \alpha_0(\Lambda)(\omega(\Lambda) - |C| + 1) + 1.$$

But by the induction hypothesis, $\nu_0(\Lambda_{T+\{u\}}) \leq \alpha_0(\Lambda_{T+\{u\}})\omega(\Lambda_{T+\{u\}}) \leq \alpha_0(\Lambda)\omega(\Lambda_{T+\{u\}})$, whence

$$\omega(\Lambda) - |C| + 1 < \omega(\Lambda_{T+\{u\}}). \tag{D15}$$

Recall that by the definition of $T$, $\omega(\Lambda_T) \leq \omega(\Lambda) - |C| + 1$. Combining this with D15 yields $\omega(\Lambda_{T+\{u\}}) > \omega(\Lambda_T)$. Therefore $u \in C'$ for some clique $C'$, which leads to a contradiction with the definition of $C$ as a maximum clique. $\square$
