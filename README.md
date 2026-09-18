# SOLinscript
``` 
git clone https://github.com/wqqhou/SOLinscript.git

cd SOLinscript

cp config.py.example config.py

nano config.py 

python3 tx.py
``` 

# Solana Transaction Automation

A small Python utility for constructing and submitting repeated Solana memo/inscription transactions through a configurable RPC endpoint.

## What it does

- Loads an RPC endpoint, local private key, inscription payload, and transaction count from configuration.
- Constructs a Solana Memo Program instruction containing the configured inscription data.
- Signs transactions locally with the configured keypair and submits them through the RPC client.
- Automates repeated submissions with a short delay between transactions.

## Technical focus

**Python, Solathon, Solana RPC, transaction construction, digital signatures, workflow automation**

The repository is intentionally small and focuses on programmatic transaction construction and repeated blockchain interaction.
