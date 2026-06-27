---
role: proof
locale: en
of_concept: keisler-shelah-isomorphism-theorem
source_book: gtm037
source_chapter: "26"
source_section: "Elementary Classes and Elementary Equivalence"
---

Obviously $(ii) \Rightarrow (i)$ (elementary equivalence is preserved under ultrapowers and isomorphisms). For the hard direction $(i) \Rightarrow (ii)$, assume $\mathfrak{A} \equiv_{\text{ee}} \mathfrak{B}$. Let

$$n = 2^{|A| + |B| + |\text{Fmla}_\mathcal{L}|}.$$

The index set $I$ will be this cardinal $n$. Note that $n^{|A|} = n^{|B|} = n^{|\text{Fmla}_\mathcal{L}|} = n$, hence $|A|, |B|, |\text{Fmla}_\mathcal{L}| < n^\partial$.

The proof constructs by transfinite recursion on $\gamma \leq 2^n$ a sequence of sets of functions $F_\gamma$, filters $D_\gamma$ over $n$, and relations $H_\gamma$, maintaining $(F_\gamma, 0, D_\gamma)$ as $(n + |\gamma|)$-consistent. Starting with $F_0$ of size $2^n$ and $D_0 = \{n\}$, the construction alternates between extending the filter to decide memberships (using Lemma 26.40) and adding functions to $G$ to capture witnessing information (using Lemma 26.37). The final filter at stage $2^n$ is an ultrafilter $D$ such that the natural map sending constants to their equivalence classes in the ultrapowers gives the desired isomorphism $\mathfrak{A}^n/D \cong \mathfrak{B}^n/D$.
