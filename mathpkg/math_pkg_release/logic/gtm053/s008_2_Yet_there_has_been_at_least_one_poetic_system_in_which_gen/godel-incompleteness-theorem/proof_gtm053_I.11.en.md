---
role: proof
locale: en
of_concept: godel-incompleteness-theorem
source_book: gtm053
source_chapter: "I"
source_section: "11"
---

The proof proceeds by combining Tarski's Undefinability Theorem (11.4) with the observation that provability is definable in arithmetic.

**Step 1: Provability is definable.** Whatever formal definition of deducibility one adopts, it is natural to expect the following property: there exists an algorithm (for example, a computer program) that for any text of the given language determines whether this text is a proof and, if so, of what formula. One can write a program that constructs texts in the language in lexicographic order, verifies whether each is a proof, and, when it is, computes the number of the formula it proves. Roughly speaking, the graph of the function $(\text{number of a proof}) \mapsto (\text{number of the formula proved})$ is definable in $\mathrm{L}_1\mathrm{Ar}$ because machine logic and arithmetic are embedded in $\mathrm{L}_1\mathrm{Ar}$. Hence, the set of numbers of provable formulas is definable in $\mathrm{L}_1\mathrm{Ar}$, in SAr, or in any language $?Ar$ as in 11.5.

**Step 2: Apply Tarski's Theorem.** By Tarski's Undefinability Theorem (11.4), the set of (numbers of) true formulas of $?Ar$ is not definable in $?Ar$. 

**Step 3: Conclusion.** If the set of provable formulas were equal to the set of true formulas, then truth would be definable (since provability is), contradicting Tarski's theorem. Therefore,

$$\{\text{true formulas}\} \neq \{\text{deducible formulas}\}.$$

Since every provable formula is true (soundness), it follows that there exist true formulas that are not provable. The system is therefore incomplete: it cannot prove all arithmetical truths.

A more detailed analysis in Part III of the book shows that the specific undecidable statement can be taken as the formalization of "I am not provable" (the Gödel sentence), and that the argument works for any recursively axiomatizable extension of a sufficiently strong fragment of arithmetic.
