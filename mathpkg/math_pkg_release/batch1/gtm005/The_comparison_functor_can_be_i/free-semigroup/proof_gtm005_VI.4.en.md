---
role: proof
locale: en
of_concept: free-semigroup
source_book: gtm005
source_chapter: "VI"
source_section: "4"
---

By definition, $\eta x = \langle x \rangle$, while $\mu = G\varepsilon F : W^2 \to W$ is determined by the formula for the counit $\varepsilon_S$ of the free-forgetful adjunction, where we have written each element of $W^2 X$ as a word (of length $k$) in $k$ words of the respective lengths $n_1, \dots, n_k$.

More briefly, $\mu_X$ applied to a word of words removes the outer pointy brackets.

This description allows direct verification of the unit and associative laws for the monad $W$, without overt reference to the notion of a semigroup. For example, the associative law for $\mu$ amounts to an observation on three layers of pointy brackets: removing first the middle brackets and then the outer brackets gives the same result as removing first the outer brackets and then the (newly) outer brackets.
