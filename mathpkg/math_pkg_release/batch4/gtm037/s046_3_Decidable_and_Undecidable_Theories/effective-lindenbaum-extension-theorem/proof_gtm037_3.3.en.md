---
role: proof
locale: en
of_concept: effective-lindenbaum-extension-theorem
source_book: gtm037
source_chapter: "3"
source_section: "3"
---

Intuitively we proceed as follows, merely effectivizing a proof of Lindenbaum's Theorem 11.13. Effectively list out all sentences. Now extend $\Gamma$ by an effective, recursive procedure: at the $m$th step, add the $m$th sequence if it is consistent to do so, otherwise add nothing. In this way we extend $\Gamma$ to a complete theory $\Delta$ with $g^{+*} \Delta$ r.e.; by 15.2, $\Delta$ is decidable.

More formally, we proceed as follows. Let $h$ be a recursive function with range $g^{+*} \text{Sent}$ and with $h0 \in g^{+*} \Gamma$. Now we define a function $f$ by recursion. Let

$$f0 = h0$$
$$f(m + 1) = hm \quad \text{if } \Gamma \not\supset \bigwedge_{i < m} g^{+-1} fi \rightarrow \neg g^{+-1} hm,$$
$$f(m + 1) = fm \quad \text{otherwise.}$$

Let $\Delta = g^{+-1} \text{Rng} f$. Now $\Delta$ is consistent. For, by induction it is clear (see the proof of the next theorem) that $\Gamma \cup \{g^{+-1} fi : i < m\}$ is consistent for each $m \in \omega$; so it follows, of course, that $\Gamma \cup \Delta$ is consistent. A fortiori, $\Delta$ is consistent. Furthermore, $\Gamma \subseteq \Delta$. For, assume that $\varphi \in \Gamma$, say $hm = \varphi$. Clearly then, since we have already established that $\Gamma \cup \{g^{+-1} fi : i < m\}$ is consistent, it follows that $f(m + 1) = hm$, so $\varphi \in \Delta$. Note that $\Delta$ is a theory, since if $\Delta \models \varphi$, with, say, $hm = \varphi$, then obviously $f(m + 1) = hm$. Next, $\Delta$ is complete, for if $\varphi$ is any sentence, then either it or its negation is consistent with $\Delta$ (by construction, every sentence is considered at some step). Since $\Delta$ is a complete theory with $g^{+*}\Delta$ r.e., by Theorem 15.2, $\Delta$ is decidable.
