---
role: proof
locale: en
of_concept: z-ultrafilter-product-lemma
source_book: gtm043
source_chapter: "4"
source_section: "4.13"
---

For each \(\alpha\), choose \(x_{\alpha} \in \bigcap \pi_{\alpha}^\# A\), and let \(x\) denote the point \((x_{\alpha})\) of \(X\). We shall show that \(x \in \bigcap A\).

By the definition of \(\pi_{\alpha}^\#\), a zero-set \(Z_{\alpha} \in Z(X_{\alpha})\) belongs to \(\pi_{\alpha}^\# A\) precisely when \(\pi_{\alpha}^{\leftarrow}[Z_{\alpha}] \in A\). Since \(x_{\alpha} \in \bigcap \pi_{\alpha}^\# A\), we have \(x_{\alpha} \in Z_{\alpha}\) whenever \(\pi_{\alpha}^{\leftarrow}[Z_{\alpha}] \in A\). Hence \(x \in \pi_{\alpha}^{\leftarrow}[Z_{\alpha}]\) for every such set, i.e., \(x\) belongs to every member of \(A\) of the form \(\pi_{\alpha}^{\leftarrow}[Z_{\alpha}]\).

Since \(A\) is a prime \(z\)-filter (being a \(z\)-ultrafilter), \(x\) belongs to every member of \(A\) of the form \(\bigcup_{\alpha} \pi_{\alpha}^{\leftarrow}[Z_{\alpha}]\) (finite unions of such preimages). Finally, an arbitrary member of \(A\) is an intersection of sets of the latter form (basic zero-sets in the product topology); consequently, \(x\) belongs to every member of \(A\). Therefore \(\bigcap A \neq \varnothing\), and \(A\) is fixed.
