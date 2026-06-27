---
role: proof
locale: en
of_concept: theorem-13-22
source_book: gtm008
source_chapter: "12"
source_section: "12 The Independence of the AC

In order to prove the independen"
---
$[[u = \check{\alpha}]] = [[u = \check{\alpha}]] \cdot [[\text{Ord}(\check{\alpha})]] \leq [[\text{Ord}(u)]]$ by Corollary 13.7. Therefore $\sum_{\alpha \in On} [[u = \check{\alpha}]] \leq [[\text{Ord}(u)]]$. In order to prove $[[\text{Ord}(u)]] \leq \sum_{\alpha \in On} [[u = \check{\alpha}]]$, note, from Theorem 13.17, that

$$\alpha \neq \beta \rightarrow [[x = \check{\alpha}]] \cdot [[x = \check{\beta}]] \leq [[\check{\alpha} = \check{\beta}] = 0.$$

Therefore, for each $x \in V^{(B)}$,

$$D_x \triangleq \{ \xi \mid [[x = \check{\xi}]] > 0 \}$$

is a set (using the fact that the mapping $\xi \rightarrow [[x = \check{\xi}]]$ is a one-to-one function on $D_x$ and $[[x = \check{\alpha}]]$ ranges over the set $B$). Thus $D = \bigcup_{x \in \mathcal{D}(u)} D_x$ is a set, and taking an ordinal $\alpha$ greater than sup $D$ we obtain

$(\forall \beta \geq \alpha) (\forall x \in \mathcal{D}(u)) [[x = \check{\beta}] = 0]$.

Therefore

(i) $[[\check{\alpha} \in u]] = \sum_{x \in \mathcal{D}(u)} u(x) \cdot [[x = \check{\alpha}] = 0.$

Since $V^{(B)}$ is a model of $ZF$, $[[\text{Ord}(\check{\alpha})]] = 1$ and

$$[[\text{Ord}(u)] \rightarrow u \in \check{\alpha} \

In order to help the reader in getting more familiar with the Boolean-valued model $V^{(B)}$ we conclude this section with some examples.

1. $$[0 = \check{0}] = 1.$$

Proof. Note that 0 in $\check{0}$ is the empty set in $V$ whereas 0 on the left-hand side of 0 = $\check{0}$ is the empty set in $V^{(B)}$, i.e., 0 = $a$ is to be replaced by its defining formula $(\forall x)[x \notin a]$. Now for $x \in V^{(B)}$,

$$[x \in \check{0}] = \sum_{v \in \mathcal{D}(\check{0})} [x = \check{v}] = 0$$ since $\mathcal{D}(\check{0}) = 0$ (empty set in $V$).

Therefore

$$[(\forall x)[x \notin \check{0}]] = \prod_{x \in V^{(B)}} [x \notin \check{0}] = 1.$$

2. $$[\check{a} + 1 = (\alpha + 1)^{\check{v}}] = 1.$$

Proof. The meaning of 2 is

$$[(\forall \gamma)[\gamma \in \check{a} \vee \gamma = \check{a} \leftrightarrow \gamma \in (\alpha + 1)^{\check{v}}] = 1.$$

To prove this we first note, from Definition 13.3, that

$$[\check{y} \in \check{a} \vee \check{y} = \check{a}] = \left( \sum_{\delta \in \alpha} [\check{δ} = \check{y}] \right) + [\check{a} = \check{y}]$$

$$= \sum_{\delta \in (\alpha + 1)} [\check{δ} = \check{y}]$$

$$= [\check{y} \in (\alpha + 1)^{\check{v}}].$$

Then by Corollary 13.23

$$[(\forall \gamma)[\gamma \in \check{a} \

hence, by the induction hypothesis and 2,

$$[0 \in a \land (\forall x \in a)[x + 1 \in a]] \leq [[(n + 1)^{\vee} \in a]].$$

5. $$[0 \in a \land (\forall x \in a)[x + 1 \in a] \rightarrow \check{\omega} \subseteq a] = 1$$ for $a \in V^{(B)}$.

Proof.

$$[0 \in a \land (\forall x \in a)[x + 1 \in a]] \leq \prod_{n \in \omega} [[\check{n} \in a]]$$ by 4

$$= [[\check{\omega} \subseteq a]].$$

6. $$[\omega = \check{\omega}] = 1.$$

Proof. $\omega = a \leftrightarrow \varphi(a)$ where $\varphi(a)$ is

$$0 \in a \land (\forall x \in a)[x + 1 \in a] \land (\forall y)[0 \in y \land (\forall x \in y)[x + 1 \in y] \rightarrow a \subseteq y].$$

Thus, from 3 and 5, $$[\omega = \check{\omega}] = 1.$$ Therefore, $\omega$ in $V^{(B)}$ is $\check{\omega}$.
