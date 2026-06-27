---
role: proof
locale: en
of_concept: bounded-right-difference-quotients-first-category
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

Since each $E_n$ is closed and nowhere dense in the complete metric space $C$, the set $E = \bigcup_{n=1}^{\infty} E_n$ is a countable union of closed nowhere dense sets. By the definition of first category, $E$ is therefore of first category in $C$.

To see that $E$ is exactly the set of all continuous functions that have bounded right difference quotients at some point of $[0,1)$, observe: if $f \in E$, then $f \in E_n$ for some $n$, which means there exists $x \in [0, 1-1/n]$ such that $|f(x+h)-f(x)| \leq nh$ for all $0 < h < 1-x$, so the right difference quotient $(f(x+h)-f(x))/h$ is bounded by $n$. Conversely, if $f \in C$ has bounded right difference quotients at some point $x \in [0,1)$, then for some integer $n$ the bound $n$ suffices, and $x \in [0, 1-1/n]$ for large enough $n$, so $f \in E_n \subseteq E$.
