---
role: proof
locale: en
of_concept: productive-set
source_book: gtm053
source_chapter: "III"
source_section: "7"
---

*This is a definition, not a theorem. The key result using this concept is Proposition 7.6, which states that the set of numbers of true formulas is productive.*

To give the context: working in the language $\mathrm{L}_1\mathrm{Ar}$, construct an enumerable family $\{P_k(x_1)\}$ of formulas with one free variable such that $P_k$ defines $E_k$. This uses the standard construction of terms $\bar{f}[k]$ as in Section 8 of Chapter VI.

Then, using the self-reference lemma (7.3), given any $k$ with $E_k$ contained in the set of true formulas, construct the diagonal formula $Q_{\neg P_k}$ that says "my number does not belong to the set defined by $P_k$." This yields an element $f(k) = N(Q_{\neg P_k})$ that lies in the set of true formulas but not in $E_k$, establishing productivity.
