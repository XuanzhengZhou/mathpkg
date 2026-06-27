---
role: proof
locale: en
of_concept: if-varphi-abs-a-if-psi-abs-a-if-a-1-ldots-a-m-b-1-ldots-b-n-is-a-list-of-distinc
source_book: gtm001
source_chapter: "11"
source_section: ""
---

Clearly if $b_1, \ldots, b_n \in A$ then
$$[(\forall x_1, \ldots, x_m)[\varphi \rightarrow \psi]] \rightarrow (\forall x_1, \ldots, x_m \in A)[\varphi \rightarrow \psi].$$

The formal details consist of observing that on the hypothesis
$$(\forall x_1, \ldots, x_m)[\varphi \rightarrow \psi]$$
we can deduce $\varphi \rightarrow \psi$ and hence
$$a_m \in A \rightarrow [\varphi \rightarrow \psi].$$

Then by generalization
$$(\forall

But a basic hypothesis of our theorem is that under the hypotheses listed above

$$a_1 \in A.$$

Hence by modus ponens we can deduce

$$(\forall x_2, \ldots, x_m \in A)[\varphi \rightarrow \psi].$$

Repeating this we arrive finally at

$$\psi$$

from which one application of the deduction theorem gives that on the hypotheses

$$b_1, \ldots, b_n \in A, (\forall x_1, \ldots, x_m \in A)[\varphi \rightarrow \psi]$$

we can deduce

$$\varphi \rightarrow \psi.$$

Then by generalization we deduce

$$(\forall x_1) \ldots (\forall x_m)[\varphi \rightarrow \psi]$$

and finally, by the deduction theorem,

$$b_1, \ldots, b_n \in A \rightarrow [(\forall x_1, \ldots, x_m \in A)[\varphi \rightarrow \psi]] \rightarrow$$

$$(\forall x_1, \ldots, x_m)[\varphi \rightarrow \psi]].$$

We then have

$$b_1, \ldots, b_n \in A \rightarrow [(\forall x_1, \ldots, x_m)[\varphi \rightarrow \psi]] \leftrightarrow$$

$$(\forall x_1, \ldots, x_m \in A)[\varphi \rightarrow \psi]].$$

Since $\varphi$ and $\psi$ are each absolute w.r.t. $A$

$$b_1, \ldots, b_n \in A \wedge a_1, \ldots, a_m \in A \rightarrow [\varphi \leftrightarrow \varphi^A],$$

$$b_1, \ldots, b_n \in A \wedge a_1, \ldots, a_m \in A \rightarrow [\psi \leftrightarrow \psi^A].$$

Hence by generalization, properties of equivalence, and the self-distributive law, if $b_1, \ldots, b_n \in A$ then

The proof is left to the reader.
