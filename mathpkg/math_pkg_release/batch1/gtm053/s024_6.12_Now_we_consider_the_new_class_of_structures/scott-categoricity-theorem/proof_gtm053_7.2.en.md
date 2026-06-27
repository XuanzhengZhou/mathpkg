---
role: proof
locale: en
of_concept: scott-categoricity-theorem
source_book: gtm053
source_chapter: "7"
source_section: "7.2"
---

The proof constructs the Scott sentence $\Sigma(A)$ by an infinitary back-and-forth argument. For each $n < \omega$, one defines formulas $\varphi_{\bar{a}}^n(\bar{x})$ that characterize the $n$-type of the finite tuple $\bar{a}$ in $A$. These formulas are built inductively: $\varphi_{\bar{a}}^0(\bar{x})$ is the conjunction of all atomic and negated atomic formulas true of $\bar{a}$; for the inductive step, $\varphi_{\bar{a}}^{n+1}(\bar{x})$ asserts that for every extension $b$ of $\bar{a}$ there is an element $y$ in the model satisfying $\varphi_{\bar{a}b}^n(\bar{x}, y)$, and for every $y$ there exists such a $b$ in $A$. The Scott sentence is then the conjunction over all tuples $\bar{a}$ in $A$ of the countable conjunction $\bigwedge_n \forall \bar{x} (\varphi_{\bar{a}}^{n+1}(\bar{x}) \to \varphi_{\bar{a}}^n(\bar{x}))$ together with $\varphi_{\emptyset}^0$. By a back-and-forth argument, any two countable models of $\Sigma(A)$ are isomorphic.
