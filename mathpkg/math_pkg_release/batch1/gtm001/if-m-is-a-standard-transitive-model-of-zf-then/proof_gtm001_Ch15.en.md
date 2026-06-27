---
role: proof
locale: en
of_concept: if-m-is-a-standard-transitive-model-of-zf-then
source_book: gtm001
source_chapter: "15"
source_section: ""
---

(1) Since $0 \in M$ and $F'0 = 0$ it follows that $0 \in L^M$ and hence $L^M$ is not empty. Furthermore if $y \in x \in L^M$ then

$$(\exists \alpha \in M)[y \in x = F' \alpha \subseteq F'' \alpha].$$

Therefore $(\exists \beta < \alpha)[y = F' \beta]$. But $\alpha \in M$ and $M$ is transitive. Thus $\beta \in M$ and $y \in L^M$, and hence $L^M$ is transitive.

Since $L$ is a model of ZF + AC + GCH + $V = L$ it follows that if $\varphi$ is any axiom of ZF + AC + GCH + $V = L$ then $\varphi^L$ is a theorem of ZF. Since $M$ is a model of ZF every theorem of ZF relativized to $M$ is a theorem of ZF. Therefore $(\varphi^L)^M$ is a theorem of ZF. Then by Theorem 15.48 $\varphi^{L^M}$ is a theorem of ZF. Hence $L^M$ is a model of $\varphi$.

Consequently $L^M$ is a standard transitive model of ZF + AC + GCH + $V = L$.

By Theorem 15.27, $\text{On}^L = \text{On}$. Relativizing to $M$ we have $\text{On}^{L^M} = \text{On}^M$. Details are left to the reader.

(2) The proof is left to the

Gödel’s use of the Axiom of Constructibility to prove the relative consistency of ZFC, and ZFC + GCH, might suggest that he introduced constructibility simply as a means to an end. That, however, is not at all the case. Gödel held his discovery of constructible sets, and his proof that the class of constructible sets, $L$, is a model of ZFC, to be by itself, one of his major achievements. His confidence in the importance of the notion of constructibility was further vindicated when in 1967 Ronald Björn Jensen used $V = L$ to solve a problem in real analysis, the Souslin problem. In addition Jensen derived, from $V = L$, three principles that can be understood and used by people who are not specialists in set theory. Following Jensen, Saharon Shelah in 1974, used $V = L$ to settle a problem in group theory, the Whitehead problem.$^1$

In view of these results it is natural to ask about the status of the Axiom of Constructibility, $V = L$. If one is of the opinion that the purpose of set theory is to axiomatize the largest possible part of Cantor’s world of sets, then $V = L$ must be rejected because it is severely restrictive. But rejecting $V = L$ as an axiom does not diminish the importance of constructibility and the achievements of Jensen. Rather it directs our attention to $L$, which is the smallest natural universe of sets. To understand $L$ is an important part of understanding set theory. With Jensen the first step was taken toward a better understanding of $L$.

In the late 1970s, at a date unknown to the authors because he did not publish his results, Jack Silver introduced a special technique for deriving consequences of $V = L$ and hence for deriving information about $L$. This technique involves the use of structures that Silver called machines and

$^1$ For a discussion of Jensen’s solution of the Souslin problem and Shelah’s solution of the Whitehead problem see Devlin, Keith J. The Axiom of Constructibility: A Guide for the Mathematician. Lecture Notes in Mathematics, Vol. 617, New York: Springer-Verlag, 1977

which are now known as Silver machines. In this chapter we will study an elementary part of the theory of Silver machines.

A Silver machine is a special kind of structure that we call an algebra. But to define an algebra we need some preliminary notions and notation:
