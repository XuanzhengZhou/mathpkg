---
role: proof
locale: en
of_concept: hom-direct-sum-product-natural
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

We verify commutativity of diagram (2); diagram (1) is similar. Let $\pi_\alpha: \prod_A U_\alpha \to U_\alpha$ and $q_\alpha: \prod_A Hom_R(N, U_\alpha) \to Hom_R(N, U_\alpha)$ be the canonical projections. Define $v_N(\gamma) = (\pi_\alpha \gamma)_{\alpha \in A}$ for $\gamma \in Hom_R(N, \prod_A U_\alpha)$. If $\gamma \in Hom_R(N, \prod_A U_\alpha)$, then for all $\alpha \in A$,

$$\pi'_\alpha(\prod_A Hom(f, U_\alpha)(v_N(\gamma))) = Hom(f, U_\alpha)(\pi_\alpha v_N(\gamma)) = Hom(f, U_\alpha)(Hom(N, q_\alpha)(\gamma)) = q_\alpha \gamma f$$

$$= Hom(M, q_\alpha)(Hom(f, \prod_A U_\alpha)(\gamma)) = \pi'_\alpha(v_M(Hom(f, \prod_A U_\alpha)(\gamma))).$$

Thus the diagram commutes, as desired.
