"""
Daily route optimisation skeleton using OR-Tools.

Final design:
HOME -> Appointment 1 -> Appointment 2 -> ... -> HOME

The travel-time matrix is the cost between nodes.
Each appointment contributes its own service duration.
Later versions add booked time windows and breaks.
"""

from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def solve_route(time_matrix, service_minutes, start_index=0):
    n = len(time_matrix)
    manager = pywrapcp.RoutingIndexManager(n, 1, start_index)
    routing = pywrapcp.RoutingModel(manager)

    def transit(from_index, to_index):
        f = manager.IndexToNode(from_index)
        t = manager.IndexToNode(to_index)
        return int(time_matrix[f][t] + service_minutes[f])

    transit_idx = routing.RegisterTransitCallback(transit)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_idx)

    search = pywrapcp.DefaultRoutingSearchParameters()
    search.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search.time_limit.seconds = 5

    solution = routing.SolveWithParameters(search)
    if not solution:
        return []

    route = []
    idx = routing.Start(0)
    while not routing.IsEnd(idx):
        route.append(manager.IndexToNode(idx))
        idx = solution.Value(routing.NextVar(idx))
    route.append(manager.IndexToNode(idx))
    return route
