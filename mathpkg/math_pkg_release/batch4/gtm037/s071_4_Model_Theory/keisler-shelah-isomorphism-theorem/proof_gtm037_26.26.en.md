---
role: proof
locale: en
of_concept: keisler-shelah-isomorphism-theorem
source_book: gtm037
source_chapter: "26"
source_section: "26"
---

$(ii) \Rightarrow (i)$ is immediate since isomorphic structures are elementarily equivalent and Łoś's theorem ensures elementary equivalence to the ultrapower.

$(i) \Rightarrow (ii)$ (sketch). Assume $\mathfrak{A} \equiv_{\text{ee}} \mathfrak{B}$. Let $n = 2^{|A| + |B| + |\text{Fmla}_{\mathcal{L}}|}$. The index set will be this cardinal $n$. Note $|A|, |B|, |\text{Fmla}_{\mathcal{L}}| < n^{\partial}$.

One constructs by recursion on $\gamma \leq 2^n$ a decreasing family $F_\gamma$ of functions, an increasing family $D_\gamma$ of filters over $n$, such that $(F_\gamma, 0, D_\gamma)$ is $(n + |\gamma|)$-consistent over $n$. The construction uses Lemma 26.37 to add functions from $G$ and Lemma 26.40 to extend the filter to decide sets.

At the final stage $\gamma = 2^n$, $D_{2^n}$ is an ultrafilter over $n$. The ultrapowers $n\mathfrak{A}/D_{2^n}$ and $n\mathfrak{B}/D_{2^n}$ are then shown to be isomorphic via a back-and-forth argument using the consistency conditions that guarantee the existence of appropriate realizing elements.
