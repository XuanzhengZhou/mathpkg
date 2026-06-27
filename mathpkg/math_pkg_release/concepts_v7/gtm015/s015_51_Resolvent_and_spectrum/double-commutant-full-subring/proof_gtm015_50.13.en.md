---
role: proof
locale: en
of_concept: double-commutant-full-subring
source_book: gtm015
source_chapter: "50"
source_section: "50.13"
---

# Proof of The Double Commutant is a Full Subring

**Proof.** (i) By definition, $T'$ is the commutant of $T$, i.e., the set of all elements of $A$ that commute with every element of $T$. Then $T'' = (T')'$ is the double commutant. 

Clearly $T \subset T''$. To show $T''$ is a full subring: if $x \in T''$ is invertible in $A$, then for any $y \in T'$, we have $xy = yx$. Multiplying on left and right by $x^{-1}$ yields $yx^{-1} = x^{-1}y$, so $x^{-1} \in T''$. Thus $T''$ is a full subring.

(ii) Let $\{B_i\}$ be a family of full subrings. If $x \in \bigcap B_i$ is invertible, then $x^{-1} \in B_i$ for each $i$, so $x^{-1} \in \bigcap B_i$.

(iii) Take the intersection of all full subrings containing $T$; this is the smallest such subring, and by (i) it is contained in $T''$.
