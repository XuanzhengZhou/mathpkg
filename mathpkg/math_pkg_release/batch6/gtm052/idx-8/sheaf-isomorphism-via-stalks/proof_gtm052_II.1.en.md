---
role: proof
locale: en
of_concept: sheaf-isomorphism-via-stalks
source_book: gtm052
source_chapter: "II"
source_section: "1"
---

If $\varphi$ is an isomorphism it is clear that each $\varphi_P$ is an isomorphism. Conversely, assume $\varphi_P$ is an isomorphism for all $P \in X$. To show that $\varphi$ is an isomorphism, it suffices to show that $\varphi(U): \mathcal{F}(U) \rightarrow \mathcal{G}(U)$ is an isomorphism for all $U$, because then we can define an inverse morphism $\psi$ by $\psi(U) = \varphi(U)^{-1}$ for each $U$.

First we show $\varphi(U)$ is injective. Let $s \in \mathcal{F}(U)$ and suppose $\varphi(s) \in \mathcal{G}(U)$ is $0$. Then for every point $P \in U$, the image $\varphi(s)_P$ of $\varphi(s)$ in the stalk $\mathcal{G}_P$ is $0$. Since $\varphi_P$ is injective for each $P$, we deduce that $s_P = 0$ in $\mathcal{F}_P$ for each $P \in U$. This means that for each $P \in U$, there exists an open neighborhood $V_P$ of $P$ contained in $U$ such that $s|_{V_P} = 0$. The collection $\{V_P\}_{P \in U}$ forms an open cover of $U$, and by the identity axiom (3) for the sheaf $\mathcal{F}$, we conclude $s = 0$ in $\mathcal{F}(U)$. Hence $\varphi(U)$ is injective.

Next we show $\varphi(U)$ is surjective. Let $t \in \mathcal{G}(U)$. For each $P \in U$, since $\varphi_P$ is surjective, there exists a germ $s_P \in \mathcal{F}_P$ such that $\varphi_P(s_P) = t_P$. This means there exists an open neighborhood $V_P$ of $P$ contained in $U$ and a section $s^{(P)} \in \mathcal{F}(V_P)$ such that $s^{(P)}_P = s_P$ and $\varphi(s^{(P)})$ agrees with $t|_{V_P}$ in a neighborhood of $P$. Shrinking $V_P$ if necessary, we may assume $\varphi(s^{(P)}) = t|_{V_P}$ on $V_P$. Now on $V_P \cap V_Q$, we have $\varphi(s^{(P)}|_{V_P \cap V_Q} - s^{(Q)}|_{V_P \cap V_Q}) = t|_{V_P \cap V_Q} - t|_{V_P \cap V_Q} = 0$. By the injectivity already proved on $V_P \cap V_Q$, we have $s^{(P)}|_{V_P \cap V_Q} = s^{(Q)}|_{V_P \cap V_Q}$. By the gluing axiom (4) for $\mathcal{F}$, there exists $s \in \mathcal{F}(U)$ such that $s|_{V_P} = s^{(P)}$ for all $P$. Then $\varphi(s)|_{V_P} = \varphi(s^{(P)}) = t|_{V_P}$, so applying the identity axiom for $\mathcal{G}$, we get $\varphi(s) = t$. Hence $\varphi(U)$ is surjective.

Thus $\varphi(U)$ is an isomorphism for every open $U$, and $\varphi$ is an isomorphism of sheaves.
