---
role: proof
locale: en
of_concept: theorem-15-8-inseparable-recursive-function
source_book: gtm037
source_chapter: "15"
source_section: "3"
---

Let $f$ be a recursive function satisfying Definition 6.21 for the effectively inseparable pair $g^{+*} \Gamma$ and $M = g^{+*} \{ \varphi : \varphi \text{ is a sentence and } \neg \varphi \in \Gamma \}$. Given $\Delta$ as in the statement, set

$$A = g^{+*} \Delta \cup \{ x : x \text{ is not the Gödel number of a sentence} \}$$

and

$$B = g^{+*} \{ \varphi : \varphi \text{ is a sentence and } \neg \varphi \in \Delta \}.$$

Then $g^{+*} \Gamma \subseteq A$, $M \subseteq B$, $A \cap B = 0$, and both $A$ and $B$ are r.e. Say $A = \operatorname{Dmn} \varphi_{e}^{1}$ and $B = \operatorname{Dmn} \varphi_{r}^{1}$. Then $f(e, r) = g^{+} \varphi$ for some $\varphi$ as desired in the conclusion.

We define a partial recursive function $k'$ by setting

$$k'(x, e) \simeq \mu y \,[(e, x, y) \in \mathrm{T}_{1} \text{ or } x \notin g^{+*} \mathrm{Sent}_{\mathcal{L}}],$$

for all $x, e \in \omega$. Say $k' = \varphi_{r}^{2}$. Note that

$$\operatorname{Dmn} k' = \{ (x, e) : x \in \operatorname{Dmn} \varphi_{e}^{1} \text{ or } x \notin g^{+*} \mathrm{Sent}_{\mathcal{L}} \}.$$

The construction ensures that for any index $e$ with $g^{+*} \Delta = \operatorname{Dmn} \varphi_{e}^{1}$, the value $h e$ yields the Gödel number of a sentence independent of $\Delta$.
