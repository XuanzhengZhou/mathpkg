---
role: proof
locale: en
of_concept: inconsistency-finite-conjunction-criterion
source_book: gtm037
source_chapter: "Chapter 8: Sentential Logic"
source_section: "2. Elements of Logic"
---
[Proof truncated in source OCR.]

(i) $\Rightarrow$ (ii). Assuming (i), we have $\Gamma \vdash \bot$ (falsum), so by the finiteness of proofs, there is a finite $\Gamma_0 \subseteq \Gamma$ with $\Gamma_0 \vdash \bot$. By the Generalized Deduction Theorem (Lemma 8.36), this yields $\vdash \bigwedge_{i \leq m} \neg \varphi_i$ for appropriate formulas $\varphi_i \in \Gamma_0$ (after transforming the proof using logical manipulations).

(ii) $\Rightarrow$ (i). If $\vdash \bigwedge_{i \leq m} \neg \varphi_i$, then in particular $\Gamma \vdash \bigwedge_{i \leq m} \neg \varphi_i$ since each $\varphi_i \in \Gamma$. But $\bigwedge_{i \leq m} \neg \varphi_i \rightarrow \bot$ is a tautology (it asserts that all $\varphi_i$ hold while their negations also hold), so $\Gamma \vdash \bot$, making $\Gamma$ inconsistent.

[The complete proof relies on the Generalized Deduction Theorem (Lemma 8.36) and properties of the generalized conjunction.]
