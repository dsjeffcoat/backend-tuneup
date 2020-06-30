#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Diarte Jeffcoat w/help from Kyle Negley, Janell Huyck, and Jordan Davidson"

import timeit
import cProfile
import pstats
import functools


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.

    @functools.wraps(func)
    def profile_wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        try:
            prof.enable()
            result = func(*args, **kwargs)
            prof.disable()
            return result
        finally:
            p = pstats.Stats(prof)
            p.sort_stats("cumulative").print_stats()
    return profile_wrapper

    # p = pstats.Stats(run_func)
    # result = p.sort_stats('cumulative')
    #     print(result)
    # return profile_wrapper

    #     t = timeit.Timer(stmt='main')
    #     result = t.repeat(repeat=7, number=3)
    #     best_time = min(result)
    #     print(
    #         f"Best time across 7 repeats of 3 runs per repeat: {best_time:.10f} secs")
    #     return result
    # return wrapper_timer
    # cProfile.run(func)


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = {}

    for movie in movies:
        if movie in duplicates:
            duplicates[movie] += 1
        else:
            duplicates[movie] = 1

    result = []
    for movie in duplicates:
        if duplicates[movie] > 1:
            result.append(movie)

            # movies = read_movies(src)
            # duplicates = []
            # while movies:
            #     movie = movies.pop()
            #     if is_duplicate(movie, movies):
            #         duplicates.append(movie)
    return result


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(functools.partial(find_duplicate_movies, "movies.txt"))
    result = t.repeat(repeat=7, number=3)
    best_time = min(result)
    print(
        f"Best time across 7 repeats of 3 runs per repeat: {best_time:.10f} secs")
    # print(result)

    # @functools.partial()
    # def wrapper_timer(*args, **kwargs):
    #     t = timeit.Timer(stmt='main')
    #     result = t.repeat(repeat=7, number=3)
    #     best_time = min(result)
    #     print(
    #         f"Best time across 7 repeats of 3 runs per repeat: {best_time:.10f} secs")
    #     return result
    # return wrapper_timer


def main():
    """Computes a list of duplicate movie entries."""
    timeit_helper()
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()

# # Timer testing

# t = timeit.Timer(stmt='pass', setup='pass')
# result = t.repeat(repeat=7, number=3)
# best_time = min(result)
# print(f"Best time across 7 repeats of 3 runs per repeat: {best_time:.10f}")
