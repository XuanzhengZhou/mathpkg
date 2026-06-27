---
role: proof
locale: en
of_concept: theorem-23-23
source_book: gtm008
source_chapter: "3"
source_section: "3 A consequence of"
---
In most cases $B$ satisfies the additional requirement that $V^{(B)}$ is a model of $ZF$. In this case we can prove the $AC$ in $V^{(B)}$ by a forcing argument just as in Theorem 14.25 with suitable modifications as in the proof of Theorem 23.24. below. However, since we shall give an example of a Boolean algebra $B$ such that $V^{(B)}$ does not satisfy the Axiom of Powers, we indicate a direct proof of Theorem 23.23 in the general case. We take the Axiom of Choice in the following form:

$(\forall u)(\exists v)(\forall x \in u)[(\exists y \in x)(\exists! x' \in u)[y \in x'] \rightarrow (\exists! y \in x)[y \in v]]$.

Let $\phi(x, y)$ be $y \in x \wedge (\exists! x' \in u)[y \in x']$, $u \in V^{(B)}$. Since $\bigcup_{x \in \mathcal{D}(u)} \mathcal{D}(x)$ is a set, let $\{y_\xi | \xi < \alpha\}$ be an enumeration of this set (using the $AC$ in $V$). Then define $v \in V^{(B)}$ by

$$\mathcal{D}(v) = \bigcup_{x \in \mathcal{D}(u)} \mathcal{D}(x) = \{y_\xi | \xi < \alpha\},$$

$(\forall y \in \mathcal{D}(v)) \left[ v(y) = \sum_{x \in \mathcal{D}(u)} \sum_{\xi < \alpha} ([y = y_\xi \wedge \phi(x, y_\xi)] \cdot \prod_{\eta < \xi} [\neg \phi(x, y_\eta)]] \right]$.

Note that $v(y) \in B$, since we have only sup's and inf's over sets. Now one can show that

$(\forall y, y' \in

all the sums which are definable in $M$. (The set of these sums is countable. Note that $B^M$ is only a class in $M$, so $h_0$ need not be $M$-complete, but $h_0$ preserves all the sums 6 in the proof of Theorem 14.22.) Finally, let $F = \{b \in B^M \mid h_0(b) = 1\}$ be the ultrafilter corresponding to $h_0$. As in Theorem 14.22 there is a mapping

$$h: (V^{(B)})^M \xrightarrow{\text{onto}} M[F]$$

such that

$$M[F] \models \varphi(h(u_1), \ldots, h(u_n)) \leftrightarrow h_0([\varphi(u_1, \ldots, u_n)]) = 1$$

for $u_1, \ldots, u_n \in (V^{(B)})^M$, $\varphi$ a formula of $\mathcal{L}^*$. We have to show that $M[F] \models ACH$. Using the language $\mathcal{L}^*$ we can define in $M$ (a Gödelization of) the ramified language obtained from $\mathcal{L}^*$ and $M$ (i.e., with ordinals ranging over the ordinals in $M$), and we can express the syntactical notion of “$U$ is a constant term” in $M$ as well as $[u \in v]$ and $[u = v]$. Let $D$ be the denotation operator related to $M[F]$. $D(u)$ can be expressed as follows

$$D(u) = \{D(v) \mid \rho(v) < \rho(u) \land [v \in u] \in F\}.$$

Using $H^M$, we have an $M$-definable well-ordering of $M$ and hence an $M$-definable well-ordering $\leq$ of the constant terms. For $x_1, x_2 \in M[F]$, let $C(x_1)$ be the first $y$ (w.r.t. $\leq$) such that

where $a$ is a set and for each $x$ in $a$, $A$ "x is a basic open class. Then $\tilde{B}$ is the completion of $B$ and, referring to the remark preceding Theorem 23.21, $B$ can be regarded as a class of sets. We define $\check{P}$, $\leq$, $G$ by

$$[u \in \check{P}] \triangleq \sum_{p \in P} [u = \check{p}]$$

$$[\check{≤}(u, v)] \triangleq \sum_{p_1, p_2 \in P \atop p_1 \leq p_2} [u = \check{p}_1] \cdot [u = \check{p}_2]$$

$$[u \in G] \triangleq \sum_{p \in P} [u = \check{p}] \cdot [p]^{-0}.$$

Now consider

$$V^{(B)} \triangleq \langle V^{(B)}, \equiv, \bar{\epsilon}, M, \check{P}, \check{≤}, G \rangle.$$

First we prove that

1. $$[\forall i \in \omega)(\exists \alpha)(\exists p \in \check{P})[\langle i, \alpha \rangle \in p \wedge p \in G]] = 1.$$

By Theorem 23.4,

$$[\forall i \in \omega)(\exists \alpha)(\exists p \in \check{P})[\langle i, \alpha \rangle \in p \wedge p \in G]] = \prod_{i < \omega} \sum_{\alpha \in On} \sum_{p \in P \atop \langle i, \alpha \rangle \in p} [\check{p} \in G].$$

But for each $i \in \omega$

$$\sum_{\alpha \in On} \sum_{p \in P \atop \langle i, \alpha \rangle \in p} [\check{p} \in G] \geq \sum_{\alpha \in On} [\{\langle i, \alpha \rangle\}]

Now, in order to show that the Axiom of Replacement does not hold in $V^{(B)}$, let $\varphi(i, \alpha)$ be $(\exists p \in \check{P})[\langle i, \alpha \rangle \in p \wedge p \in G]$. Then, by 1-3,

$$\llbracket (\forall i \in \omega)(\exists! \alpha) \varphi(i, \alpha) \wedge (\forall \alpha)(\exists i \in \omega) \varphi(i, \alpha) \rrbracket = 1$$

i.e., $\varphi$ determines a function from $\omega$ onto $On$ in $V^{(B)}$, but

$$\llbracket (\exists v)(\forall i < \omega)(\exists x \in v) \varphi(i, x) \rrbracket = 0,$$

therefore the Axiom of Replacement does not hold in $V^{(B)}$.
