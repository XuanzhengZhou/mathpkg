```yaml
---
role: proof
source_book: gtm-0073
chapter: I
section: "I.2"
proof_technique: direct-verification
locale: en
content_hash: ""
written_against: ""
---
($\Rightarrow$) If $H \leq G$, then for any $a,b \in H$, $b^{-1} \in H$ since $H$ is a group, and $ab^{-1} \in H$ by closure.

($\Leftarrow$) Since $H \neq \emptyset$, there exists $a \in H$. Taking $a = b$ gives $e = aa^{-1} \in H$, so $H$ contains the identity. For any $b \in H$, taking $a = e$ gives $eb^{-1} = b^{-1} \in H$, so $H$ is closed under inverses. For any $a,c \in H$, write $c = b^{-1}$ for some $b \in H$; then $ac = a(b^{-1}) = ab^{-1} \in H$, so $H$ is closed under the group operation. Associativity in $H$ is inherited from $G$. Hence $H$ is a subgroup.
