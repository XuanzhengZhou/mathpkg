---
role: proof
locale: en
content_hash: ""
written_against: ""
source: gtm-0073
section: "I.2"
---

# Proof of Theorem 2.5

($\Leftarrow$) Assume $ab^{-1} \in H$ for all $a,b \in H$. Since $H \neq \emptyset$,
there exists $a \in H$. Taking $b = a$ gives $e = aa^{-1} \in H$, so $H$ contains
the identity.

For any $b \in H$, taking $a = e$ (now known to be in $H$) gives
$b^{-1} = eb^{-1} \in H$, so $H$ is closed under inverses.

For any $a,b \in H$, we now know $b^{-1} \in H$, so
$ab = a(b^{-1})^{-1} \in H$, proving $H$ is closed under the group operation.
Associativity is inherited from $G$. Thus $H$ is a subgroup.

($\Rightarrow$) If $H$ is a subgroup of $G$, then for any $a,b \in H$, the element
$b^{-1} \in H$ (subgroups contain inverses) and $ab^{-1} \in H$ (subgroups are
closed under the product). The condition is therefore necessary.
