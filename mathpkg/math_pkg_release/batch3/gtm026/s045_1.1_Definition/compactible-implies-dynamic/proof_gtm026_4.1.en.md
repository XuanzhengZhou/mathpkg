---
role: proof
locale: en
of_concept: compactible-implies-dynamic
source_book: gtm026
source_chapter: "4"
source_section: "1"
---

*Proof.* Let $M$ be compactible. Provide $M$ with a compact Hausdorff topology rendering the left multiplications continuous (and hence closed). $M$ is a nonempty closed right ideal and, by compactness, the intersection of a chain of nonempty closed right ideals is a nonempty closed right ideal. By Zorn's lemma there exists a minimal closed right ideal $I$. We will show that $I$ is a coalescent ideal.

Since $pE$ is closed for any $p$ in $E$, $pE = I$ for all $p$ in $I$ and $I$ is a minimal right ideal. Let $p$ be in $I$. We must show that the restricted left multiplication $L_p: I \rightarrow I$ is injective. This uses Lemma 1.17 to find an idempotent $u$ in $I$ with $pu = p$, and then the properties of the idempotent and the closed equalizer of continuous functions yield the injectivity of $L_p$.

Therefore $I$ is a coalescent ideal, and $M$ is dynamic. The second statement follows immediately from the definition of compactible theory. $\square$
