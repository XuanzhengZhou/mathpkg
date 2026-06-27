```yaml
---
role: proof
source_book: gtm-0073
chapter: I
section: "I.5"
proof_technique: homomorphism-factorization
locale: en
content_hash: ""
written_against: ""
---
Consider $f \colon G \to \operatorname{Im} f$, which is an epimorphism. Apply Theorem 5.6 with $N = \operatorname{Ker} f$. Since $\operatorname{Ker} f$ is a normal subgroup of $G$ contained in the kernel of $f$ (trivially equal to it), Theorem 5.6 yields a unique homomorphism $\bar{f} \colon G / \operatorname{Ker} f \to \operatorname{Im} f$ given by $a(\operatorname{Ker} f) \mapsto f(a)$. The kernel of $\bar{f}$ is $\{a(\operatorname{Ker} f) \mid a \in \operatorname{Ker} f\} = (\operatorname{Ker} f)/(\operatorname{Ker} f)$, the trivial subgroup of $G / \operatorname{Ker} f$. Hence $\bar{f}$ is a monomorphism by Theorem 2.3. Since $f$ is surjective onto $\operatorname{Im} f$, $\bar{f}$ is also surjective. Therefore $\bar{f}$ is an isomorphism.
