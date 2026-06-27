---
role: proof
locale: en
of_concept: godels-first-incompleteness-theorem
source_book: gtm053
source_chapter: "VII"
source_section: "1"
---

# Proof of Gödel's First Incompleteness Theorem

**Theorem (Gödel's First Incompleteness Theorem).** Let $T$ be a consistent, recursively axiomatizable theory containing enough arithmetic (e.g., Peano Arithmetic PA or Robinson's Q). Then $T$ is incomplete: there exists a sentence $G$ in the language of $T$ such that $T \not\vdash G$ and $T \not\vdash \neg G$.

*Proof.* The proof presented in GTM053 follows Smullyan's approach, using Tarski's theorem on the undefinability of truth and the fact that provability is definable in arithmetic.

**Step 1: Arithmetization of syntax.** Encode formulas, terms, and proofs as natural numbers (Gödel numbering). Under this encoding, the set of (Gödel numbers of) axioms of $T$ is recursive, and the set of (Gödel numbers of) theorems provable from $T$ is recursively enumerable.

**Step 2: Definability of provability.** One constructs an arithmetic formula $\operatorname{Prf}_T(x, y)$ expressing "$x$ is the Gödel number of a proof in $T$ of the formula with Gödel number $y$." The provability predicate is then:
$$\operatorname{Prov}_T(y) \equiv \exists x\, \operatorname{Prf}_T(x, y).$$

Crucially, for any sentence $P$ with Gödel number $\ulcorner P \urcorner$:
- If $T \vdash P$, then $T \vdash \operatorname{Prov}_T(\ulcorner P \urcorner)$.
- The predicate $\operatorname{Prov}_T$ is a $\Sigma_1$-formula (existential quantification over a recursive relation).

**Step 3: The Diagonal Lemma (Fixed Point Lemma).** For any formula $\varphi(x)$ with one free variable, there exists a sentence $\psi$ such that
$$T \vdash \psi \leftrightarrow \varphi(\ulcorner \psi \urcorner).$$

Apply this to $\neg \operatorname{Prov}_T(x)$ to obtain a sentence $G$ (the "Gödel sentence") satisfying:
$$T \vdash G \leftrightarrow \neg \operatorname{Prov}_T(\ulcorner G \urcorner).$$

$G$ asserts: "I am not provable in $T$."

**Step 4: Proof of incompleteness.** 
- If $T \vdash G$, then $T \vdash \operatorname{Prov}_T(\ulcorner G \urcorner)$ (by Step 2). But from the fixed point, $T \vdash \neg \operatorname{Prov}_T(\ulcorner G \urcorner)$, contradicting the consistency of $T$. Hence $T \not\vdash G$.
- If $T \vdash \neg G$, then $T \vdash \operatorname{Prov}_T(\ulcorner G \urcorner)$ (by the fixed point). However, the $\Sigma_1$-completeness of $T$ ensures that $\operatorname{Prov}_T(\ulcorner G \urcorner)$ being true in the standard model implies $T \vdash G$, again contradicting consistency. (This step requires $\omega$-consistency or the stronger assumption; Rosser later refined this to require only simple consistency.)

Thus $G$ is undecidable in $T$: neither $G$ nor $\neg G$ is provable. The sentence $G$ is true in the standard model $\mathbb{N}$, since it asserts its own unprovability, which we have just established.

**Alternative approach via Tarski's Theorem.** GTM053 also presents a proof based on Tarski's theorem on the undefinability of truth: the set of (Gödel numbers of) true arithmetic sentences is not definable in arithmetic. Since the set of provable sentences IS definable (via $\operatorname{Prov}_T$), the two sets cannot coincide, so there must be true but unprovable sentences. $\square$
