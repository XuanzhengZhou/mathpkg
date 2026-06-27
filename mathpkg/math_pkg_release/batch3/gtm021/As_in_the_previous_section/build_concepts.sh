#!/bin/bash
# Batch concept extraction for GTM021 Chapters 23-30
set -e
BASE="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch3/gtm021/As_in_the_previous_section"

write_yaml() {
  local dir="$1" id="$2" type="$3" title_en="$4" dep_req="$5" dep_rec="$6" dep_sug="$7" ch="$8" sec="$9" role="${10}"
  mkdir -p "$dir"
  cat > "$dir/concept.yaml" << YAMLEND
id: "$id"
title_en: "$title_en"
title_zh: ""
type: $type
domain: algebra
subdomain: algebraic-groups
difficulty: advanced
tags: []
depends_on: {required: [$dep_req], recommended: [$dep_rec], suggested: [$dep_sug]}
source_books: [{book_id: "gtm021", author: "James E. Humphreys", title: "Linear Algebraic Groups", chapter: "$ch", section: "$sec", pages: "", role_in_book: "$role"}]
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
YAMLEND
}

# ============================================================
# SECTION 24: Regular and Singular Tori
# ============================================================

# Concept 6: Weyl group definition
d="$BASE/weyl-group-of-torus"
write_yaml "$d" "weyl-group-of-torus" "definition" "Weyl group of an algebraic group relative to a torus" "" "rigidity-of-tori" "" "24" "24.1" "defining-the-weyl-group"
cat > "$d/theorem.tex" << 'TEXEND'
Let $S$ be any torus in a connected algebraic group $G$. Because of the rigidity of tori, $N_G(S)/C_G(S)$ is a finite group, called the Weyl group of $G$ relative to $S$ and denoted $W(G, S)$. Since all maximal tori are conjugate, all their Weyl groups are isomorphic; such a group is called simply the Weyl group of $G$.
TEXEND
cat > "$d/introduce.en.md" << 'MDEND'
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
The Weyl group of an algebraic group relative to a torus is the finite quotient $N_G(S)/C_G(S)$. It measures how the torus sits inside the group by capturing the outer automorphisms induced by conjugation. For maximal tori, the Weyl group is an invariant of the group up to isomorphism.
MDEND
echo "Concept 6 done"

# Concept 7: Proposition 24.1A
d="$BASE/centralizer-of-maximal-torus-in-borel"
write_yaml "$d" "centralizer-of-maximal-torus-in-borel" "proposition" "Centralizer of maximal torus lies in every Borel subgroup and Weyl group acts simply transitively" "weyl-group-of-torus" "conjugacy-theorem" "" "24" "24.1" "weyl-group-action-on-borel-containing-torus"
cat > "$d/theorem.tex" << 'TEXEND'
Let $T$ be a maximal torus of a connected algebraic group $G$, $C = C_G(T)$. Then $C$ lies in every Borel subgroup containing $T$, and the finite group $W = N_G(T)/C$ acts simply transitively on the set $\mathfrak{B}^T$ of Borel subgroups containing $T$.
TEXEND
cat > "$d/introduce.en.md" << 'MDEND'
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This proposition establishes that the centralizer of a maximal torus is contained in every Borel subgroup that contains the torus. Moreover, the Weyl group acts simply transitively on the finite set of Borel subgroups containing a fixed maximal torus, providing a concrete interpretation of the Weyl group.
MDEND
cat > "$d/proof_gtm021_24.24.1.en.md" << 'PROOFEND'
---
role: proof
locale: en
of_concept: centralizer-of-maximal-torus-in-borel
source_book: gtm021
source_chapter: "24"
source_section: "24.1"
---
First we show that $W$ acts transitively. Let $B_1, B_2 \in \mathfrak{B}^T$. The conjugacy theorem shows that $xB_2x^{-1} = B_1$, for some $x \in G$. Since $xTx^{-1}$ and $T$ are maximal tori of $B_1$, there also exists $y \in B_1$, such that $yxTx^{-1}y^{-1} = T$, so $z = yx \in N_G(T)$. But $zB_2z^{-1} = B_1$, so the coset of $z$ in $W$ sends $B_2$ to $B_1$.

To say that $W$ acts simply transitively is just to say that the isotropy group in $W$ of $B \in \mathfrak{B}^T$ is trivial, i.e., that if $x \in N_G(T)$ satisfies $xBx^{-1} = B$, then $x \in C_G(T)$. But $N_G(B) = B$ (23.1), while $N_B(T) = C_B(T)$ (19.4), so this follows.
PROOFEND
echo "Concept 7 done"

# Concept 8: Proposition 24.1B
d="$BASE/epimorphism-maps-borel-tori-and-weyl-groups"
write_yaml "$d" "epimorphism-maps-borel-tori-and-weyl-groups" "proposition" "Epimorphism induces surjective maps on Borel-fixed-points and Weyl groups" "weyl-group-of-torus" "centralizer-of-maximal-torus-in-borel" "" "24" "24.1" "functoriality-of-weyl-group"
cat > "$d/theorem.tex" << 'TEXEND'
Let $\varphi: G \rightarrow G'$ be an epimorphism of algebraic groups, with $T$ and $T' = \varphi(T)$ respective maximal tori. Then $\varphi$ induces surjective maps $\mathfrak{B}^T \rightarrow \mathfrak{B}'^T$ and $W(G, T) \rightarrow W(G', T')$, which are also injective in case $\operatorname{Ker} \varphi$ lies in all Borel subgroups of $G$.
TEXEND
cat > "$d/introduce.en.md" << 'MDEND'
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This proposition describes the functorial behavior of Borel subgroups containing a maximal torus and the Weyl group under epimorphisms of algebraic groups. The maps are always surjective and become injective when the kernel is contained in all Borel subgroups.
MDEND
cat > "$d/proof_gtm021_24.24.1.en.md" << 'PROOFEND'
---
role: proof
locale: en
of_concept: epimorphism-maps-borel-tori-and-weyl-groups
source_book: gtm021
source_chapter: "24"
source_section: "24.1"
---
If $B$ is a Borel subgroup of $G$ containing $T$, then $\varphi(B)$ is a Borel subgroup of $G'$ containing $T'$ (by properties of epimorphisms and Corollary 21.3C). This gives a map $\mathfrak{B}^T \rightarrow \mathfrak{B}'^T$. Surjectivity follows from the conjugacy theorem. For the Weyl group map, if $n \in N_G(T)$, then $\varphi(n) \in N_{G'}(T')$, inducing a homomorphism $W(G,T) \rightarrow W(G',T')$. When $\operatorname{Ker} \varphi$ lies in all Borel subgroups, the preimage of $B'$ is a single Borel subgroup, giving injectivity.
PROOFEND
echo "Concept 8 done"

# Concept 9: Proposition 24.2
d="$BASE/torus-regular-iff-centralizer-solvable"
write_yaml "$d" "torus-regular-iff-centralizer-solvable" "proposition" "A torus is regular if and only if its centralizer is solvable" "weyl-group-of-torus" "regular-singular-tori" "" "24" "24.2" "characterization-of-regular-tori"
cat > "$d/theorem.tex" << 'TEXEND'
Let $S$ be a torus in a connected algebraic group $G$, and let $C = C_G(S)$. Then $S$ is regular if and only if $C$ is solvable. In that case $C$ lies in every Borel subgroup of $G$ containing $S$, and for each maximal torus $T$ containing $S$, $\mathfrak{B}^T = \mathfrak{B}^S$.
TEXEND
cat > "$d/introduce.en.md" << 'MDEND'
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This proposition characterizes regular tori: a torus is regular precisely when its centralizer is solvable. This connects the finiteness of $\mathfrak{B}^S$ (the definition of regularity) to the structure of the centralizer. When $S$ is regular, its centralizer is contained in every Borel subgroup that contains $S$.
MDEND
cat > "$d/proof_gtm021_24.24.2.en.md" << 'PROOFEND'
---
role: proof
locale: en
of_concept: torus-regular-iff-centralizer-solvable
source_book: gtm021
source_chapter: "24"
source_section: "24.2"
---
Identify $\mathfrak{B}^S$ with a closed subset $X$ of some $G/B$, $B \supset S$. The connected components $Y$ of $X$ all have dimension equal to the codimension in $C$ of a Borel subgroup of $C$. As a result, $S$ is regular $\Leftrightarrow$ $\mathfrak{B}^S$ is finite $\Leftrightarrow$ $C$ is a Borel subgroup of itself (i.e., $C$ is solvable).
PROOFEND
echo "Concept 9 done"

# Concept 10: Proposition 24.3
d="$BASE/singular-torus-contained-in-root-kernel"
write_yaml "$d" "singular-torus-contained-in-root-kernel" "proposition" "A torus is singular iff contained in the kernel of some root" "torus-regular-iff-centralizer-solvable" "root-system" "" "24" "24.3" "characterization-of-singular-tori"
cat > "$d/theorem.tex" << 'TEXEND'
Let $S$ be a torus in a connected algebraic group $G$, and let $T$ be a maximal torus containing $S$. Then $S$ is singular if and only if $S \subset T_\alpha = (\operatorname{Ker} \alpha)^\circ$ for some $\alpha \in \Psi$.
TEXEND
cat > "$d/introduce.en.md" << 'MDEND'
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This proposition characterizes singular tori as those contained in the connected kernel of some root $\alpha \in \Psi$. Here $\Psi$ denotes the set of roots that are not purely from the Lie algebra of $I(T)$, and $T_\alpha$ is a subtorus of codimension 1 in the maximal torus.
MDEND
cat > "$d/proof_gtm021_24.24.3.en.md" << 'PROOFEND'
---
role: proof
locale: en
of_concept: singular-torus-contained-in-root-kernel
source_book: gtm021
source_chapter: "24"
source_section: "24.3"
---
Let $S$ be singular. Then $C = C_G(S)$ is nonsolvable (24.2); in particular, $C$ has larger dimension than the solvable group $C \cap I(T)$, so the space of fixed points of $S$ in $\mathfrak{g}$ is not wholly included in $\mathcal{L}(I(T))$. If $S$ fixes $x \in \mathfrak{g}$, it also fixes the various $\mathfrak{g}'_\alpha$ components of $x$, so we conclude that $S \subset \operatorname{Ker} \alpha$ for at least one $\alpha \in \Psi$. But then $S \subset T_\alpha$.

Conversely, let $S \subset T_\alpha$ for some $\alpha \in \Psi$. If $S$ is not singular, then $C$ must be solvable and lie in all Borel subgroups of $G$ including $S$; in particular, $C \subset I(T)$. Since the global and infinitesimal centralizers of $S$ correspond (Proposition 18.4A), all the fixed points of $S$ in $\mathfrak{g}$ must lie in $\mathcal{L}(I(T))$, contrary to the definition of $\Psi$.
PROOFEND
echo "Concept 10 done"

# Concept 11: Corollary 24.3
d="$BASE/centralizer-of-root-kernel-mod-radical-rank-1"
write_yaml "$d" "centralizer-of-root-kernel-mod-radical-rank-1" "corollary" "Quotient of centralizer of root kernel by its radical is semisimple of rank 1" "singular-torus-contained-in-root-kernel" "semisimple-rank" "" "24" "24.3" "construction-of-rank-1-semisimple-groups"
cat > "$d/theorem.tex" << 'TEXEND'
For $\alpha \in \Psi$, set $Z_\alpha = C_G(T_\alpha)$ where $T_\alpha = (\operatorname{Ker} \alpha)^\circ$. Then $G_\alpha = Z_\alpha/R(Z_\alpha)$ is a semisimple group of rank 1.
TEXEND
cat > "$d/introduce.en.md" << 'MDEND'
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
This corollary constructs rank-1 semisimple groups from a root $\alpha$. The group $Z_\alpha$ is the centralizer of the codimension-1 torus $T_\alpha$, and after factoring out its radical, one obtains a semisimple group of rank 1. These groups play a crucial role in understanding the structure of $G$.
MDEND
cat > "$d/proof_gtm021_24.24.3.en.md" << 'PROOFEND'
---
role: proof
locale: en
of_concept: centralizer-of-root-kernel-mod-radical-rank-1
source_book: gtm021
source_chapter: "24"
source_section: "24.3"
---
Since $T_\alpha$ is singular, the connected group $Z_\alpha$ is not solvable. Its radical $R(Z_\alpha)$ is a solvable normal subgroup; factoring it out yields a semisimple group $G_\alpha$. The maximal torus of $G_\alpha$ has dimension 1 (since $T_\alpha$ has codimension 1 in $T$), so the semisimple rank is 1.
PROOFEND
echo "Concept 11 done"

echo "=== Section 24 complete (concepts 6-11) ==="
