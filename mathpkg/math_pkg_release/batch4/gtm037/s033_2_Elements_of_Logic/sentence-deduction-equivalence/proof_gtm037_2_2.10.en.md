---
role: proof
locale: en
of_concept: sentence-deduction-equivalence
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

$(\Gamma\text{-Thm}) \cap \text{Sent} \in \Delta$ clearly satisfies 10.84 (i)-(ii). Hence $\Gamma\text{-Thm}'' \subseteq (\Gamma\text{-Thm}) \cap \text{Sent}$, so $\Gamma \vdash'' \varphi \Rightarrow \Gamma \vdash \varphi$.

To prove the converse, let

$$\Delta = \{\varphi \in \text{Fmla}: \text{for all } m \in \omega \text{ and all } \alpha \in {}^m\text{Rng } v, \text{ if } \forall \alpha_0 \cdots \forall \alpha_{m-1} \varphi \text{ is a sentence then } \Gamma \vdash'' \forall \alpha_0 \cdots \forall \alpha_{m-1} \varphi\}.$$

Clearly $\text{Axm} \cup \Gamma \subseteq \Delta$ and $\Delta$ is closed under generalization. To show that $\Delta$ is closed under detachment it clearly suffices to show

(1) if $n \in \omega$, $\alpha \in {}^n\text{Rng } v$, $\forall \alpha_0 \cdots \forall \alpha_{n-1}(\varphi \rightarrow \psi)$ is a sentence, $\Gamma \vdash'' \forall \alpha_0 \cdots \forall \alpha_{n-1} \varphi$, and $\Gamma \vdash'' \forall \alpha_0 \cdots \forall \alpha_{n-1}(\varphi \rightarrow \psi)$, then $\Gamma \vdash'' \forall \alpha_0 \cdots \forall \alpha_{n-1} \psi$.

This is established just like (1) in the proof of 10.32.

Hence $\Gamma\text{-Thm} \subseteq \Delta$, so $\Gamma \vdash \varphi \Rightarrow \Gamma \vdash'' \varphi$ when $\varphi$ is a sentence. $\square$

[Note: The proof is truncated in the source — the final line is cut off, but the argument is complete from context.]
