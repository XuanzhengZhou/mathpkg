---
role: proof
locale: en
of_concept: theorem-15-16-d-discrete-equivalence
source_book: gtm043
source_chapter: "15"
source_section: "16"
---
$(2) \Rightarrow (3)$. This follows as in Theorem 15.16, except that transfinite induction is now used in place of ordinary induction.

$(3) \Rightarrow (2)$. Let $S$ be a $d$-discrete set. By hypothesis, $X$ is a nonmeasurable union of sets of $d$-diameter smaller than a gauge for $S$; and each of these contains at most one point of $S$.

$(2) \Rightarrow (4)$. This is Lemma 15.19.

$(4) \Rightarrow (2)$. Let $S$ be a $d$-discrete set in $X$. Then $S$ is $C$-embedded in $X$ (15.15(b)), so that $\operatorname{cl}_{vX} S = vS$ (8.10(a)). Hence the hypothesis implies that $vS \subset cX$. Given $p \in vS$, let $V$ be a neighborhood of $p$ in $cX$ whose $d^c$-diameter is less than a gauge for $S$. Then $V \cap S$ contains at most one point. But $p \in \operatorname{cl}_{cX}(V \cap S)$, because $p \in \operatorname{cl} S$. Therefore, $p \in V \cap S \subset S$. This shows that $vS \subset S$, i.e., the discrete space $S$ is realcompact. Hence its cardinal is nonmeasurable.

$(2) \Rightarrow (1)$. We prove, first, that the condition corresponding to (2) holds for subsets of $\gamma X$. Let $T$ be any $u$-discrete subset of $\gamma X$. Construct $S \subset X$ by selecting, for each $t \in T$, a point $s \in X$ such that $u(t, s) < \delta/3$, where $\delta$ is a gauge for $T$. Then $S$ is $d$-discrete (with gauge $\delta/3$), where $d$ is the restriction of $u$. Hence the cardinal $|T| = |S|$ is nonmeasurable. It follows that every real $z$-ultrafilter on $X$ is Cauchy.
