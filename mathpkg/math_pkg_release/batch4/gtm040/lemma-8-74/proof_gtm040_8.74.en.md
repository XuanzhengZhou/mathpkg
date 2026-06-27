---
role: proof
locale: en
of_concept: lemma-8-74
source_book: gtm040
source_chapter: "8"
source_section: "74"
---

**Proof:** We shall proceed by induction on $k$. If $k = 0$, the result is trivial. Suppose that both quantities exist for some $k$ and that they correspond. Then

$$(P^{k+1}f)_i = \sum_j P_{ij}(P^k f)_j$$

or

$$(P^{k+1}f)_{\langle U,n \rangle} = \sum_{V \in U \atop V \in \mathcal{R}_{n+1}} \frac{\mu(V)}{\mu(U)} (P^k f)_{\langle V,n+1 \rangle}.$$

By inductive hypothesis, $(\mathbf{M}[f_{n+k} \mid \mathcal{R}_n], \mathcal{R}_n) \sim P^k f$. Hence, by definition of the correspond

That is, $P^{k+1}f$ exists if and only if $M[f_{n+k+1} \mid \mathcal{R}_n]$ does, and if they exist, then they correspond.
