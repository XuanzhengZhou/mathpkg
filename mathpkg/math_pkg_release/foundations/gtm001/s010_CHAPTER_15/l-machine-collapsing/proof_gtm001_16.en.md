---
role: proof
locale: en
of_concept: l-machine-collapsing
source_book: gtm001
source_chapter: "16"
source_section: ""
---

**Proof.** Since $\mathcal{P}_<$ has the collapsing property, $\pi: \bar{\eta} \rightarrow \eta$ is a strong $\mathcal{P}_<$-map. By induction on $\bar{\varphi}$: for sentences $\bar{\varphi} < \bar{\eta}$, $L \models \bar{\varphi}$ iff $L \models \pi(\bar{\varphi})$. For $\exists^{\bar{\alpha}} x_i \bar{\theta}(x_i)$: $L \models \bar{\varphi} \rightarrow (\exists \bar{t} \in T_{\bar{\alpha}})[L \models \bar{\theta}(\bar{t})] \rightarrow (\exists t \in T_\alpha)[L \models \theta(t)] \rightarrow L \models \varphi$, using the induction hypothesis. Conversely, if $L \models \varphi$, let $t = K(\langle \varphi \rangle) \in T_\alpha$, take $\bar{t}$ with $\pi(\bar{t}) = t$, and apply induction.
