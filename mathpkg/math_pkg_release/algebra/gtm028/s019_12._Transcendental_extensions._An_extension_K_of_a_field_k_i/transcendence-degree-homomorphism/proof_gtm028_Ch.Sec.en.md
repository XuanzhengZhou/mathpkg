---
role: proof
locale: en
of_concept: transcendence-degree-homomorphism
source_book: gtm028
source_chapter: "II. Elements of Field Theory"
source_section: "§12. Transcendental Extensions"
---

We assume that there exists a $k$-homomorphism $\tau$ of $R$ onto $R'$ and we consider a transcendence basis $L'$ of $R'/k$. For every element $x'$ of $L'$ we fix an element $x$ in $R$ such that $x' = x\tau$ and we denote by $L$ the set of all elements $x$ obtained in this fashion.

From the fact that $L'$ is a transcendence set, it follows at once that also $L$ is a transcendence set. For if a nonzero polynomial $f$ with coefficients in $k$ vanished on a finite subset of $L$, then applying $\tau$ would give the same relation on the corresponding elements of $L'$, contradicting algebraic independence.

By Theorem 23, $L$ is contained in some transcendence basis $M$ of $R/k$. The cardinal numbers of $L'$ and $L$ are the same since for every $x'$ in $L'$ there is only one element $x$ in $L$ such that $x' = x\tau$ and since therefore the correspondence $x' \to x$ is one-to-one. Since $L$ is a subset of $M$, we have $|L'| = |L| \leq |M| = \operatorname{tr.d.} R/k$, which completes the proof.
