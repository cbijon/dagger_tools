# dagger_tools
Some tools for DAGGER project

# Node Leaderboard Information Retrieval

This script allows you to retrieve information about a specific node from the SHDW Rewards Oracle node leaderboard.

## Usage

1. Make sure you have Python installed on your system.
2. Install the required packages by running the following command:
pip3 install requests
3. Run the script with the following command:
python3 dagger_leaderboard.py <node_address>
Replace `<node_address>` with the actual node address you want to check.

## Example

```bash
python3 dagger_leaderboard.py 77DXfdCcBrivtbvLDXA5kKwHmnALCCqRmRBwMKCtaKKT
Node Rank: 1
Total Rewards: 246.55829145
Node Status: top_150

Output
The script will display the rank, total rewards, and status of the specified node.
```

Notes
The total rewards are presented in SHDW.
