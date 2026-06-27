---
role: proof
locale: en
of_concept: nullstellensatz-for-analytic-ideal-sheaves
source_book: gtm038
source_chapter: "IV"
source_section: "4. Coherent Sheaves"
---

For $\mathfrak{z}_0 \in B \setminus A$, we have $\mathcal{I}(A)_{\mathfrak{z}_0} = \mathcal{O}_{\mathfrak{z}_0}$, so $(\mathcal{O}/\mathcal{I}(A))_{\mathfrak{z}_0} = \mathbf{O}_{\mathfrak{z}_0}$.

For $\mathfrak{z}_0 \in A$, suppose $\mathcal{I}(A)_{\mathfrak{z}_0} = \mathcal{O}_{\mathfrak{z}_0}$. Then $1_{\mathfrak{z}_0} \in \mathcal{I}(A)_{\mathfrak{z}_0}$, meaning there exists a holomorphic function $f$ on a neighborhood $U(\mathfrak{z}_0)$ with $f|U \cap A = 0$ and $r_f(\mathfrak{z}_0) = 1_{\mathfrak{z}_0} = r_1(\mathfrak{z}_0)$. By the identity theorem, $r_f$ and $r_1$ agree on a neighborhood $V(\mathfrak{z}_0) \subset U$. Since the restriction map $r$ is bijective on $V$, it follows that $f|V = 1|V$, contradicting $f(\mathfrak{z}_0) = 0$ (since $\mathfrak{z}_0 \in A$ and $f$ vanishes on $A$). Hence $\mathcal{I}(A)_{\mathfrak{z}_0} \neq \mathcal{O}_{\mathfrak{z}_0}$, so $(\mathcal{O}/\mathcal{I}(A))_{\mathfrak{z}_0} \neq \mathbf{O}_{\mathfrak{z}_0}$.

Thus $\operatorname{Supp}(\mathcal{O}/\mathcal{I}(A)) = A$, and by definition $N(\mathcal{I}(A)) = A$.

For the second statement: there exist non-reduced ideal sheaves $\mathcal{J}$ (e.g., $\mathcal{J} = \mathcal{I}(A)^2$) where $N(\mathcal{J}) = A$ but $\mathcal{J} \subsetneq \mathcal{I}(A) = \mathcal{I}(N(\mathcal{J}))$.
