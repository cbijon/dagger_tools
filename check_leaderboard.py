import sys
import requests

def get_node_info(node_address):
    # API endpoint for node leaderboard
    api_url = "https://shdw-rewards-oracle.shdwdrive.com/node-leaderboard"
    
    # Fetch JSON data from the API
    response = requests.get(api_url)
    data = response.json()

    # Find the node in the data
    node_info = next((node for node in data["nodes"] if node["node_id"] == node_address), None)

    if node_info:
        # Get rank, rewards, and status for the specified node
        rank = data["nodes"].index(node_info) + 1
        rewards = int(node_info["total_rewards"]) / 1_000_000_000  # Divide by 1 billion
        status = node_info["status"]
        return rank, rewards, status
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <node_address>")
        sys.exit(1)

    node_address_to_check = sys.argv[1]
    result = get_node_info(node_address_to_check)

    if result:
        rank, rewards, status = result
        print(f"Node Rank: {rank}")
        print(f"Total Rewards: {rewards}")
        print(f"Node Status: {status}")
    else:
        print("Node not found in the leaderboard.")
