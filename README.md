# MooZi: A High-Performance Game-playing System that Plans with a Learned Model 
Author: Zeyi Wang

This repo contains the sourcecode and compiled PDF of the work of Zeyi Wang.
A thesis submitted in partial fulfillment of the requirements for the degree of Master of Science in Department or Computing Science at University of Alberta.
The sourcecode of MooZi is [available here](https://github.com/uduse/moozi).

## Abstract
The intent of this thesis is to develop a high-performance open-source system that plans with a learned model and to understand the algorithm through extensive analysis. We formulate the problem of maximizing accumulated rewards in Markov Decision Processes, and we frame playing games as such problems. We develop the MooZi system to solve these problems. MooZi includes (1) a MuZero-based algorithm that plans with a learned model (2) a distributed architecture that trains and evaluates the algorithm efficiently, and (3) a collection of tools to visualize and understand the algorithm. We empirically show that MooZi outperforms PPO and AC in MinAtar environments. We also show that MooZi learns to play the two-players board game Breakthrough. We use our tools to analyze the learned model by visualizing search trees and learned representation. We make MooZi publicly available to accelerate future research.
