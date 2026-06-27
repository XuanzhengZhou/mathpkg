---
role: proof
locale: en
of_concept: ufd-with-maximal-primes-is-pid
source_book: gtm028
source_chapter: "IV"
source_section: "15"
---

In a UFD, every minimal prime ideal is principal. Since every proper prime ideal is assumed maximal, it is also minimal, hence principal. Thus every prime ideal is principal. Now let $\mathfrak{a}$ be any proper ideal. Consider the set of all proper principal ideals containing $\mathfrak{a}$ (non-empty since $\mathfrak{a}$ is contained in some proper prime ideal). Since $R$ is a UFD, there is no infinite strictly descending chain of principal ideals, so a minimal such principal ideal $Ry$ exists. From $\mathfrak{a} \subset Ry$, we have $\mathfrak{a} = y \mathfrak{a}_1$ with $\mathfrak{a}_1 \neq (0)$. If $\mathfrak{a}_1$ were proper, it would be contained in $Rz$ for some non-unit $z \neq 0$, giving $\mathfrak{a} \subset Ryz \subsetneq Ry$, contradiction. Hence $\mathfrak{a}_1 = R$ and $\mathfrak{a} = Ry$, proving $\mathfrak{a}$ is principal.
