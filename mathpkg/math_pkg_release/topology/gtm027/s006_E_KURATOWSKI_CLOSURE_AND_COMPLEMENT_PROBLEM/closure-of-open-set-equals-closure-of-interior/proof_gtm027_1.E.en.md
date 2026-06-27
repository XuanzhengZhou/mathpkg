---
role: proof
locale: en
of_concept: closure-of-open-set-equals-closure-of-interior
source_book: gtm027
source_chapter: "1"
source_section: "E"
---

# Proof of Closure of an Open Set Equals Closure of Its Interior

Let $X$ be a topological space and let $A \subseteq X$ be the closure of an open set; that is, $A = U^-$ for some open set $U$.

We claim that $A = A^{-c-c}$, where $c$ denotes complementation. Equivalently, $A$ is the closure of the interior of $A$.

**Step 1.** Since $U$ is open and $U \subseteq U^- = A$, we have $U \subseteq A^\circ$ (the interior of $A$). Indeed, $A^\circ$ is the largest open set contained in $A$, and $U$ is an open set contained in $A$.

**Step 2.** Taking closures: $U^- \subseteq (A^\circ)^-$. But $U^- = A$, so $A \subseteq (A^\circ)^-$.

**Step 3.** Conversely, $A^\circ \subseteq A$, so $(A^\circ)^- \subseteq A^- = A$ (since $A$ is closed, being the closure of $U$).

**Step 4.** Therefore $A = (A^\circ)^-$, which is exactly $A = A^{-c-c}$ (the closure of the interior of $A$).

This lemma is the key observation needed to establish that at most 14 distinct sets can be generated from any set by repeated application of closure and complementation.
