---
role: proof
locale: en
of_concept: finite-intersections-form-a-base
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Finite Intersections of a Family Form a Base

**Theorem.** If $s$ is a non-empty family of sets, then the family of finite intersections of members of $s$ is the base for a topology for the set $X = igcup \{S : S \in s\}$.

**Proof.** If $s$ is a family of sets let $\mathcal{B}$ be the family of finite intersections of members of $s$. Then the intersection of two members of $\mathcal{B}$ is again a member of $\mathcal{B}$ (since the intersection of two finite intersections is again a finite intersection). Applying the preceding theorem (Theorem 11), $\mathcal{B}$ is the base for a topology. $\square$