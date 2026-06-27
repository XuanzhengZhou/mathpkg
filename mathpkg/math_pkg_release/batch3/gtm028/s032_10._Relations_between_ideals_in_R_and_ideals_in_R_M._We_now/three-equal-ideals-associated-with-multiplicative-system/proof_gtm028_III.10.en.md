---
role: proof
locale: en
of_concept: three-equal-ideals-associated-with-multiplicative-system
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

We prove the chain of inclusions $\mathfrak{n} \subset \mathfrak{n}' \subset \mathfrak{n}'' \subset \mathfrak{n}$.

\textbf{Inclusion $\mathfrak{n} \subset \mathfrak{n}'$:} This follows from Theorem 16(a). For any primary ideal $\mathfrak{q}$ disjoint from $M$, Theorem 16(a) asserts that $\mathfrak{n} \subset \mathfrak{q}$ (the kernel is contained in every contracted ideal disjoint from $M$). Taking the intersection over all such primary ideals yields $\mathfrak{n} \subset \mathfrak{n}'$.

\textbf{Inclusion $\mathfrak{n}' \subset \mathfrak{n}''$:} This is obvious, since $\mathfrak{n}''$ is the intersection of a subset of the primary ideals whose intersection defines $\mathfrak{n}'$ (namely, only those primary ideals that are primary components of $(0)$).

\textbf{Inclusion $\mathfrak{n}'' \subset \mathfrak{n}$:} Since $M$ is closed under multiplication, there exists an element $m \in M$ which belongs to all the primary components of $(0)$ that meet $M$ (this follows from the fact that $M$ is a multiplicative system and the prime avoidance lemma). If $m$ is such an element, then for any $x \in \mathfrak{n}''$, we have $x$ belonging to all primary components of $(0)$ that are disjoint from $M$. Taking the full primary decomposition of $(0)$, the fact that $x$ is in the components disjoint from $M$ and $m$ is in the components meeting $M$ implies $mx = 0$ (since $mx$ lies in all primary components of $(0)$, hence in $(0)$ itself). Therefore $x \in \mathfrak{n}$, proving $\mathfrak{n}'' \subset \mathfrak{n}$.

The three inclusions together establish $\mathfrak{n} = \mathfrak{n}' = \mathfrak{n}''$. Q.E.D.
