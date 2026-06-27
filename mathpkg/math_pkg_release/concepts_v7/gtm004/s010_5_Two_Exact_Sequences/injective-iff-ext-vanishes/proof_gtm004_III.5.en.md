---
role: proof
locale: en
of_concept: injective-iff-ext-vanishes
source_book: gtm004
source_chapter: "III"
source_section: "5"
---

# Proof of Injectivity iff Ext Vanishes (Corollary 5.6)

The $\Lambda$-module $B$ is injective if and only if $\operatorname{Ext}_\Lambda(A, B) = 0$ for all $\Lambda$-modules $A$.

**Proof.** This is the dual assertion to Corollary 5.5.

If $B$ is injective, then for any short exact sequence $0 \rightarrow B \rightarrow E \rightarrow A \rightarrow 0$, the sequence splits, so it represents the zero element in $\operatorname{Ext}_\Lambda(A, B)$. Since every element of $\operatorname{Ext}_\Lambda(A, B)$ arises from such an extension (by Theorem 2.4), we have $\operatorname{Ext}_\Lambda(A, B) = 0$.

Conversely, suppose $\operatorname{Ext}_\Lambda(A, B) = 0$ for all $\Lambda$-modules $A$. Let $B \xrightarrow{\iota} E$ be any monomorphism. Set $A = E / \iota(B)$, giving a short exact sequence

$$
0 \rightarrow B \xrightarrow{\iota} E \rightarrow A \rightarrow 0.
$$

Since $\operatorname{Ext}_\Lambda(A, B) = 0$, this extension splits, so $\iota$ has a left inverse, i.e., $B$ is a direct summand of $E$. This holds for every monomorphism $B \hookrightarrow E$, which is equivalent to $B$ being injective.
