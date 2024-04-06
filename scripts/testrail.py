"""
This script is useful for automated cleanup of completed test artifacts in TestRail.
To use this script replace the placeholder API_URL, PROJECT_ID, USERNAME and PASSWORD with actual TestRail credentials and ensure the requests library is installed
"""

# Configuration
API_URL = " "
PROJECT_ID = " "
USERNAME = " "
PASSWORD = " "

import requests

# Assuming API_URL, USERNAME, and PASSWORD are defined


def get_completed_test_runs():
    url = f"{API_URL}get_runs/{PROJECT_ID}"
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    data = response.json()
    runs = data["runs"]
    completed_runs = [
        run for run in runs if run["is_completed"] or run["completed_on"] is not None
    ]
    return completed_runs


def delete_test_run(run_id):
    url = f"{API_URL}delete_run/{run_id}"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, auth=(USERNAME, PASSWORD))
    if response.status_code != 200:
        print(f"Error deleting test run {run_id}: {response.text}")
    return response.status_code == 200


# New function to fetch completed test plans
def get_completed_test_plans():
    url = f"{API_URL}get_plans/{PROJECT_ID}"
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    data = response.json()
    plans = data.get("plans", [])
    completed_plans = [plan for plan in plans if plan.get("is_completed", False)]
    return completed_plans


# New function to delete a test plan
def delete_test_plan(plan_id):
    url = f"{API_URL}delete_plan/{plan_id}"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, auth=(USERNAME, PASSWORD))
    if response.status_code != 200:
        print(f"Error deleting test plan {plan_id}: {response.text}")
    return response.status_code == 200


# Handling completed test runs
completed_runs = get_completed_test_runs()
for run in completed_runs:
    if delete_test_run(run["id"]):
        print(f"Deleted completed test run: {run['id']}")
    else:
        print(f"Failed to delete test run: {run['id']}")

# Handling completed test plans
completed_plans = get_completed_test_plans()
for plan in completed_plans:
    if delete_test_plan(plan["id"]):
        print(f"Deleted completed test plan: {plan['id']}")
    else:
        print(f"Failed to delete test plan: {plan['id']}")
