import json

from screening_ai.conversation_engine import (
    ConversationStateMachine
)

from screening_ai.error_handling import (
    detect_issue
)

with open(
    "screening_ai/conversation_flow.json",
    "r"
) as f:
    flow = json.load(f)

engine = ConversationStateMachine(flow)

while not engine.is_end():

    print("\nAI:", engine.get_question())

    answer = input("User: ")

    issue = detect_issue(answer)

    if issue == "silence":
        engine.handle_silence()

    elif issue == "confusion":
        engine.handle_confusion()

    elif issue == "repeat":
        engine.handle_repeat()

    else:
        engine.next()

print("\nInterview Completed")