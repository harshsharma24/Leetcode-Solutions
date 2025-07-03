from collections import defaultdict, deque

def process_messages(messages):
    # Step 1: Group messages by sender and sort by timestamp
    sender_queues = defaultdict(deque)
    for sender_id, content, timestamp in sorted(messages, key=lambda x: x[2]):
        sender_queues[sender_id].append((timestamp, content))
    
    # Step 2: Create a queue of sender_ids that still have messages
    active_senders = deque([sender for sender in sender_queues if sender_queues[sender]])
    
    result = []
    while active_senders:
        sender_id = active_senders.popleft()
        
        # Pop the next message from this sender
        timestamp, content = sender_queues[sender_id].popleft()
        result.append(content)
        
        # If this sender still has messages, add them back to the end of the queue
        if sender_queues[sender_id]:
            active_senders.append(sender_id)
    
    return result

# Main block to test the function
if __name__ == "__main__":
    input_messages = [
        [1, "Msg A1", 100],
        [2, "Msg B1", 100],
        [3, "Msg C1", 105],
        [1, "Msg A2", 110],
        [2, "Msg B2", 115],
        [2, "Msg B3", 120],
        [1, "Msg A3", 130],
        [1, "Msg A4", 135],
        [4, "Msg D1", 125]
    ]
    
    output = process_messages(input_messages)
    print(output)
