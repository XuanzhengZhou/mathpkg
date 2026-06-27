---
role: proof
locale: en
of_concept: if-vdash-varphi-and-if-a-is-a-nonempty-class-that-satisfies-each-nonlogical-axio
source_book: gtm001
source_chapter: "11"
source_section: ""
---

We regard (1) as the special case of (2) with $n = 0$. Since $\varphi$ is a theorem it has a proof and indeed by hypothesis a proof in which each nonlogical axiom is satisfied by $A$. Suppose that the sequence of wff

$$\eta_1, \ldots, \eta_m$$

is such a proof. Then $\eta_m$ is $\varphi$ and each $\eta_k$ is either an axiom or is inferred from previous formulas in the sequence by one of the rules of inference. Our procedure is to show that the sequence

$$\eta_1, \ldots, \eta_m$$

can be modified to produce a proof of (2). More precisely we will prove by induction that for each $\eta_k$, $k = 1

If $\eta_k$ is of the form $[\psi \rightarrow [\theta \rightarrow \zeta]] \rightarrow [[\psi \rightarrow \theta] \rightarrow [\psi \rightarrow \zeta]]$ or $[\neg \psi \rightarrow \neg \theta] \rightarrow [\theta \rightarrow \psi]$ an argument similar to the foregoing leads to

$$b_1, \ldots, b_p \in A \rightarrow \eta_k^A.$$

If $\eta_k$ is of the form $(\forall x)[\psi \rightarrow \theta] \rightarrow [\psi \rightarrow (\forall x)\theta]$ where $x$ is not free in $\psi$ then from the tautology $[p \rightarrow [q \rightarrow r]] \rightarrow [q \rightarrow [p \rightarrow r]]$ we have

$$[x \in A \rightarrow [\psi^A \rightarrow \theta^A]] \rightarrow [\psi^A \rightarrow [x \in A \rightarrow \theta^A]].$$

By generalization and Axiom 4

$$(\forall x)[x \in A \rightarrow [\psi^A \rightarrow \theta^A]] \rightarrow [\psi^A \rightarrow (\forall x)[x \in A \rightarrow \theta^A]]],$$

and hence

$$b_1, \ldots, b_p \in A \rightarrow \eta_k^A.$$

If $\eta_k$ is of the form $(\forall x)\psi(x) \rightarrow \psi(a)$ then as an instance of this same axiom we have

$$(\forall x)[x \in A \rightarrow \psi^A(x)] \rightarrow [a \in A \rightarrow \psi^A(a)].$$

Therefore

$$a \in A \rightarrow [(\forall x \in A)\psi^A(x) \rightarrow \psi^A(a)]$$

and hence

$$b_1, \ldots, b_p \in A \rightarrow \eta_k^A.$$

If $\eta_k$ is an axiom of ZF then by hypothesis $A \models \eta_k$, and from

Since $A \neq 0$

$$b_1, \ldots, b_p \in A \land c_1, \ldots, c_{q-1} \in A \rightarrow \eta_k^A.$$

With $q - 1$ repetitions we obtain

$$b_1, \ldots, b_p \in A \rightarrow \eta_k^A.$$

Case 3. If $\eta_k$ is inferred from $\eta_i$ by generalization then there is an $a$ not among $b_1, \ldots, b_p$. From the induction hypothesis

$$b_1, \ldots, b_p \in A \land a \in A \rightarrow \eta_i^A(a).$$

Since $a$ is not among $b_1, \ldots, b_p$ we have by generalization and Axiom 4

$$b_1, \ldots, b_p \in A \rightarrow (\forall x \in A) \eta_i^A(x).$$

Remark. From Theorem 12.6 we see that if a proof of a wff $\varphi$ requires only the logical axioms then every nonempty class $A$ will be a model of $\varphi$. In particular every nonempty class $A$ is a model of the logical axioms and if two wffs are logically equivalent, i.e.,

$$\vdash_{\text{LA}} \varphi \leftrightarrow \psi$$

then a nonempty class $A$ is a model of $\varphi$ iff it is a model of $\psi$.

We are interested in classes $A$ that are models of ZF. Since there are infinitely many axioms for ZF the assertion that $A$ is a model of ZF is the assertion that each wff in a certain infinite collection of wffs is a theorem in ZF. This assertion we abbreviate as the metastatement, $A \models ZF$.

From Theorem 12.6 we see that if $A \models ZF$ then every theorem of ZF holds in $A$, that is, $A$ satisfies each theorem of ZF. In the next section we will give conditions on $A$ that assure that $A \models ZF$. One

(3) $[A, R] \models \varphi \leftrightarrow B \models \varphi$ if $\varphi$ is closed.

(4) If all of the free variables of $\varphi$ are among $a_1, \ldots, a_n$ and if

$$a_1, \ldots, a_n \in A$$

then

$$[A, R] \models \varphi(a_1, \ldots, a_n) \leftrightarrow B \models \varphi(F'a_1, \ldots, F'a_n).$$

(1) If $R$ Wfr $A \wedge x \in A$ it then follows that $(R^{-1})' \{x\}$ is a set. Therefore if $f \mathcal{F}_n(R^{-1})' \{x\}$ then $\mathcal{W}(f)$ is a set. Let

$$K = \{f | (\exists z \subseteq A) [f \mathcal{F}_n z \wedge (\forall x \in z) [f'x = \{f'y|yRx\} \wedge (R^{-1})' \{x\} \subseteq z]\}.$$

Then any two functions in $K$ have the same values at any point common to their domains: Otherwise there would exist an $f$ and $g$ in $K$ and an $x$ in $\mathcal{D}(f) \cap \mathcal{D}(g)$ such that $f(x) \neq g(x)$. If $c = \{x \in \mathcal{D}(f) \cap \mathcal{D}(g)|f'x \neq g'x\}$ then $c \neq 0 \wedge c \subseteq A$. Therefore $(\exists x \in c)[c \cap (R^{-1})' \{x\} = 0]$. Since $x \in c$

$$(R^{-1})' \{x\} \subseteq \mathcal{D}(f) \wedge (R^{-1})' \{x\} \subseteq \mathcal{D}(g).$$

Then $yRx$ implies $f'y = g'y$ and hence

$$f'

If

$$F = \cup(K)$$

and if $\langle a, x \rangle \in F \land \langle a, y \rangle \in F$ then $(\exists f \in K)(\exists g \in K)[x = f'a \land y = g'a]$. But since $a \in \mathcal{D}(f) \cap \mathcal{D}(g), f'a = g'a$, i.e., $x = y$. Therefore $F$ is a function.

Furthermore $(\forall f \in K)(\forall x \in \mathcal{D}(f))[F'x = f'x]$; consequently

$$F'x = f'x = \{f'y|yRx\} = \{F'y|yRx\}.$$

From this it follows that $F$ is one-to-one, for if not there is an $x$ and a $y$ in $\mathcal{D}(F)$ for which $F'x = F'y$ but $x \neq y$. From Proposition 9.4 it then follows that there is an R-minimal $x$ in $\mathcal{D}(F)$ for which $(\exists y \in \mathcal{D}(F))[x \neq y \land F'x = F'y]$. Then

$$F'x = \{F'z|zRx\} = \{F'w|wRy\} = F'y.$$

From this and the defining property of $x$ it then follows that $zRy$ if and only if $zRx$ and hence $x = y$. This is a contradiction.

Since

$$\mathcal{D}(F) = \bigcup_{f \in K} \mathcal{D}(f)$$

and $f \in K$ implies $\mathcal{D}(f) \subseteq A$ it follows that $\mathcal{D}(F) \subseteq A$. If $A - \mathcal{D}(F) \neq 0$ then by Proposition 9.4, $A - \mathcal{D}(F)$ has an R-minimal element, that is

$$(\exists x \in A - \mathcal{D}(F))[A - \mathcal{D}(F) \

Furthermore $y R x$ implies $y \in a - \{x\}$ and hence $g' y = F' y$. Therefore

$$g' x = \{g' y | y R x\}.$$

If $z \neq x$ then since $z \in \mathcal{D}(g)$, $g' z = F' z$. But

$$F' z = \{F' y | y R z\}.$$

If $y R z$ and $z \in a$, then $y \in a$. Furthermore since $z$ is connected to $x$ by a finite R-chain and since $R$ is well founded, $y \neq x$. Then $g' y = F' y$ and

$$g' z = \{g' y | y R z\}.$$

Since $a$ is the domain of $g$ and $a$ is closed under $R^{-1}$ it follows that $g \in K$. Hence $x \in a \subseteq \mathcal{D}(F)$. This is a contradiction from which we conclude that $\mathcal{D}(F) = A$.

Thus if $B = F'' A$ then

$$F: A \xrightarrow{1-1} B.$$

Furthermore $a \in b \wedge b \in B$ implies that $(\exists x \in A)[a \in b \wedge b = F' x]$. But

$$F' x = \{F' y | y R x\}.$$

Thus $(\exists y)[y R x \wedge a = F' y]$, i.e., $a \in B$ and hence $B$ is transitive.

Also $a \in A \wedge b \in A \wedge a R b \rightarrow F' a \in \{F' y | y R b\} = F' b$. Therefore

$$F \text{ Isom}_{R, E}(A, B).$$

We have now proved (1) and (2). Since (3) is the special case of (4) with $n = 0$ it is sufficient to prove (4). This we do by induction on the number, $n$, of logical symbols in $\varphi$. If $n = 0$, then

If $\varphi$ is of the form $\psi \wedge \eta$ and all of the free variables of $\varphi$ are among $a_1, \ldots, a_n$ then so are the free variables of $\psi$ and of $\eta$. From the induction hypothesis if $a_1 \in A \wedge \cdots \wedge a_n \in A$ then

$$[A, R] \models \psi(a_1, \ldots, a_n) \leftrightarrow B \models \psi(F'a_1, \ldots, F'a_n)$$

$$[A, R] \models \eta(a_1, \ldots, a_n) \leftrightarrow B \models \eta(F'a_1, \ldots, F'a_n).$$

Therefore

$$[A, R] \models \psi(a_1, \ldots, a_n) \wedge [A, R] \models \eta(a_1, \ldots, a_n) \leftrightarrow B \models \psi(F'a_1, \ldots, F'a_n)$$

$$\wedge B \models \eta(F'a_1, \ldots, F'a_n).$$

Hence

$$[A, R] \models [\psi(a_1, \ldots, a_n) \wedge \eta(a_1, \ldots, a_n)] \leftrightarrow B \models [\psi(F'a_1, \ldots, F'a_n)$$

$$\wedge \eta(F'a_1, \ldots, F'a_n)].$$

If $\varphi$ is of the form $(\forall x)\psi(x)$ and if all of the free variables of $\varphi$ are among $a_1, \ldots, a_n$ then there is an $x$ not among $a_1, \ldots, a_n$ and all of the free variables of $\psi(x)$ are among $a_1, \ldots, a_n$, $x$. From the induction hypothesis if $a_1 \in A \wedge \cdots \wedge a_n \in A$ then

$$x \in A \rightarrow [[A, R] \models \psi(x, a

A basic part of the interpretation of our theory is that each wff $\varphi(x)$ expresses a property that a given individual $a$ has or does not have according as $\varphi(a)$ holds or does not hold. Then $\varphi^A(x)$ expresses the “same” or “corresponding” property for the universe $A$.

Consider, for example, the existence of an empty set. Earlier we proved that there exists an individual $a$, called the empty set, having the property

$(\forall x)[x \notin a]$.

From the Axiom of Regularity it follows that every nonempty class $A$, as a universe, has this property. In particular, the class of infinite cardinal numbers $N'$ contains an individual $a$ with the property

$(\forall x \in N')[x \notin a]$.

The set in $N'$ that plays the role of the empty set is $\aleph_0$, a set that is far from empty. Thus when viewed from within the universe $N'$, $\aleph_0$ is empty but when viewed from “without,” i.e., in $V$, $\aleph_0$ is not empty.

There are however properties $\varphi(x)$ and universes $A$ such that an individual of $A$ has the property when viewed from within $A$ iff it has the property when viewed from without. Such a property is said to be absolute with respect to $A$.
