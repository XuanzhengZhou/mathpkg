---
role: proof
locale: en
of_concept: no-smallest-infinite-natural
source_book: gtm022
source_chapter: "VIII"
source_section: "6"
---

If $n$ is a natural number and $n \neq 0$, then $n = m + 1$ for some natural number $m$, since this result is a theorem of $\mathcal{T}(\mathbb{N})$. If $n$ is the smallest infinite natural number, then $n \neq 0$ (since $0$ is finite), so $n = m + 1$. But then $m < n$, and $m$ must be finite (else $n$ would not be the smallest infinite). However, if $m$ is finite, then $n = m + 1$ is also finite, a contradiction. Hence there is no smallest infinite natural number.

To see that the set of infinite natural numbers is external, note that if it were an internal set $u$, then the statement "$u$ has no greatest member" would be true in the enlargement, but this would imply (by transfer of the least upper bound property for non-empty bounded subsets) a contradiction as described in the discussion of the completeness property of $\mathbb{R}$.
