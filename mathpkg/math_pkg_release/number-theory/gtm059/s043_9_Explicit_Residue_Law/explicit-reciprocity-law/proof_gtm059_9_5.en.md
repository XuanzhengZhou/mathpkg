---
role: proof
locale: en
of_concept: explicit-reciprocity-law
source_book: gtm059
source_chapter: "9"
source_section: "§5"
---

**Proof.** By LS 4 of §5 in the preceding chapter, we have for $m \ge n$,

$$(x, \pi_n) = (\pi_{3n} - 1, \pi_n).$$

This shifts the burden of the proof to the level $m = 3n$ and $x = \pi_{3n} - 1$ of the main lemma. To apply the main lemma of the preceding section, we need to take $m$ so large that

$$\operatorname{ord}_K(\pi_{3n} - 1) \ge n[2i] + 1 + 2e.$$

Since $[\pi_{3n}]_n(d_i) < p^i$ and $[\pi_{3n}]_n \in \pi_{3n} p^i$, it suffices to take $m \ge 4n + 1 + 4e$.

Let $y = \pi_{3n} - 1$. We apply the main lemma of the preceding section to the amount of $n$ and an appropriate amount to conclude

$$(x, \pi_n) = [x, \pi_n]_n(x),$$

which is the desired formula. The proof uses the logarithmic derivative pairing and the reduction to the case where $x$ has sufficiently high order so that the power series expansions converge and the formal manipulations are justified.
