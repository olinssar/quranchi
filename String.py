import pyrogram

app = pyrogram.Client(
    "session_name",
    29086176,
    "d8825825375f883ceb201f2ab1459ba2",
    in_memory=True
)

app.start()

string_session = app.export_session_string()

app.send_message("me", f"`{string_session}`")

print("\n\nCHECK SAVED MESSAGES")
