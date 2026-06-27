---
role: proof
locale: en
of_concept: hyper-real-ideal-properties
source_book: gtm043
source_chapter: "5"
source_section: "5.7"
---

**(a)** If $f$ is bounded, say $|f| \leq n$, then $|M(f)| \leq n$ for every maximal ideal $M$, so $M(f)$ is never infinitely large. Conversely, if $f$ is unbounded, consider the family of zero-sets $Z_n = \{x : |f(x)| \geq n\}$ for $n \in \mathbf{N}$. This family has the finite intersection property (each $Z_n$ is nonempty, and $Z_{n+1} \subseteq Z_n$). Hence it extends to a $z$-ultrafilter $\mathcal{A}$. The corresponding maximal ideal $M = Z^{\leftarrow}[\mathcal{A}]$ satisfies $|M(f)| \geq n$ for all $n$, so $|M(f)|$ is infinitely large.

**(b)** This follows immediately from (a) and Lemma 4.10: every zero-set associated with a free ideal is noncompact, and conversely, every noncompact zero-set belongs to $Z[I]$ for some free ideal $I$, hence to $Z[M]$ for some free maximal ideal $M$.

**(c)** This reformulates (a) with emphasis on the construction: if $f$ is unbounded, the sets $Z_n = \{x : |f(x)| \geq n\}$ form a family with the finite intersection property, embeddable in a $z$-ultrafilter $\mathcal{A}$. Then $M = Z^{\leftarrow}[\mathcal{A}]$ is maximal, and $M(f)$ is infinitely large.
