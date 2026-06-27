---
role: proof
locale: en
of_concept: deduction-theorem-generalized
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

$(i) \Rightarrow (ii)$. We proceed by induction on $m$, the case $m = 0$ being trivial (condition $(ii)$ is then to be interpreted as $\Gamma \vdash \psi$, just like $(i)$). Assume that the implication holds for $m$, and suppose that $\Gamma \cup \{\varphi_0, \ldots, \varphi_m\} \vdash \psi$. Then by 10.86, $\Gamma \cup \{\varphi_0, \ldots, \varphi_{m-1}\} \vdash \varphi_m \rightarrow \psi$, so by the induction assumption,

$$\Gamma \vdash \varphi_0 \wedge \cdots \wedge \varphi_{m-1} \rightarrow (\varphi_m \rightarrow \psi).$$

A suitable tautology then gives $\Gamma \vdash \varphi_0 \wedge \cdots \wedge \varphi_m \rightarrow \psi$, as desired.

The implication $(ii) \Rightarrow (i)$ is trivial. $\square$
