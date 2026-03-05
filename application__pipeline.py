from collections import deque
# Create an empty queue
application_inbox = deque()

# Create an empty stack
processed_history = []
startup_names = [" TechCorp ", "bio-gen", " AI Labs ", "Future-Tech"]
for name in startup_names:
    cleaned_name = name.strip().lower()
    application_inbox.append(cleaned_name)
    while application_inbox:
    name = application_inbox.popleft()
    print("Approving:", name)

    processed_history.append(name)
    last_processed = processed_history.pop()
print("Reverting approval for:", last_processed)
from collections import deque

# Initialize structures
application_inbox = deque()
processed_history = []

# Messy startup names
startup_names = [" TechCorp ", "bio-gen", " AI Labs ", "Future-Tech"]

# Clean and add to queue
for name in startup_names:
    cleaned_name = name.strip().lower()
    application_inbox.append(cleaned_name)

# Process applications (FIFO)
while application_inbox:
    name = application_inbox.popleft()
    print("Approving:", name)
    processed_history.append(name)

# Undo last approval (LIFO)
last_processed = processed_history.pop()
print("Reverting approval for:", last_processed)

