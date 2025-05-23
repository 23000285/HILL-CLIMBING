#!/usr/bin/env python
# coding: utf-8

import random
import string

def generate_random_solution(answer):
    # Find the length of the answer and store in l
    l = len(answer)
    # Generate a random list of characters of the same length
    return [random.choice(string.printable) for _ in range(l)]

def evaluate(solution, answer):
    print("Evaluating:", "".join(solution))
    target = list(answer)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        # Calculate ASCII difference between characters
        diff += abs(ord(s) - ord(t))
    return diff

def mutate_solution(solution):
    # Randomly mutate one character in the solution
    ind = random.randint(0, len(solution) - 1)
    solution[ind] = random.choice(string.printable)
    return solution

def SimpleHillClimbing():
    answer = "Artificial Intelligence"
    best = generate_random_solution(answer)
    best_score = evaluate(best, answer)
    while True:
        print("Score:", best_score, " Solution:", "".join(best))  
        if best_score == 0:
            break
        new_solution = mutate_solution(list(best))
        score = evaluate(new_solution, answer)   
        if score < best_score:
            best = new_solution
            best_score = score

# Run the hill climbing algorithm
SimpleHillClimbing()
