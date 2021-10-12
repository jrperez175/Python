from hashlib import sha256
import time

MAX_NONCE = 1000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number,transaction,previos_hash,prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) +transaction + previos_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f'Successfully mined bitcoins wirh nonce value: {nonce} ')
            return new_hash
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__ == '__main__':
    transactions = '''
    Dhaval->Bhavin->20,
    Mando->Cara->45,
    '''
    difficulty = 6
    star_time = time.time()
    print("Start_mining")
    new_hash = mine(5,transactions,'8ds8ds',difficulty)
    total_time = str(time.time() - star_time)
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
