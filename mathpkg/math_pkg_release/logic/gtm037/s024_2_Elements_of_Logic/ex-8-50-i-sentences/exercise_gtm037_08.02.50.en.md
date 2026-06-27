---
role: exercise
locale: en
chapter: "8"
section: "2"
exercise_number: "8.50"
---

Let IAxm be the set of all sentences of the following kinds (where $\varphi, \psi, \chi \in \text{ISent}$, the set of I-sentences):

$$\varphi \rightarrow (\psi \rightarrow \varphi)$$
$$[\varphi \rightarrow (\psi \rightarrow \chi)] \rightarrow [(\varphi \rightarrow \psi) \rightarrow (\varphi \rightarrow \chi)]$$
$$[(\varphi \rightarrow \psi) \rightarrow \varphi] \rightarrow \varphi.$$

Let $\Gamma\text{-IThm}$ be the intersection of all sets of I-sentences including $\Gamma \cup \text{IAxm}$ and closed under detachment. We write $\Gamma \vdash_{\text{I}} \varphi$ for $\varphi \in \Gamma\text{-IThm}$. Establish the following, where all sentences and sets of sentences are taken from ISent:

(a) $\emptyset \vdash_{\text{I}} \varphi \rightarrow \varphi$.

(b) The deduction theorem for $\vdash_{\text{I}}$.

(c) $\emptyset \vdash_{\text{I}} (\varphi \rightarrow \psi) \rightarrow [(\psi \rightarrow \chi) \rightarrow (\varphi \rightarrow \chi)]$.

(d) If $\Gamma \vdash_{\text{I}} \langle s \rangle$ for each $s \in P$, then $\Gamma \vdash_{\text{I}} \varphi$ for each $\varphi \in \text{ISent}$.

(e) $\emptyset \vdash_{\text{I}} (\varphi \rightarrow \psi) \rightarrow ([(\varphi \rightarrow \chi) \rightarrow \psi] \rightarrow \psi)$.

(f) Call a set $\Gamma$ of I-sentences I-consistent if not $(\Gamma \vdash_{\text{I}} \varphi)$ for some I-sentence $\varphi$. If $\Gamma$ is I-consistent, then $\Gamma$ has a model which is not identically 1.

Hint: use these steps:
(1) there is an $s \in P$ such that not $(\Gamma \vdash_{\text{I}} \langle s \rangle)$;
(2) there is a maximal $\Delta \supseteq \Gamma$ such that not $(\Delta \vdash_{\text{I}} \langle s \rangle)$.
