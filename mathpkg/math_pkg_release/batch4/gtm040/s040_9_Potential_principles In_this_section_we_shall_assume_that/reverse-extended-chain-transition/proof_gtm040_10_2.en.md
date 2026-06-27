---
role: proof
locale: en
of_concept: reverse-extended-chain-transition
source_book: gtm040
source_chapter: "10"
source_section: "2"
---

From the definition, $\hat{u}_E(\omega) = -v_E(\omega')$. Hence $\Pr'[\omega \in \text{domain } \hat{u}_E] = \Pr[\omega \in \text{domain } v_E] > 0$, giving condition (1). Since the chain watched starting in $E$ is transient, $\Pr[v_E = +\infty] = 0$, so $\Pr'[\hat{u}_E = -\infty] = 0$, giving (2).

For the transition matrix, compute the conditional probability:
$$\Pr'[x_{\hat{u}_E} = k \land x_{\hat{u}_E+1} = j \land x_{\hat{u}_E+2} = i] = \Pr[x_{v_E-2} = i \land x_{v_E-1} = j \land x_{v_E} = k] = \nu_i P_{ij} P_{jk} e_k^E$$
by Lemma 10-10. Normalizing yields $\hat{P}_{ji} = \nu_i P_{ij} / \nu_j$. The same argument as in Proposition 6-12 shows $\hat{N}_{ji} = \nu_i N_{ij} / \nu_j$, from which transience and condition (4) follow.
