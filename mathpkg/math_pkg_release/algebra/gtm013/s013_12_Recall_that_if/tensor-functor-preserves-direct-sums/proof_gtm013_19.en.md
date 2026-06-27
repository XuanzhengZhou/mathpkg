---
role: proof
locale: en
of_concept: tensor-functor-preserves-direct-sums
source_book: gtm013
source_chapter: "5"
source_section: "19"
---

For the functor $({}_S U \otimes_R -)$: given a direct sum $(M, (i_\alpha), (p_\alpha))$ in ${}_R\mathbf{M}$, apply Lemma 19.9 with the bimodule ${}_S U_R$ (viewed as $U_R$) and the one-term direct sum with $N = R$. More directly, let $f: M \to M''$ be an $R$-homomorphism. Define $U \otimes_R f$ by $(U \otimes_R f)(u \otimes m) = u \otimes f(m)$. This is well-defined because $(u, m) \mapsto u \otimes f(m)$ is $R$-balanced.

For any $s \in S$, $(U \otimes_R f)(su \otimes m) = su \otimes f(m) = s(u \otimes f(m)) = s((U \otimes_R f)(u \otimes m))$, so $U \otimes_R f$ is an $S$-homomorphism. Composition is preserved: $(U \otimes_R g)(U \otimes_R f) = U \otimes_R (g f)$, showing this is an additive covariant functor.

Preservation of direct sums follows from Lemma 19.9: for fixed $U$, the functor sends a direct sum $\bigoplus_\alpha M_\alpha$ with injections $i_\alpha$ to $U \otimes_R \bigoplus_\alpha M_\alpha$ with maps $1_U \otimes i_\alpha$, which by (19.9) forms a direct sum decomposition $U \otimes_R (\bigoplus_\alpha M_\alpha) \cong \bigoplus_\alpha (U \otimes_R M_\alpha)$. The symmetric argument works for $(- \otimes_S U_R)$.
