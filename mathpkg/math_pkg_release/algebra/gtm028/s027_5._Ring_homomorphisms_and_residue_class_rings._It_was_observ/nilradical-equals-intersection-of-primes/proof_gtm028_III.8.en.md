---
role: proof
locale: en
of_concept: nilradical-equals-intersection-of-primes
source_book: gtm028
source_chapter: "III"
source_section: "§8"
---

It is easily seen that every nilpotent element is contained in every prime ideal. Hence the main point that has to be proved is that if an element $u$ of $R$ is not nilpotent, then there exists a prime ideal not containing $u$. To prove this we consider the set $\mathcal{J}$ of all ideals $\mathfrak{A}$ in $R$ which contain no power of $u$. Since $u$ is not nilpotent, the zero ideal belongs to $\mathcal{J}$, and thus $\mathcal{J}$ is non-empty. It is obvious that $\mathcal{J}$ is inductive. Let, by Zorn's Lemma, $\mathfrak{p}$ be a maximal element of $\mathcal{J}$. Then $u \notin \mathfrak{p}$. We claim that $\mathfrak{p}$ is a prime ideal. For, let $x$ and $y$ be elements of $R$ which do not belong to $\mathfrak{p}$. Then $\mathfrak{p} + (x) > \mathfrak{p}$ and hence some power $u^m$ belongs to $\mathfrak{p} + (x)$. Similarly some power $u^n$ belongs to $\mathfrak{p} + (y)$. Then $u^{m+n}$ belongs to $\mathfrak{p} + (xy)$, and since $u^{m+n} \notin \mathfrak{p}$ it follows that $xy \notin \mathfrak{p}$, showing that $\mathfrak{p}$ is a prime ideal.
