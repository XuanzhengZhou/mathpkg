---
role: proof
locale: en
of_concept: m-simeq-n-rightarrow-m-n
source_book: gtm001
source_chapter: "9"
source_section: ""
---

(By induction on $n$). If $m \simeq 0$, then $m = 0$. As our induction hypothesis assume that $(\forall m)[m \simeq n \rightarrow m = n]$ and assume that $m \simeq (n + 1)$. It then follows that $m \neq 0$ and hence, for some integer $p$, we have $m = p + 1$. But $p + 1 \simeq n + 1$ implies that $p \simeq n$. (Exercise 5 above.) Then, from the induction hypothesis it follows that $p = n$; hence $m = p + 1 = n + 1$.
