---
role: proof
locale: en
of_concept: flabby-image-sheaves
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---
**1.** We show by induction that all $\mathcal{B}_{\lambda}$ are flabby: For $\mathcal{B}_0 \simeq \mathcal{S}$ this is true by assumption; suppose we have proved that $\mathcal{B}_0, \mathcal{B}_1, \ldots, \mathcal{B}_{\ell-1}$ are flabby sheaves.

For $U \subset X$ open, the exactness of
$$0 \rightarrow \Gamma(U, \mathcal{B}_{\ell-1}) \rightarrow \Gamma(U, \mathcal{S}_{\ell-1}) \rightarrow \Gamma(U, \mathcal{B}_{\ell}) \rightarrow 0$$
follows from the exactness of
$$\mathcal{O} \rightarrow \mathcal{B}_{\ell-1} \hookrightarrow \mathcal{S}_{\ell-1} \rightarrow \mathcal{B}_{\ell} \rightarrow \mathcal{O}$$
by the surjectivity property of flabby sheaves. Let $s \in \Gamma(U, \mathcal{B}_{\ell})$. Then there is an $s' \in \Gamma(U, \mathcal{S}_{\ell-1})$ with $\varphi_{\ell} \circ s' = s$. Since $\mathcal{S}_{\ell-1}$ is flabby there is an $s^* \in \Gamma(X, \mathcal{S}_{\ell-1})$ with $s^* \mid U = s'$. But now $\varphi_{\ell} \circ s^* \in \Gamma(X, \mathcal{B}_{\ell})$ and $\varphi_{\ell} \circ s^* \mid U = s$. Therefore, $\mathcal{B}_{\ell}$ is flabby.
