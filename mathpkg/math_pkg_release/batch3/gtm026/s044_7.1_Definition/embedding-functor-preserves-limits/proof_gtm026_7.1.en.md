---
role: proof
locale: en
of_concept: embedding-functor-preserves-limits
source_book: gtm026
source_chapter: "7"
source_section: "7.1"
---

*Proof.* Let $(\Sigma, E)$ be a diagram in $\mathcal{K}$ and let $(L, \psi)$ be a limit of $E$. Write $E$-nodes as $j$ and use superscripts for $\Sigma$-diagrams to avoid notational confusion with $\Delta$-diagrams. We must show that $(\tilde{L}, (\widetilde{\psi^j}): \tilde{L} \longrightarrow \widetilde{E^j})$ is a limit of the diagram $\tilde{E}$ in $\mathcal{K}^{\Delta}$.

Let $(D, \Gamma^j: D \longrightarrow \widetilde{E^j})$ be a lower bound of $\tilde{E}$ in $\mathcal{K}^{\Delta}$. Then for each $i \in N(\Delta)$, $(D_i, \Gamma_i)$ is a lower bound of $E$, inducing unique $\Lambda_i: D_i \longrightarrow L$ such that $\Lambda_i \psi^j = \Gamma_i^j$. To see that $\Lambda: D \longrightarrow \tilde{L}$ is a diagram morphism, consider any $\alpha: i \to i'$ in $\Delta$. Since $\Gamma^j: D \longrightarrow \widetilde{E^j}$ is a diagram morphism for all $j \in N(\Sigma)$, we have $D_{\alpha} \Gamma_{i'}^j = \Gamma_i^j$. Substituting the definition of $\Lambda$, we obtain $D_{\alpha} \Lambda_{i'} \psi^j = \Lambda_i \psi^j$. Since $(\psi^j: j \in N(\Sigma))$ is a limit, this forces $D_{\alpha} \Lambda_{i'} = \Lambda_i$, proving that $\Lambda$ is a diagram morphism. Uniqueness follows from the uniqueness of each $\Lambda_i$. $\square$
