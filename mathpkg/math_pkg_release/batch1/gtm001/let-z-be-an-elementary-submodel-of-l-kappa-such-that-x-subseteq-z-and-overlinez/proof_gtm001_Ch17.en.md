---
role: proof
locale: en
of_concept: let-z-be-an-elementary-submodel-of-l-kappa-such-that-x-subseteq-z-and-overlinez
source_book: gtm001
source_chapter: "17"
source_section: ""
---

Let $h: L_{\overline{\kappa}} \rightarrow L_{\overline{\kappa}}$ be an elementary embedding such that $\mathcal{W}(h) = Z$. For any

Let $\Pi = \langle \langle \delta_i, \alpha_i, P_i \rangle, \pi_{ij} \rangle_{i,j \in I} \subseteq Z$ be a $\kappa$-direct limit system which is not well founded. Then there exist sequences $\langle i_n: n \in \omega \rangle$ and $\langle \sigma_n: n \in \omega \rangle$ such that $(\forall n \in \omega) [i_n \in I \land \sigma_n < \delta_{i_n}]$ and

$$(\forall n \in \omega)[i_n \leq i_{n+1} \land \pi_{i_n i_{n+1}}(\sigma_n) > \sigma_{n+1}].$$

Claim: There exists a sequence $\langle j_n: n \in \omega \rangle$ such that

(i) $(\forall n \in \omega)[j_n \in I \land i_n \leq j_n \leq j_{n+1}]$;

(ii) $\lambda \triangleq \sup_{n < \omega} \delta_{j_n} \in S$;

(iii) $\Pi' = \Pi \upharpoonright \{j_n: n \in \omega\}$ is a countable $\lambda$-direct limit system.

We let $\sigma'_n = \pi_{i_n j_n}(\sigma_n)$. Then

$$\pi_{j_n j_{n+1}}(\sigma'_n) = \pi_{j_n j_{n+1}}(\pi_{i_n j_n}(\sigma_n))$$

$$= \pi_{i_n j_{n+1}}(\sigma_n)$$

$$= \pi_{i_{n+1} j_{n+1}}(\pi_{i_n i_{n+1}}(\sigma_n))$$

$$> \pi_{i_{n+1} j_{n+1}}(\sigma_{n+1}) = \sigma'_{n+1}.$$

Hence $\Pi'$ is not well founded, and hence not $Z$-well-founded. Thus $\Pi$ is not $Z$-well-founded.

We shall now prove the claim. By recursion on $n$, we define $\gamma_n \in
