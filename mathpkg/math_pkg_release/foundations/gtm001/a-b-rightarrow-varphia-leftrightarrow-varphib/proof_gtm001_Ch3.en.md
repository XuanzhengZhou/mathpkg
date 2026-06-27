---
role: proof
locale: en
of_concept: a-b-rightarrow-varphia-leftrightarrow-varphib
source_book: gtm001
source_chapter: "3"
source_section: ""
---

** (By induction on $n$ the number of logical symbols in $\varphi$). If $n = 0$, then $\varphi(a)$ is of the form $c \in d$, $c \in a$, $a \in c$, or $a \in a$. Clearly

$$a = b \rightarrow [c \in d \leftrightarrow c \in d].$$

From the definition of equality

$$a = b \rightarrow [c \in a \leftrightarrow c \in b].$$

From Proposition 3.3

$$a = b \rightarrow [a \in c \leftrightarrow b \in c].$$

Again from the definition of equality and Proposition 3.3 respectively

$$a = b \rightarrow [a \in a \leftrightarrow a \in b],$$

$$a = b \rightarrow [a \in b \leftrightarrow b \in b].$$

Therefore

$$a = b \rightarrow [a \in a \leftrightarrow b \in b].$$

As our induction hypothesis we assume the result true for each wff having fewer than $n$ logical symbols. If $n > 0$ and $\varphi(a)$ has exactly $n$ logical symbols, then $\varphi(a)$ must be of the form

(1) $\neg \psi(a)$, (2) $\psi(a) \land \eta(a)$, or (3) $(\forall x) \psi(a, x)$.

In Cases (1) and (2) $\

Thus if $\varphi(a)$ is $\neg \psi(a)$ or $\psi(a) \wedge \eta(a)$,

$$a = b \rightarrow [\varphi(a) \leftrightarrow \varphi(b)].$$

If $\varphi(a)$ is $(\forall x)\psi(a, x)$ we first choose a free variable $c$ that is distinct from $a$ and $b$ and which does not occur in $\psi(a, x)$. Since $\psi(a, c)$ has fewer than $n$ logical symbols it follows from the induction hypothesis that

$$a = b \rightarrow [\psi(a, c) \leftrightarrow \psi(b, c)].$$

Generalizing on $c$ in this formula, using Logical Axiom 4, and the following result from logic

$$(\forall x)[\psi(a, x) \leftrightarrow \psi(b, x)] \rightarrow [(\forall x)\psi(a, x) \leftrightarrow (\forall x)\psi(b, x)]$$

we arrive at the conclusion that

$$a = b \rightarrow [(\forall x)\psi(a_1 x) \leftrightarrow (\forall x)\psi(b_1 x)].$$

Remark. Extensionality assures us that a set is completely determined by its elements. From a casual acquaintance with this axiom one might assume that extensionality is a substitution principle having more to do with logic than set theory. This suggests that if equality were taken as a primitive notion then perhaps this axiom could be dispensed with. Dana Scott$^1$ however, has proved that this cannot be done without weakening the system. Thus, even if we were to take equality as a primitive logical notion it would still be necessary to add an extensionality axiom.$^2$

$^1$ Essays on the Foundations of Mathematics. Amsterdam: North-Holland Publishing Company 1962, pp. 115–131.

$^2$ See Quine, Willard Van Orman. Set Theory and its Logic. Cambridge: Harvard University Press, 1969, 30f.

CHAPTER 4
Classes

We pointed out in the Introduction that one objective of axiomatic set theory is to avoid the classical paradoxes. One such paradox, the Russell paradox, arose from the naïve acceptance of the idea that given any property there exists a set whose elements are those objects having the given property, i.e., given a wff $\varphi$ containing one free variable, there exists a set that contains all objects for which $\varphi$ holds and contains no object for which $\varphi$ does not hold. More formally there exists a set $a$ such that

$$(\forall x)[x \in a \leftrightarrow \varphi(x)].$$

This principle, called the Axiom of Abstraction, was accepted by Frege in his Grundgesetze der Arithmetik (1893). In a letter$^1$ to Frege (1902) Bertrand Russell pointed out that the principle leads to the following paradox.

Consider the wff $b \notin b$. If there exists a set $a$ such that

$$(\forall x)[x \in a \leftrightarrow x \notin x]$$

then in particular

$$a \in a \leftrightarrow a \notin a.$$

The idea of the collection of all objects having a specified property is so basic that we could hardly abandon it. But if it is to be retained how shall the paradox be resolved? The Zermelo–Fraenkel approach is the following.

For each wff $\varphi(a, a_1, \ldots, a_n)$ we will introduce a class symbol

$$\{x \mid \varphi(x, a_1, \ldots, a_n)\}$$

$^1$ van Heijenoort, Jean. From Frege to Gödel. Cambridge: Harvard University Press, 1967, pp. 124–125.

which is read “the class of all $x$ such that $\varphi(x, a_1, \ldots, a_n)$.” Our principal interpretation is that the class symbol $\{x \mid \varphi(x)\}$ denotes the class of individuals that have the property $\varphi$. We will show that class is an extension of the notion of set in that every set is a class but not every class is a set.

We will extend the $\in$-relation to class symbols in such a way that an object is an element of a class $\{x \mid \varphi(x)\}$ if and only if that object is a set and it has the defining property for the class. The Russell paradox is then resolved by showing that $\{x \mid x \notin x\}$ is a proper class, i.e., a class that is not a set. It is then disqualified for membership in any class, including itself, on the grounds that it is not a set.

Were we to adjoin the symbols

$$\{x \mid \varphi(x)\}$$

to our object language it would be necessary to extend our rules for wffs and add axioms governing the new symbols. We choose instead to introduce classes as defined terms. It is, of course, essential that we provide an effective procedure for reducing to primitive symbols any formula that contains a defined term. We begin by defining the contexts in which class symbols are permitted to appear. Our only concern will be their appearance in wffs in the wider sense as defined by the following rules.
