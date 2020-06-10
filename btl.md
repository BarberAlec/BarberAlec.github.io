## Bayesian Transfer Learning
Transfer learning is the process of using knowledge learned from one or more source tasks, to help increase the learning rate of another target learning task. Take for example a pianist learning the organ. The pianist already knows the fundamentals of sheet music and other related skills. We would then expect that they would learn the organ faster relative to another person who had no musical experience. Transfer learning attempts to bring this knowledge transfer into an AI context.

This research looks at the case of transfer learning in a Bayesian setting. Bayesian statistics is a technology that allows for the processing of knowledge and data into a personal belief of an unknown object of interest in a mathematically justified manner. While investigations into transfer learning in a Bayesian setting in research exists,  it is far more common to employ more traditional *black box* methods which rely on an algorithm finding correlations and patterns between different inputs in a hard to  interpret way. More specifically, this research looks at an assumption that most Bayesian transfer learning methods make about how the underlying relationships between different tasks relate to each other. This dissertation attempts to define a framework which does not make any assumptions on theses relationships.


## Background Techniques
### Distributed Opinion Pooling
#### Logarithmic Pooling
A mechanism for merging knowledge from multiple experts. Finds the distribution on an unknown object of interest theta, given a set of beliefs (distributions) \\[ \mathbf{F} = \{f_1(\theta), ... , f_m(\theta) \} \\] and a set of corresponding weights \\[w_1, ... , w_m \\].

\\[ f^{\circ} \equiv f^{\circ}(\theta)=\sum_{i=1}^{m}\left[f_{i}(\theta)\right]^{w_{i}}\\]

It is KLD (Kullback-Leibler divergence) optimial as follows:

\\[ f^{\circ} \equiv \arg \min _{f \in F} \sum_{i=1}^{m} w_{i} D\left[f \| f_{i}\right] \\]

I.e. it finds the distribution which is closest, in a KLD sense, to the sum of the weighted KLDs with each distribution.

#### Linear Pooling
Interstingly, if we inverse the KLD function above as shown below, we can find the new optimial combination is linear pooling.

\\[ f^{\circ} \equiv \arg \min _{f \in F} \sum_{i=1}^{m} w_{i} D\left[f_{i} \|f \right] \\]


## Our Contribution 