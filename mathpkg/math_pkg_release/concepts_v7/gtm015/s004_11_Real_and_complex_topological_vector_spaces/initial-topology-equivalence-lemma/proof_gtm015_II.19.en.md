---
role: proof
locale: en
of_concept: initial-topology-equivalence-lemma
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "19. Initial topologies"
---

# Proof that Initial Topology for a Family Equals Initial Topology for the Product Mapping

**Lemma (19.2).** If $E$ is a set, $(E_\iota)_{\iota \in I}$ is a family of topological spaces, and $f_\iota : E \to E_\iota$ ($\iota \in I$) is a family of mappings, then the initial topology for the family $(f_\iota)_{\iota \in I}$ coincides with the initial topology for the mapping

$$f: E \to F = \prod_{\iota \in I} E_\iota$$

defined by $f(x) = (f_\iota(x))_{\iota \in I}$.

*Proof.* A base for the product topology on $F$ is given by the sets

$$U = \prod_{\iota \in I} U_\iota,$$

where, for a suitable finite subset $J$ of $I$, $U_\iota = E_\iota$ for $\iota \notin J$, and $U_\iota$ is an open subset of $E_\iota$ for $\iota \in J$. The preimage under $f$ of such a set is

$$f^{-1}(U) = \bigcap_{\iota \in J} f_\iota^{-1}(U_\iota),$$

which is precisely a basic open set for the initial topology of the family $(f_\iota)_{\iota \in I}$. Thus the two initial topologies have identical bases, hence coincide. $\square$
