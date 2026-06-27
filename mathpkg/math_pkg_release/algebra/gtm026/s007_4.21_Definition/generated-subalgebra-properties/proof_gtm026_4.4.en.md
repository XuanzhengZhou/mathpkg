---
role: proof
locale: en
of_concept: generated-subalgebra-properties
source_book: gtm026
source_chapter: "4"
source_section: "4"
---

**Proof of (4.31).** 

(1) $A \subset \langle A \rangle$: The diagram defining $\langle A \rangle$ is commutative because $\eta$ is natural and $X\eta \cdot \xi = \mathrm{id}_X$. For $a \in A$, we have $a = a\eta \cdot \xi \in \mathrm{Im}(iT \cdot \xi) = \langle A \rangle$.

(2) If $A \subset B$, then $\langle A \rangle \subset \langle B \rangle$: This is obvious from the definition, as the image construction is monotone with respect to inclusion.

(3) $\langle A \rangle$ is a $T$-subalgebra: Since $iT \cdot \xi: (AT, A\mu) \longrightarrow (X, \xi)$ is a $T$-homomorphism (where $A\mu$ is the multiplication of the free $T$-algebra on $A$), its image $\langle A \rangle$ is a subalgebra by (4.32).

(4) If $B$ is a $T$-subalgebra, then $B = \langle B \rangle$: This follows directly from the definition of $T$-subalgebra.

(5) $\langle \langle A \rangle \rangle = \langle A \rangle$: Since $\langle A \rangle$ is a $T$-subalgebra by (3), applying (4) yields the result.

(6) If $A \subset B$ and $B$ is a $T$-subalgebra, then $\langle A \rangle \subset \langle B \rangle = B$ by (2) and (4). $\square$
