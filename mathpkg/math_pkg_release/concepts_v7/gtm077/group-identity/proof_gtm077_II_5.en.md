---
role: proof
locale: en
of_concept: group-identity
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Existence and Uniqueness of the Identity Element (Theorem 16)

**Theorem 16.** In every group $\mathfrak{G}$ there exists a uniquely determined element $E$ (called the *unit element* or *identity*) such that for every element $A$ of the group,

$$AE = EA = A.$$

*Proof.* The proof proceeds in two parts: first we establish the existence of a right identity, then a left identity, and finally we show they coincide.

**1. Existence of a right identity.** Consider an arbitrary but fixed element $A \in \mathfrak{G}$. By axiom (iv), there exists an element $E$ (depending a priori on $A$) such that

$$AE = A.$$

Now let $B$ be any element of $\mathfrak{G}$. Again by axiom (iv), there exists an element $Y$ such that $YA = B$. Then, using the associative law (ii),

$$BE = (YA)E = Y(AE) = YA = B.$$

Thus $BE = B$ holds for *every* $B \in \mathfrak{G}$. Hence $E$ is a *right identity*: it satisfies $BE = B$ for all $B$, and in particular $E$ does not depend on the choice of the original element $A$.

**2. Existence of a left identity.** By an entirely symmetric argument, applying axiom (iv) in the form $YA = B$, one obtains the existence of an element $E'$ such that

$$E'A = A$$

for every $A \in \mathfrak{G}$. (Alternatively, fix $A$, find $E'$ with $E'A = A$ by (iv); then for any $B$, write $B = AX$ by (iv), and $E'B = E'(AX) = (E'A)X = AX = B$.) Thus $E'$ is a *left identity*.

**3. Equality and uniqueness.** Apply the right identity property with $B = E'$ and the left identity property with $A = E$:

$$E'E = E \qquad \text{and} \qquad E'E = E'.$$

Hence $E = E'$. Therefore there exists a *unique two-sided identity* $E$ satisfying $AE = EA = A$ for all $A \in \mathfrak{G}$.

This element is called the *unit element* and plays the role of the number $1$ in ordinary multiplication; it is accordingly also denoted by $1$. The unit element may be omitted as a factor in any product without affecting the result. $\square$
