# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    Start: (5, 5)
    Is the start a goal? False
    Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    """
    "*** YOUR CODE HERE ***"
    # Stack declaration and formatting
    stack = util.Stack()
    stack.push(((problem.getStartState(), '', 0), []))  # ((Position, action, cost), path)
    visited = []  # Visited node list

    # If stack is empty we finish looking through the whole graph
    while not stack.isEmpty():
        current = stack.pop()  # Get current node from stack

        if problem.isGoalState(current[0][0]):  # If goal we finish the search
            return current[1]  # Return list of actions

        visited.append(current[0][0])
        temp = []  # Temp list where we will add all successor nodes

        for child in problem.getSuccessors(current[0][0]):
            if child[0] not in visited:
                temp.append((child, current[1] + [child[1]]))  # We add the movement as a list (easier to return)

        temp.reverse()  # This is only because we know it will find the best path in small map.

        for item in temp:
            stack.push(item)  # Add successors to visit

    return []  # If answer not found we return empty list


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Queue declaration and formatting
    queue = util.Queue()
    queue.push(((problem.getStartState(), '', 0), []))  # ((Position, action, cost), path)
    visited = []  # Visited node list

    # If queue is empty we finish looking through the whole graph
    while not queue.isEmpty():
        current = queue.pop()  # Get current node from queue

        if problem.isGoalState(current[0][0]):  # If goal we finish the search
            return current[1]  # Return list of actions

        visited.append(current[0][0])

        for child in problem.getSuccessors(current[0][0]):
            if child[0] not in visited:
                visited.append(child[0])  # Add current's childs to visited (so no duplicates can be added in queue)
                queue.push((child, current[1] + [child[1]]))  # Add child and move list to queue

    return []  # If answer not found we return empty list

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    heap = util.PriorityQueue()
    heap.push(((problem.getStartState(), '', 0), [], 0), 0)  # (((position, action, cost), path, acc. cost), priority)

    visited = {problem.getStartState(): 0}
    while not heap.isEmpty():
        current = heap.pop()
        if problem.isGoalState(current[0][0]):
            return current[1]  # Goal found

        for child in problem.getSuccessors(current[0][0]):
            if child[0] not in visited or current[2] + child[2] < visited[child[0]]:
                if child[0] in visited:
                    visited[child[0]] = current[2]+child[2]
                else:
                    visited.update({child[0]: current[2]+child[2]})
                heap.push((child, current[1] + [child[1]], current[2] + child[2]),
                          current[2] + child[2] + heuristic(child[0], problem))
                # Priority = current acc. cost + next cost + heuristic
    return []  # No solution found


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
