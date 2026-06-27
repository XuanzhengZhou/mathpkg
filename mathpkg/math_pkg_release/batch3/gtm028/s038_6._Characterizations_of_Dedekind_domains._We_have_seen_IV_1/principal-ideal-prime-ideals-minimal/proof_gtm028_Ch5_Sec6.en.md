---
role: proof
locale: en
of_concept: principal-ideal-prime-ideals-minimal
source_book: gtm028
source_chapter: "V"
source_section: "6"
---

Let $\mathfrak{p}$ be a prime ideal of $Ra$. If $R'$ denotes the quotient ring $R_{\mathfrak{p}}$, then it is clear that the maximal ideal $\mathfrak{p}' = R'\mathfrak{p}$ of $R'$ is a prime ideal of $R'a$ (IV, Section 10, Theorem 17), and that $\mathfrak{p}$ will be minimal in $R$ if and only if $\mathfrak{p}'$ is minimal in $R'$ (IV, Section 11, Theorem 19). Since also $R'$ is noetherian and integrally closed, it follows that we may assume in the proof that $\mathfrak{p}$ is a maximal ideal.

Under this assumption, Lemma 6 shows that $\mathfrak{p}$ is invertible. We assert that every ideal $\mathfrak{q} \neq 0$ contained in $\mathfrak{p}$ admits $\mathfrak{p}$ as an associated prime ideal. To see this, we observe that we have $\mathfrak{q}(R:\mathfrak{p}) \subset \mathfrak{q}$, whence $\mathfrak{q}(R:\mathfrak{p}) \subset \mathfrak{q}:\mathfrak{p}$. On the other hand, $(\mathfrak{q}:\mathfrak{p}) \subset \mathfrak{q}$; and since $\mathfrak{p}$ is invertible it follows that $\mathfrak{q}:\mathfrak{p} = (\mathfrak{q}:\mathfrak{p})\mathfrak{p}\mathfrak{p}^{-1} \subset \mathfrak{q}\mathfrak{p}^{-1} = \mathfrak{q}(R:\mathfrak{p})$. Hence $\mathfrak{q}:\mathfrak{p} = \mathfrak{q}(R:\mathfrak{p})$. From $\mathfrak{p}(R:\mathfrak{p}) = R$ it follows that $\mathfrak{p} \not\subset \mathfrak{p}^2(R:\mathfrak{p})$; therefore there exists an element $t$ in $\mathfrak{p}(R:\mathfrak{p})$ not in $\mathfrak{p}^2(R:\mathfrak{p})$. This element $t$ satisfies $t\mathfrak{q} \subset \mathfrak{p}\mathfrak{q}$, and from the equality $\mathfrak{q}:\mathfrak{p} = \mathfrak{q}(R:\mathfrak{p})$ we deduce that $\mathfrak{p}$ is an associated prime of $\mathfrak{q}$. Applying this to $\mathfrak{q} = Ra$, we conclude that $\mathfrak{p}$ is minimal among the primes containing $Ra$. Thus $\mathfrak{p}$ is a minimal prime ideal of $R$.
