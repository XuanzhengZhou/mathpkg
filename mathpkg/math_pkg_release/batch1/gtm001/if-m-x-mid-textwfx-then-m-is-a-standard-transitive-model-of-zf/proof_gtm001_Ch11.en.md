---
role: proof
locale: en
of_concept: if-m-x-mid-textwfx-then-m-is-a-standard-transitive-model-of-zf
source_book: gtm001
source_chapter: "11"
source_section: ""
---

** Since $0 \in R_1'$ we have $0 \in M$, i.e., $M \neq 0$. If $x \in M$ then $(\exists \alpha)[x \in R_1' \alpha]$. Since $R_1' \alpha$ is transitive $x \in R_1' \alpha \rightarrow x \subseteq R_1' \alpha$ and hence $x \subseteq M$. Thus $M$ is transitive. Since $M$ is nonempty and transitive $M$ is a model of Axiom 1.

Recall that a set is well founded if each of its elements is well founded. Consequently if $a \in M \land b \in M$ then $\{a, b\} \in M$. Thus $M$ is a model of Axiom 2.

If $a \in M$ then $b \in \cup(a) \rightarrow (\exists x)[b \in x \land x \in a]$. Since $M$ is transitive it follows that $\cup(a) \subseteq M$, hence $\cup(a) \in M$. Thus $M$ is a model of Axiom 3.

If $a \in M \land b \subseteq a$ then since $M$ is transitive $b \subseteq M$ and hence $b \in M$. Thus $\mathcal{P}(a) \subseteq M$ and hence $\mathcal{P}(a) \in M$. Thus $M$ is a model of Axiom 4.

If $(\forall x \in M)(\forall y \in M)(\forall z \in M)[\varphi^M(x, y) \land \varphi^M(x, z) \rightarrow y = z]$ and if $a \in M$

If $a \in R_1' \aleph_\alpha$ then
$$\text{rank} (\cup(a)) = \mu_\gamma ((\forall x \in \cup(a)) [\text{rank}(x) < \gamma]) \leq \text{rank}(a).$$

Therefore $\cup(a) \in R_1' \aleph_\alpha$ and $R_1' \aleph_\alpha$ is a model of Axiom 3.

If $a \in R_1' \aleph_\alpha$ then $\mathcal{P}(a) \subseteq R_1' \aleph_\alpha$ and hence $\mathcal{P}(a) \cap R_1' \aleph_\alpha = \mathcal{P}(a)$. Furthermore since $b \subseteq a$ implies $\text{rank}(b) \leq \text{rank}(a)$ and since $a \in \mathcal{P}(a)$
$$\text{rank} (\mathcal{P}(a)) = \text{rank}(a) + 1 < \aleph_\alpha.$$

Thus $\mathcal{P}(a) \in R_1' \aleph_\alpha$ and hence $R_1' \aleph_\alpha$ is a model of Axiom 4.

From the AC it follows by induction that
$$(\forall \beta < \aleph_\alpha) [\overline{R_1' \beta} < \aleph_\alpha].$$

Indeed $\overline{R_1' 0} = 0 < \alpha$. If $\overline{R_1' \beta} < \aleph_\alpha$ for $\beta < \aleph_\alpha$ then since $\aleph_\alpha$ is inaccessible
$$\overline{R_1' (\beta + 1)} = \mathcal{P}(R_1' \beta) < \aleph_\alpha.$$

If $\beta \in K_{\text{II}}$ and if $\gamma < \beta \rightarrow R_1' \gamma < \aleph_\alpha$, then by Theorem 10.47
$$\overline{R_1' \beta} = \bigcup_{\gamma < \beta} R_1' \gamma \leq \aleph_\alpha \times \overline{\beta} = \ale

(4) STM($R'_1\alpha$, Ax. 4) $\leftrightarrow \alpha \in K_{11}$.

(5) STM($R'_1\omega$, Ax. 5) $\land \neg$ STM ($R'_1(\omega 2)$, Ax. 5).

(6) STM($R'_1\alpha$, Ax. 6) $\leftrightarrow \alpha > 0$.

(7) STM($R'_1\alpha$, Ax. 7) $\leftrightarrow \alpha > \omega$.

In Exercises 8–15 assume $\aleph_\alpha$ an inaccessible cardinal.

(8) $\mathcal{P}(a)$ Abs $R'_1\aleph_\alpha$.

(9) $a \simeq b$ Abs $R'_1\aleph_\alpha$.

(10) cf($\beta$) Abs $R'_1\aleph_\alpha$.

(11) $\beta \in N$ Abs $R'_1\aleph_\alpha$.

(12) $\beta \in N'$ Abs $R'_1\aleph_\alpha$.

(13) Reg($\beta$) Abs $R'_1\aleph_\alpha$.

(14) Inacc$_w(\beta)$ Abs $R'_1\aleph_\alpha$.

(15) Inacc($\beta$) Abs $R'_1\aleph_\alpha$.

Remark. There are several interesting conclusions to be drawn from the foregoing exercises and Proposition 13.40. First we have that if $\aleph_\alpha$ is inaccessible then $R'_1\aleph_\alpha$ is a standard transitive model of ZF. The proof requires AC. From this and Exercise 15 it follows that it is consistent with ZF to assume that there are no inaccessible cardinals. We argue in the following way. Suppose the statement “there exists an inaccessible cardinal” were provable in ZF. Let $\aleph_\alpha$ be the smallest such cardinal. Then $R'_1\aleph_\alpha$ is a standard transitive model of ZF. But from Exercise
