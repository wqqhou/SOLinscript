from solathon import Client, Transaction, Keypair
from solathon.core.instructions import *
import config
import time

# connected to private RPC
client = Client(f'{config.RPC}', local=True)

# Prepare the info needed for the transaction
sender = Keypair().from_private_key(f'{config.private_key}')
program = PublicKey('MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr')
tx_data = bytes(f'{config.inscription}','utf-8')
account = AccountMeta(sender.public_key, True, True)
instruction = Instruction(keys=[account], program_id=program, data=tx_data)

# Create & Send the transaction, then print the result.
for i in range(0, config.tx_count):
    time.sleep(3)
    transaction = Transaction(instructions=[instruction], signers=[sender])
    result = client.send_transaction(transaction)
    print(result)
