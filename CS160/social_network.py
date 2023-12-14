# Name: Sahil Bains
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
###
#  Problem 1a
###

# Building a practice graph with 6 nodes, 5 of which
# are connected through an edge but 'E' node isolated

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()
    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")
    # Adding the nodes D and E to the graph
    practice_graph.add_nodes_from(["D", "E"])
    # Adding the edges from D to A, B, C, and D
    practice_graph.add_edge("D", "B")
    practice_graph.add_edge("D", "C")
    practice_graph.add_edge("D", "E")
    practice_graph.add_edge("C", "F")
    practice_graph.add_edge("D", "F")

    assert isinstance(practice_graph, nx.Graph)
    assert set(practice_graph.nodes) == {'A', 'B', 'C', 'D', 'E', 'F'}
    return practice_graph

## Function that draws the graph
def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###


## Function that establishes the relationship web of the
#  Shakespearean play: Romeo and Juliet 
def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rjg = nx.Graph()
    rjg = nx.Graph()
    rjg.add_edge("Nurse", "Juliet")
    rjg.add_edge("Juliet", "Tybalt")
    rjg.add_edge("Juliet", "Friar Laurence")
    rjg.add_edge("Juliet", "Capulet")
    rjg.add_edge("Juliet", "Romeo")
    rjg.add_edge("Tybalt", "Capulet")
    rjg.add_edge("Capulet", "Escalus")
    rjg.add_edge("Capulet", "Paris")
    rjg.add_edge("Friar Laurence", "Romeo")
    rjg.add_edge("Romeo", "Benvolio")
    rjg.add_edge("Romeo", "Montague")
    rjg.add_edge("Romeo", "Mercutio")
    rjg.add_edge("Benvolio", "Montague")
    rjg.add_edge("Montague", "Escalus")
    rjg.add_edge("Escalus", "Mercutio")
    rjg.add_edge("Escalus", "Paris")
    rjg.add_edge("Mercutio", "Paris")

    return rjg


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    # Finding immediate friends of the profile
    friends_are_immediate = friends(graph, user)
    # Storing friend of friends
    every_friend = set()
    # Iterating through all of immediate friends
    for friend in friends_are_immediate:
        # Adding immediate friends of current friend to
        # set of friend of friends
        every_friend.update(friends(graph, friend))
        # Removing the profile from original set
    every_friend.discard(user)
    every_friend.difference_update(friends_are_immediate)
    return every_friend


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends
    that user1 and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    f1 = set(graph.neighbors(user1))
    f2 = set(graph.neighbors(user2))
    return f1.intersection(f2)


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    # Creating a set of user friends
    profile_friends = set(graph[user])
    # Creating dictionary to store common friends map
    common_friends_map = {}
    # Iterating over every profile
    for alt_user in graph:
        # Checking if the user is neither a given user or their friend
        if alt_user != user and alt_user not in profile_friends:
            other_user_friends = set(graph[alt_user])
            common_friends = profile_friends.intersection(other_user_friends)
            # Checking if there's one common friend
            if len(common_friends) > 0:
                common_friends_map[alt_user] = len(common_friends)

    return common_friends_map


def number_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    def sort_key(key1):
        return (-map_with_number_vals[key1], key1)

    return sorted(map_with_number_vals.keys(), key=sort_key)


def rec_number_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common frriends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    # Geting the list of the user's friends
    profile_friends = set(graph[user])

    # Finding the common friends between the user and their friends
    common_friends = {}
    for friend in profile_friends:
        for common_friend in graph[friend]:
            if common_friend != user and common_friend not in profile_friends:
                common_friends.setdefault(common_friend, 0)
                common_friends[common_friend] += 1

    # Sorting the recommended friends by number of common friends, then by name
    # Couldn't figure function out without lambda
    sorted_recommended = sorted(common_friends.items(), key=lambda x: (-x[1], x[0]))

    # Return a list of recommended friends
    return [friend for friend, count in sorted_recommended]


#  Problem 3
###


def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    # Finding all common friends of profile and their friends
    # Getting the set of profile's friends and the set of
    # their friends' friends
    friends = set(graph[user])
    fof = set()
    for friend in friends:
        fof.update(graph[friend])

    # Removing profile and profile's friends from
    # the set of friends of friends
    fof.discard(user)
    fof -= friends

    # Computing influence scores for each person
    # in the set of friends of friends
    scores = {}
    for person in fof:
        common_friends = friends & set(graph[person])
        total_influence = sum(1 / len(graph[friend]) for friend in common_friends)
        scores[person] = total_influence

    return scores


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    # Getting the profile's friends
    friends = graph[user]

    # Finding friends who aren't a friend of the profile
    recommend = [friend for friend in graph if friend not in friends and friend != user]

    # Sorting recommendations on the influence score
    # Could not find solution without lambda
    recommend.sort(key=lambda x: (-len(set(graph[x]) & set(friends)), x))

    # Limiting the output to the expected amount
    recommend = recommend[:5]
    return recommend

###
#  Problem 5
###


def get_facebook_graph(filename):
    """Builds and returns the facebook graph"""
    G = nx.Graph()
    with open(filename) as f:
        for line in f:
            line = line.strip().split()
            u, v = int(line[0]), int(line[1])
            G.add_edge(u, v)
    return G


facebook = get_facebook_graph('facebook-links-small.txt')


def main():
    # practice_graph = get_practice_graph()
    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_practice_graph(practice_graph)

    # rj = get_romeo_and_juliet_graph()
    # Comment out this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:\n")

    # Loading the graph
    rjg = get_romeo_and_juliet_graph()

    same_rec = []
    different_rec = []

    # Finding the users with same recommendation
    for main_user in rjg.nodes:
        if recommend_by_influence(rjg, main_user):
            same_rec.append(main_user)
        else:
            different_rec.append(main_user)

    # Printing users with same recommendations
    print("Unchanged Recommendations:", sorted(same_rec))
    # Printing users with different recommendations
    print("Changed Recommendations:", sorted(different_rec))

    ###
    #  Problem 5
    ###

    def get_facebook_graph(filename):
        """Builds and returns the facebook graph"""
        G = nx.Graph()
        with open(filename) as f:
            for line in f:
                line = line.strip().split()
                u, v = int(line[0]), int(line[1])
                G.add_edge(u, v)
        return G

    facebook = get_facebook_graph('facebook-links-small.txt')
    # assert len(facebook.nodes()) == 63731
    # assert len(facebook.edges()) == 817090
    # print(len(facebook.nodes()))

    ###
    #  Problem 6
    ###

    print("\nProblem 6:\n")

    # Looping through the User IDs in their sorted list
    for item in sorted([int(x) for x in facebook]):
        # Converting the userID into an integer
        u_id = int(item)
        # checking if user ID is a multiple of 1000 and present in graph
        if u_id % 1000 == 0 and u_id in facebook:
            recommendations = rec_number_common_friends(facebook, item)
            # Printing the user IDs and their friend recommendations
            print(u_id, "(by num_common_friends):", recommendations[:10])

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:\n")

    for i in sorted([int(x) for x in facebook]):
        # Converting the userID into an integer
        us_id = int(i)
        # checking if user ID is a multiple of 1000 and present in graph
        if us_id % 1000 == 0 and us_id in facebook:
            recommendations = recommend_by_influence(facebook, i)
            # Printing the user IDs and their friend recommendations
            print(i, "(by influence):", recommendations[:10])

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:\n")

    # Results for number of users with same/different
    # first 10 friend recommendations
    same_result = 0
    diff_result = 0

    # Looping through users with ID multiples of 1000
    for x in sorted([int(x) for x in facebook]):
        us_id = int(x)
        if us_id % 1000 == 0 and us_id in facebook:
            # Getting first 10 friend recommendations
            # for both recommendation systems
            recs_by_influence = recommend_by_influence(facebook, x)[:10]
            recs_by_random = rec_number_common_friends(facebook, x)[:10]
            # Checking if the recommendations are the same or different
            if recs_by_influence == recs_by_random:
                same_result += 1
            else:
                diff_result += 1

    # Printing output

    print(f"Same: {same_result}")
    print(f"Different: {diff_result}")


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# NA
