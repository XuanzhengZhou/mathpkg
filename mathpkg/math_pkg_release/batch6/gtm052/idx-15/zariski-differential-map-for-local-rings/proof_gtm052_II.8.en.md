---
role: proof
locale: en
of_concept: zariski-differential-map-for-local-rings
source_book: gtm052
source_chapter: "II"
source_section: "8"
---

By (8.4A), the cokernel of $\delta$ is $\Omega_{k/k} = 0$, so $\delta$ is surjective. To show injectivity, it suffices to prove that the dual map

$$\delta' : \operatorname{Hom}_k(\Omega_{B/k} \otimes k, k) \to \operatorname{Hom}_k(\mathfrak{m}/\mathfrak{m}^2, k)$$

is surjective. The domain is isomorphic to $\operatorname{Hom}_B(\Omega_{B/k}, k)$, which by the universal property of differentials is identified with $\operatorname{Der}_k(B,k)$, the set of $k$-derivations of $B$ into $k$. For any $d \in \operatorname{Der}_k(B,k)$, its restriction to $\mathfrak{m}$ vanishes on $\mathfrak{m}^2$ (by the Leibniz rule) and annihilates $k$ (since $d(1)=0$), hence factors through $\mathfrak{m}/\mathfrak{m}^2$. Thus $\delta'$ is surjective, so $\delta$ is injective.
