
def parse_task(task):
    task_lower = task.lower()
    metadata = {
        "task": task,
        "type": "indoor",
        "weather_required": "any",
        "daylight_required": False,
        "tide_required": "none"
    }

    if any(word in task_lower for word in ["lawn", "garden", "spread", "build", "shed", "paint", "boat"]):
        metadata["type"] = "outdoor"
        metadata["weather_required"] = "dry"
        metadata["daylight_required"] = True

    if "boat" in task_lower and "launch" in task_lower:
        metadata["tide_required"] = "high"

    if "tax" in task_lower or "submit" in task_lower:
        metadata["type"] = "indoor"

    if "car" in task_lower or "inverness" in task_lower:
        metadata["type"] = "travel"
        metadata["weather_required"] = "safe"

    return metadata
