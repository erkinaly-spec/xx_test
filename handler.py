import runpod

def handler(job):
    x = job["input"].get("x", 0)
    y = job["input"].get("y", 0)
    return {"sum": x + y}

runpod.serverless.start({"handler": handler})
