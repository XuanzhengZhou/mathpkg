---
role: proof
locale: en
of_concept: effaceable-delta-functor-is-universal
source_book: gtm052
source_chapter: "III"
source_section: "1"
---

The proof proceeds by constructing the extension $f^i$ inductively on $i$. For $i = 0$, we are given $f^0: T^0 \to T'^0$.

Assume $f^0, \ldots, f^{i-1}$ have been constructed and commute with the $\delta$'s up to the appropriate level. To construct $f^i: T^i \to T'^i$, take any object $A$. By effaceability of $T^i$, there exists a monomorphism $u: A \hookrightarrow M$ such that $T^i(u) = 0$. Form the short exact sequence
$$0 \to A \xrightarrow{u} M \to N \to 0.$$
From the $\delta$-functor properties, we have exact sequences and connecting morphisms
$$T^{i-1}(N) \xrightarrow{\delta^{i-1}} T^i(A) \xrightarrow{T^i(u)} T^i(M)$$
and similarly for $T'$. Since $T^i(u) = 0$, the morphism $\delta^{i-1}$ is surjective. The commutativity with $f^{i-1}$ forces the definition of $f^i$ on the image of $\delta^{i-1}$, which is all of $T^i(A)$. One then verifies this definition is independent of the choice of embedding $u$, and that the resulting $f^i$ commute with all $\delta$'s. For full details, see Grothendieck [1, II, 2.2.1].
