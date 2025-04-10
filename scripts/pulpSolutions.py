import json
from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpBinary, PULP_CBC_CMD


credits = 138
import os
print("Current working directory:", os.getcwd())


def getSolutions():
    # Load players from JSON file
    with open("./resources/data.json") as f:
        players = json.load(f)

    # Create binary decision variables
    player_vars = {
        p["id"]: LpVariable(f"select_{p['id']}", cat=LpBinary) for p in players
    }

    # Set up the problem
    prob = LpProblem("EuroLeague_Fantasy_Team", LpMaximize)

    # Objective: Maximize total predicted points
    prob += lpSum(player_vars[p["id"]] * float(p["calculated"]) for p in players)

    # Constraints
    prob += lpSum(player_vars[p["id"]] for p in players) == 10
    prob += lpSum(player_vars[p["id"]] * float(p["credit"]) for p in players) <= 138
    prob += lpSum(player_vars[p["id"]] for p in players if p["position"] == "G") == 4
    prob += lpSum(player_vars[p["id"]] for p in players if p["position"] == "F") == 4
    prob += lpSum(player_vars[p["id"]] for p in players if p["position"] == "C") == 2

    # Solve it
    prob.solve(PULP_CBC_CMD(msg=False))

    # Get selected players
    selected_players = [p for p in players if player_vars[p["id"]].value() == 1]

    # Totals
    total_credit = sum(float(p["credit"]) for p in selected_players)
    total_points = sum(float(p["calculated"]) for p in selected_players)

    # Output
    print("✅ Selected Players:\n")
    for p in selected_players:
        print(f"{p['name']:30} | {p['position']} | {p['credit']} cr | {p['calculated']} pts")

    print("\n==============================")
    print(f"💰 Total Credit Used: {total_credit}")
    print(f"📊 Total Projected Points: {total_points}")
    print("==============================")
