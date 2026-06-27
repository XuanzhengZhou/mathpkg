---
role: proof
locale: en
of_concept: sentential-equivalence-congruence
source_book: gtm037
source_chapter: "9"
source_section: "Elements of Logic"
---

(i) The relation $\equiv_{\Gamma}$ is reflexive because $\Gamma \vdash \varphi \leftrightarrow \varphi$ for any $\varphi$. It is symmetric because $\vdash (\varphi \leftrightarrow \psi) \rightarrow (\psi \leftrightarrow \varphi)$. It is transitive because if $\Gamma \vdash \varphi \leftrightarrow \psi$ and $\Gamma \vdash \psi \leftrightarrow \chi$, then $\Gamma \vdash \varphi \leftrightarrow \chi$ by a propositional tautology.

(ii) Suppose $\varphi \equiv_{\Gamma} \varphi'$ and $\psi \equiv_{\Gamma} \psi'$. Then $\Gamma \vdash \varphi \leftrightarrow \varphi'$ and $\Gamma \vdash \psi \leftrightarrow \psi'$. By sentential logic, $\vdash (\varphi \leftrightarrow \varphi') \rightarrow (\neg \varphi \leftrightarrow \neg \varphi')$, so $\Gamma \vdash \neg \varphi \leftrightarrow \neg \varphi'$. Similarly, $\vdash (\varphi \leftrightarrow \varphi') \rightarrow ((\psi \leftrightarrow \psi') \rightarrow ((\varphi \rightarrow \psi) \leftrightarrow (\varphi' \rightarrow \psi')))$, hence $\Gamma \vdash (\varphi \rightarrow \psi) \leftrightarrow (\varphi' \rightarrow \psi')$. The verification for other connectives (if present) is analogous.
