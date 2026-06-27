---
role: proof
locale: en
of_concept: proposition-14-8
source_book: gtm055
source_chapter: "13-14"
source_section: "Section 15_Section_15"
---

Proof. If the given topology on $\mathcal{E}$ is induced by some countably determined separating family $\{\sigma_{\gamma}\}_{\gamma \in \Gamma}$ of pseudonorms, and if $\{\sigma_{\gamma}\}_{\gamma \in \Gamma_0}$ is a countable cofinal subfamily, then $\{\sigma_{\gamma}\}_{\gamma \in \Gamma_0}$ also induces the given topology on $\mathcal{E}$ (and is therefore also separating). Likewise, if a countable separating family $\{\sigma_{\gamma}\}_{\gamma \in \Gamma_0}$ of pseudonorms is arranged in a sequence $\{\sigma_n\}$, then according to the proof of Proposition 11.32,

$$|x| = \sum_{n=1}^{\infty} \frac{1}{2^n} \frac{\sigma_n(x)}{1 + \sigma_n(x)}, \quad x \in \mathcal{E},$$

(16)

defines a quasinorm that also induces the given topology on $\mathcal{E}$. Thus (i) implies (ii), (ii) implies (iii), and it is obvious that (iii) implies (iv). The proof will be completed by showing that (iv) implies (i). To this end it would suffice to invoke Propositions 11.32 and 14.7, but a direct proof is easy to give. Suppose $\mathcal{E}$ is locally convex and metrizable, and let $\{U_n\}_{n=1}^{\infty}$ be a countable neighborhood base at 0 in $\mathcal{E}$. It follows from Proposition 14.7 that for every positive integer $n$ there exists an absolutely convex neighborhood $V_n$ of 0

then $\{\tau_{\gamma}\}_{\gamma \in \Gamma}$ is a family of pseudonorms on $\mathcal{E}$, and it may be seen that the topology induced on $\mathcal{E}$ by the family $\{\tau_{\gamma}\}$ is simply the topology inversely induced by $T$, i.e., the coarsest topology on $\mathcal{E}$ making $T : \mathcal{E} \rightarrow \mathcal{F}$ continuous. Indeed, if $\mathcal{T}$ denotes this latter topology, then $\mathcal{T}$ is a linear topology on $\mathcal{E}$ (Prob. 11R), and every pseudonorm $\tau_{\gamma}$ is continuous on $\mathcal{E}$ with respect to $\mathcal{T}$. Hence $\mathcal{T}$ refines the topology induced by the family $\{\tau_{\gamma}\}$ (Prop. 11.26). On the other hand, if $V$ is an arbitrary neighborhood of 0 with respect to $\mathcal{T}$, then it is a straightforward consequence of Proposition 11.27 (and the definition of $\mathcal{T}$) that there exist indices $\gamma_1, \ldots, \gamma_n$ and a positive number $\varepsilon$ such that

$$T^{-1}(\{y \in \mathcal{F} : \sigma_{\gamma_i}(y) < \varepsilon, i = 1, \ldots, n\}) = \{x \in \mathcal{E} : \tau_{\gamma_i}(x) < \varepsilon, i = 1, \ldots, n\}$$

is contained in $V$, which shows that $\mathcal{T}$ is, in turn, refined by the topology induced by the family $\{\tau_{\gamma}\}$. Thus, in particular, if $T : \mathcal{E} \rightarrow \mathcal{F}$ is a linear transformation and if $\mathcal{F}$ is a locally convex space, then $\mathcal{E}$ is also locally convex in the topology inversely induced by $T$.

Next suppose given an indexed family $\{T_{\delta}\}_{\delta \in \Delta}$ of linear transformations of a linear space $\mathcal{E}$ into a (similarly indexed) family $\{\mathcal{F}_{\delta}\}$ of locally convex spaces, so that $T

quasinorm to work with. Moreover, in view of Proposition 14.8, it is by and large unnecessary to do so. The following criterion is frequently useful in verifying the completeness of a Frechét space.
