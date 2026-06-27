---
role: proof
locale: en
of_concept: tychonoff-product-theorem-via-z-filters
source_book: gtm043
source_chapter: "4"
source_section: "4.14"
---

Let \(X = \prod_{\alpha} X_{\alpha}\), where each \(X_{\alpha}\) is compact. As a product of completely regular spaces, \(X\) is completely regular.

Now consider any \(z\)-ultrafilter \(A\) on \(X\). For each \(\alpha\), consider the projected \(z\)-filter \(\pi_{\alpha}^\# A\) on \(X_{\alpha}\). Since each space \(X_{\alpha}\) is compact, every \(z\)-filter on \(X_{\alpha}\) is fixed (by Theorem 4.11, compactness implies all \(z\)-filters are fixed). In particular, each \(\pi_{\alpha}^\# A\) is fixed.

By the lemma of 4.13, if every projected \(z\)-filter \(\pi_{\alpha}^\# A\) is fixed, then \(A\) itself is fixed. Since \(A\) was an arbitrary \(z\)-ultrafilter, every \(z\)-ultrafilter on \(X\) is fixed. By Theorem 4.11 again, this is equivalent to \(X\) being compact. Therefore \(X\) is compact.
